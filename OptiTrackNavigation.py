import os
import unittest
from __main__ import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *

### OptiTrackNavigation
class OptiTrackNavigation(ScriptedLoadableModule):

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "OptiTrackNavigation" # TODO make this more human readable by adding spaces
    self.parent.categories = ["Examples"]
    self.parent.dependencies = []
    self.parent.contributors = ["David Garcia (Laboratorio de Imagen Medica (LIM))"] # replace with "Firstname Lastname (Organization)"
    self.parent.helpText = """
    This is an example of scripted loadable module bundled in an extension.
    """
    self.parent.acknowledgementText = """
    This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc.
    and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.
""" # replace with organization, grant and thanks.

### OptiTrackNavigationWidgety
class OptiTrackNavigationWidget(ScriptedLoadableModuleWidget):

  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)

    # Loading models
    modelsCollapsibleButton = ctk.ctkCollapsibleButton()
    modelsCollapsibleButton.text = "Models"
    self.layout.addWidget(modelsCollapsibleButton)
    parametersFormLayout = qt.QFormLayout(modelsCollapsibleButton)
   
    # Skull model selector    
    self.skullModelSelector = slicer.qMRMLNodeComboBox()
    self.skullModelSelector.nodeTypes = ( ("vtkMRMLModelNode"), "" )
    self.skullModelSelector.selectNodeUponCreation = True
    self.skullModelSelector.addEnabled = False
    self.skullModelSelector.removeEnabled = False
    self.skullModelSelector.noneEnabled = False
    self.skullModelSelector.showHidden = False
    self.skullModelSelector.showChildNodeTypes = False
    self.skullModelSelector.setMRMLScene( slicer.mrmlScene )
    self.skullModelSelector.setToolTip( "Pick the skull model." )
    parametersFormLayout.addRow("Skull model: ", self.skullModelSelector)
      
    # Skull Markers model selector
    self.skullMarkersModelSelector = slicer.qMRMLNodeComboBox()
    self.skullMarkersModelSelector.nodeTypes = ( ("vtkMRMLModelNode"), "" )
    self.skullMarkersModelSelector.selectNodeUponCreation = True
    self.skullMarkersModelSelector.addEnabled = False
    self.skullMarkersModelSelector.removeEnabled = False
    self.skullMarkersModelSelector.noneEnabled = False
    self.skullMarkersModelSelector.showHidden = False
    self.skullMarkersModelSelector.showChildNodeTypes = False
    self.skullMarkersModelSelector.setMRMLScene( slicer.mrmlScene )
    self.skullMarkersModelSelector.setToolTip( "Pick skull markers model." )
    parametersFormLayout.addRow("Skull Markers model: ", self.skullMarkersModelSelector)
    
    # Pointer model selector    
    self.pointerModelSelector = slicer.qMRMLNodeComboBox()
    self.pointerModelSelector.nodeTypes = ( ("vtkMRMLModelNode"), "" )
    self.pointerModelSelector.selectNodeUponCreation = True
    self.pointerModelSelector.addEnabled = False
    self.pointerModelSelector.removeEnabled = False
    self.pointerModelSelector.noneEnabled = False
    self.pointerModelSelector.showHidden = False
    self.pointerModelSelector.showChildNodeTypes = False
    self.pointerModelSelector.setMRMLScene( slicer.mrmlScene )
    self.pointerModelSelector.setToolTip( "Pick the pointer model." )
    parametersFormLayout.addRow("Pointer model: ", self.pointerModelSelector)
          
    # Transform Definition Area
    transformsCollapsibleButton = ctk.ctkCollapsibleButton()
    transformsCollapsibleButton.text = "Transforms"
    self.layout.addWidget(transformsCollapsibleButton)   
    parametersFormLayout = qt.QFormLayout(transformsCollapsibleButton)

    # PointerToTracker transform selector
    self.pointerToTrackerSelector = slicer.qMRMLNodeComboBox()
    self.pointerToTrackerSelector.nodeTypes = ( ("vtkMRMLLinearTransformNode"), "" )
    self.pointerToTrackerSelector.selectNodeUponCreation = True
    self.pointerToTrackerSelector.addEnabled = False
    self.pointerToTrackerSelector.removeEnabled = False
    self.pointerToTrackerSelector.noneEnabled = False
    self.pointerToTrackerSelector.showHidden = False
    self.pointerToTrackerSelector.showChildNodeTypes = False
    self.pointerToTrackerSelector.setMRMLScene( slicer.mrmlScene )
    self.pointerToTrackerSelector.setToolTip( "Pick the PointerToTracker transform." )
    parametersFormLayout.addRow("PointerToTracker transform: ", self.pointerToTrackerSelector)

    # RigidBodyToTracker transform selector
    self.rigidBodyToTrackerSelector = slicer.qMRMLNodeComboBox()
    self.rigidBodyToTrackerSelector.nodeTypes = ( ("vtkMRMLLinearTransformNode"), "" )
    self.rigidBodyToTrackerSelector.selectNodeUponCreation = True
    self.rigidBodyToTrackerSelector.addEnabled = False
    self.rigidBodyToTrackerSelector.removeEnabled = False
    self.rigidBodyToTrackerSelector.noneEnabled = False
    self.rigidBodyToTrackerSelector.showHidden = False
    self.rigidBodyToTrackerSelector.showChildNodeTypes = False
    self.rigidBodyToTrackerSelector.setMRMLScene( slicer.mrmlScene )
    self.rigidBodyToTrackerSelector.setToolTip( "Pick the RigidBodyToTracker transform." )
    parametersFormLayout.addRow("RigidBodyToTracker transform: ", self.rigidBodyToTrackerSelector)

    # TrackerToRigidBody transform selector
    self.trackerToRigidBodySelector = slicer.qMRMLNodeComboBox()
    self.trackerToRigidBodySelector.nodeTypes = ( ("vtkMRMLLinearTransformNode"), "" )
    self.trackerToRigidBodySelector.selectNodeUponCreation = True
    self.trackerToRigidBodySelector.addEnabled = False
    self.trackerToRigidBodySelector.removeEnabled = False
    self.trackerToRigidBodySelector.noneEnabled = False
    self.trackerToRigidBodySelector.showHidden = False
    self.trackerToRigidBodySelector.showChildNodeTypes = False
    self.trackerToRigidBodySelector.setMRMLScene( slicer.mrmlScene )
    self.trackerToRigidBodySelector.setToolTip( "Pick the TrackerToRigidBody transform." )
    parametersFormLayout.addRow("TrackerToRigidBody transform: ", self.trackerToRigidBodySelector)

    # Apply Transforms Button
    self.applyTransformsButton = qt.QPushButton("Apply Transforms")
    self.applyTransformsButton.toolTip = "Apply selected transforms."
    self.applyTransformsButton.enabled = False
    parametersFormLayout.addRow(self.applyTransformsButton)

    # Fiducial Registration Area
    registrationCollapsibleButton = ctk.ctkCollapsibleButton()
    registrationCollapsibleButton.text = "Fiducial Registration"
    self.layout.addWidget(registrationCollapsibleButton)   
    parametersFormLayout = qt.QFormLayout(registrationCollapsibleButton)

    # Label registration 
    registrationLabel = qt.QLabel( "Note: Use Fiducial Registration Wizard module to carry out the fiducial registration.\nParameters: \n"+
                                   "    - From fiducials: SkullModelFiducials (placed directly over the skull model)\n    - To Fiducials: PointerTipFiducials"+
                                   " (placed in the pointer tip when in contact with the markers)\n"+"    - Place fiducials -> Probe transform: PointerTipToTracker\n"+
                                   "    - Registration result transform: SkullToRigidBody\n"+"    - Result transform type: Similarity\n")
    registrationLabel.setWordWrap( True )
    parametersFormLayout.addRow(registrationLabel)
    
    # SkullToRigidBody transform selector    
    self.skullToRigidBodySelector = slicer.qMRMLNodeComboBox()
    self.skullToRigidBodySelector.nodeTypes = ( ("vtkMRMLLinearTransformNode"), "" )
    self.skullToRigidBodySelector.selectNodeUponCreation = True
    self.skullToRigidBodySelector.addEnabled = False
    self.skullToRigidBodySelector.removeEnabled = False
    self.skullToRigidBodySelector.noneEnabled = False
    self.skullToRigidBodySelector.showHidden = False
    self.skullToRigidBodySelector.showChildNodeTypes = False
    self.skullToRigidBodySelector.setMRMLScene( slicer.mrmlScene )
    self.skullToRigidBodySelector.setToolTip( "Pick the SkullToRigidBody transform (output of fiducial registration)." )
    parametersFormLayout.addRow("SkullToRigidBody transform: ", self.skullToRigidBodySelector)
          
    # Apply Registration Result Button    
    self.applyRegistrationButton = qt.QPushButton("Apply")
    self.applyRegistrationButton.toolTip = "Run the algorithm."
    self.applyRegistrationButton.enabled = False
    parametersFormLayout.addRow(self.applyRegistrationButton)

    # connections    
    self.pointerToTrackerSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onSelect)
    self.rigidBodyToTrackerSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onSelect)
    self.trackerToRigidBodySelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onSelect)
    self.applyTransformsButton.connect('clicked(bool)', self.onApplyTransformsClicked)
    self.skullToRigidBodySelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onSelect)
    self.applyRegistrationButton.connect('clicked(bool)', self.onApplyRegistrationClicked)

    # Add vertical spacer
    self.layout.addStretch(1)
    
    # Refresh scene (you only need one function for this)
    self.onSelect()
    
  def cleanup(self):
    pass

  def onSelect(self):    
    self.applyTransformsButton.enabled = self.pointerToTrackerSelector.currentNode() and self.rigidBodyToTrackerSelector.currentNode() and self.trackerToRigidBodySelector.currentNode()
    self.applyRegistrationButton.enabled = self.skullToRigidBodySelector.currentNode()
  
  def onApplyTransformsClicked(self):
    self.applyTransformsButton.enabled = False
    self.pointerToTrackerSelector.enabled = False
    self.rigidBodyToTrackerSelector.enabled = False
    self.trackerToRigidBodySelector.enabled = False
    logic = OptiTrackNavigationLogic()
    logic.buildTransformTree(self.pointerModelSelector.currentNode(), self.pointerToTrackerSelector.currentNode(), self.rigidBodyToTrackerSelector.currentNode(), self.trackerToRigidBodySelector.currentNode())

  def onApplyRegistrationClicked(self):
    self.skullToRigidBodySelector.enabled = False
    logic = OptiTrackNavigationLogic()
    logic.startNavigation(self.pointerModelSelector.currentNode(), self.skullModelSelector.currentNode(), self.skullMarkersModelSelector.currentNode(), self.pointerToTrackerSelector.currentNode(), self.rigidBodyToTrackerSelector.currentNode(), self.trackerToRigidBodySelector.currentNode(), self.skullToRigidBodySelector.currentNode())

### OptiTrackNavigationLogic
class OptiTrackNavigationLogic(ScriptedLoadableModuleLogic):

  def buildTransformTree(self, pointerModelNode, pointerToTrackerTransformNode, rigidBodyToTrackerTransformNode, trackerToRigidBodyTransformNode):
    pointerToTrackerTransformNode.SetAndObserveTransformNodeID(trackerToRigidBodyTransformNode.GetID())
    pointerModelNode.SetAndObserveTransformNodeID(pointerToTrackerTransformNode.GetID())

  def startNavigation(self, pointerModelNode, skullModelNode, skullMarkersModelNode, pointerToTrackerTransformNode, rigidBodyToTrackerTransformNode, trackerToRigidBodyTransformNode, skullToRigidBodyTransformNode):
    # Reset tranform tree
    pointerToTrackerTransformNode.SetAndObserveTransformNodeID(pointerModelNode.GetID())
    
    # Build final transform tree
    skullToRigidBodyTransformNode.SetAndObserveTransformNodeID(rigidBodyToTrackerTransformNode.GetID())
    skullModelNode.SetAndObserveTransformNodeID(skullToRigidBodyTransformNode.GetID())
    skullMarkersModelNode.SetAndObserveTransformNodeID(skullToRigidBodyTransformNode.GetID())
    pointerModelNode.SetAndObserveTransformNodeID(pointerToTrackerTransformNode.GetID())