import os
import unittest
from __main__ import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
# cualquier cosa
#
# OptiTrackNavigation
#

class OptiTrackNavigation(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

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

#
# OptiTrackNavigationWidget
#

class OptiTrackNavigationWidget(ScriptedLoadableModuleWidget):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)
    # Instantiate and connect widgets ...

    # 
    # Loading models Area
    #
    modelsCollapsibleButton = ctk.ctkCollapsibleButton()
    modelsCollapsibleButton.text = "Models"
    self.layout.addWidget(modelsCollapsibleButton)

    # Layout within the dummy collapsible button
    parametersFormLayout = qt.QFormLayout(modelsCollapsibleButton)

    #
    # Skull model selector
    #
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
      
    #
    # Skull Markers model selector
    #
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

    #
    # Pointer model selector
    #
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
   
    #
    # Load Models Button
    #
    self.loadModelsButton = qt.QPushButton("Load Models")
    self.loadModelsButton.toolTip = "Load selected models."
    self.loadModelsButton.enabled = False
    parametersFormLayout.addRow(self.loadModelsButton)
    #
    # Transform Definition Area
    #
    transformsCollapsibleButton = ctk.ctkCollapsibleButton()
    transformsCollapsibleButton.text = "Transforms"
    self.layout.addWidget(transformsCollapsibleButton)

    # Layout within the dummy collapsible button
    parametersFormLayout = qt.QFormLayout(transformsCollapsibleButton)

    #
    # PointerToTracker transform selector
    #
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

    #
    # RigidBodyToTracker transform selector
    #
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

    #
    # TrackerToRigidBody transform selector
    #
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

    #
    # Apply Transforms Button
    #
    self.applyTransformsButton = qt.QPushButton("Apply Transforms")
    self.applyTransformsButton.toolTip = "Apply selected transforms."
    self.applyTransformsButton.enabled = False
    parametersFormLayout.addRow(self.applyTransformsButton)

    #
    # Fiducial Registration Area
    #
    registrationCollapsibleButton = ctk.ctkCollapsibleButton()
    registrationCollapsibleButton.text = "Fiducial Registration"
    self.layout.addWidget(registrationCollapsibleButton)

    # Layout within the dummy collapsible button
    parametersFormLayout = qt.QFormLayout(registrationCollapsibleButton)

    #
    # input volume selector
    #
    self.inputSelector = slicer.qMRMLNodeComboBox()
    self.inputSelector.nodeTypes = ( ("vtkMRMLScalarVolumeNode"), "" )
    self.inputSelector.addAttribute( "vtkMRMLScalarVolumeNode", "LabelMap", 0 )
    self.inputSelector.selectNodeUponCreation = True
    self.inputSelector.addEnabled = False
    self.inputSelector.removeEnabled = False
    self.inputSelector.noneEnabled = False
    self.inputSelector.showHidden = False
    self.inputSelector.showChildNodeTypes = False
    self.inputSelector.setMRMLScene( slicer.mrmlScene )
    self.inputSelector.setToolTip( "Pick the input to the algorithm." )
    parametersFormLayout.addRow("Input Volume: ", self.inputSelector)

    #
    # output volume selector
    #
    self.outputSelector = slicer.qMRMLNodeComboBox()
    self.outputSelector.nodeTypes = ( ("vtkMRMLScalarVolumeNode"), "" )
    self.outputSelector.addAttribute( "vtkMRMLScalarVolumeNode", "LabelMap", 0 )
    self.outputSelector.selectNodeUponCreation = False
    self.outputSelector.addEnabled = True
    self.outputSelector.removeEnabled = True
    self.outputSelector.noneEnabled = False
    self.outputSelector.showHidden = False
    self.outputSelector.showChildNodeTypes = False
    self.outputSelector.setMRMLScene( slicer.mrmlScene )
    self.outputSelector.setToolTip( "Pick the output to the algorithm." )
    parametersFormLayout.addRow("Output Volume: ", self.outputSelector)

    #
    # check box to trigger taking screen shots for later use in tutorials
    #
    self.enableScreenshotsFlagCheckBox = qt.QCheckBox()
    self.enableScreenshotsFlagCheckBox.checked = 0
    self.enableScreenshotsFlagCheckBox.setToolTip("If checked, take screen shots for tutorials. Use Save Data to write them to disk.")
    parametersFormLayout.addRow("Enable Screenshots", self.enableScreenshotsFlagCheckBox)

    #
    # scale factor for screen shots
    #
    self.screenshotScaleFactorSliderWidget = ctk.ctkSliderWidget()
    self.screenshotScaleFactorSliderWidget.singleStep = 1.0
    self.screenshotScaleFactorSliderWidget.minimum = 1.0
    self.screenshotScaleFactorSliderWidget.maximum = 50.0
    self.screenshotScaleFactorSliderWidget.value = 1.0
    self.screenshotScaleFactorSliderWidget.setToolTip("Set scale factor for the screen shots.")
    parametersFormLayout.addRow("Screenshot scale factor", self.screenshotScaleFactorSliderWidget)

    #
    # Apply Button
    #
    self.applyButton = qt.QPushButton("Apply")
    self.applyButton.toolTip = "Run the algorithm."
    self.applyButton.enabled = False
    parametersFormLayout.addRow(self.applyButton)




    # connections
    self.skullModelSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onModelSelect)
    self.skullMarkersModelSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onModelSelect)
    self.pointerModelSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onModelSelect)
    self.loadModelsButton.connect('clicked(bool)', self.onLoadModelsButton)
    self.pointerToTrackerSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onTransformSelect)
    self.rigidBodyToTrackerSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onTransformSelect)
    self.trackerToRigidBodySelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onTransformSelect)
    self.applyTransformsButton.connect('clicked(bool)', self.onApplyTransformButton)
    self.inputSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onSelect)
    self.outputSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onSelect)

    # Add vertical spacer
    self.layout.addStretch(1)

  def cleanup(self):
    pass

  def onModelSelect(self):
    # Enables load models button when model have been selected
    self.loadModelsButton.enabled = self.skullModelSelector.currentNode() and self.skullMarkersModelSelector.currentNode() and self.pointerModelSelector.currentNode()

  def onLoadModelsButton(self):
    self.loadModelsButton.enabled = False
    self.skullModelSelector.enabled = False
    self.skullMarkersModelSelector.enabled = False
    self.pointerModelSelector.enabled = False
    logic = OptiTrackNavigationLogic()
    logic.loadModels(self.skullModelSelector.currentNode(), self.skullMarkersModelSelector.currentNode(), self.pointerModelSelector.currentNode())

  def onTransformSelect(self):
    # Enables apply transforms button when model have been selected
    self.applyTransformsButton.enabled = self.pointerToTrackerSelector.currentNode() and self.rigidBodyToTrackerSelector.currentNode() and self.trackerToRigidBodySelector.currentNode()

  def onApplyTransformButton(self):
    self.applyTransformsButton.enabled = False
    self.pointerToTrackerSelector.enabled = False
    self.rigidBodyToTrackerSelector.enabled = False
    self.trackerToRigidBodySelector.enabled = False
    logic = OptiTrackNavigationLogic()
    logic.applyTransforms(self.pointerToTrackerSelector.currentNode(), self.rigidBodyToTrackerSelector.currentNode(), self.trackerToRigidBodySelector.currentNode())

  def onSelect(self):
    self.applyButton.enabled = self.inputSelector.currentNode() and self.outputSelector.currentNode()

  def onApplyButton(self):
    logic = OptiTrackNavigationLogic()
    enableScreenshotsFlag = self.enableScreenshotsFlagCheckBox.checked
    screenshotScaleFactor = int(self.screenshotScaleFactorSliderWidget.value)
    print("Run the algorithm")
    logic.run(self.inputSelector.currentNode(), self.outputSelector.currentNode(), enableScreenshotsFlag,screenshotScaleFactor)


#
# OptiTrackNavigationLogic
#

class OptiTrackNavigationLogic(ScriptedLoadableModuleLogic):
  """This class should implement all the actual
  computation done by your module.  The interface
  should be such that other python code can import
  this class and make use of the functionality without
  requiring an instance of the Widget.
  Uses ScriptedLoadableModuleLogic base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """
  def __init__(self):
    self.skullModel=None
    self.skullMarkersModel=None
    self.pointerModel=None
    self.skull = slicer.vtkMRMLModelNode()
    self.skullMarkers = slicer.vtkMRMLModelNode()
    self.pointer = slicer.vtkMRMLModelNode()
    # self.pointerToTrackerTransform=None
    # self.rigidBodyToTrackerTransform=None
    # self.trackerToRigidBodyTransform=None
    self.matrixPointerToTrackerTransform=vtk.vtkMatrix4x4()
    self.matrixRigidBodyToTrackerTransform=vtk.vtkMatrix4x4()
    self.matrixTrackerToRigidBodyTransform=vtk.vtkMatrix4x4()
    
  def loadModels(self, skullModel, skullMarkersModel, pointerModel):
    self.skullModel=skullModel
    self.skullMarkersModel=skullMarkersModel
    self.pointerModel=pointerModel

    self.skull.SetName("SkullModel")
    self.skull.SetAndObservePolyData(self.skullModel.GetPolyData())     
    slicer.mrmlScene.AddNode(self.skull)
    # Add display node
    modelDisplayNode = slicer.vtkMRMLModelDisplayNode()
    modelDisplayNode.SetColor(1,1,1) # White
    modelDisplayNode.BackfaceCullingOff()
    modelDisplayNode.SliceIntersectionVisibilityOn()
    modelDisplayNode.SetSliceIntersectionThickness(4)
    modelDisplayNode.SetOpacity(1) # Between 0-1, 1 being opaque
    slicer.mrmlScene.AddNode(modelDisplayNode)
    self.skull.SetAndObserveDisplayNodeID(modelDisplayNode.GetID())
    
    self.skullMarkers.SetName("SkullMarkersModel")
    self.skullMarkers.SetAndObservePolyData(self.skullMarkersModel.GetPolyData())     
    slicer.mrmlScene.AddNode(self.skullMarkers)
    # Add display node
    modelDisplayNode = slicer.vtkMRMLModelDisplayNode()
    modelDisplayNode.SetColor(1,0,0) # White
    modelDisplayNode.BackfaceCullingOff()
    modelDisplayNode.SliceIntersectionVisibilityOn()
    modelDisplayNode.SetSliceIntersectionThickness(4)
    modelDisplayNode.SetOpacity(1) # Between 0-1, 1 being opaque
    slicer.mrmlScene.AddNode(modelDisplayNode)
    self.skullMarkers.SetAndObserveDisplayNodeID(modelDisplayNode.GetID())

    self.pointer.SetName("PointerModel")
    self.pointer.SetAndObservePolyData(self.pointerModel.GetPolyData())     
    slicer.mrmlScene.AddNode(self.pointer)
    # Add display node
    modelDisplayNode = slicer.vtkMRMLModelDisplayNode()
    modelDisplayNode.SetColor(0,0,0) # White
    modelDisplayNode.BackfaceCullingOff()
    modelDisplayNode.SliceIntersectionVisibilityOn()
    modelDisplayNode.SetSliceIntersectionThickness(4)
    modelDisplayNode.SetOpacity(1) # Between 0-1, 1 being opaque
    slicer.mrmlScene.AddNode(modelDisplayNode)
    self.pointer.SetAndObserveDisplayNodeID(modelDisplayNode.GetID())

  def applyTransforms(self, pointerToTrackerTransform, rigidBodyToTrackerTransform, trackerToRigidBodyTransform):
    slicer.mrmlScene.AddNode(pointerToTrackerTransform)
    slicer.mrmlScene.AddNode(rigidBodyToTrackerTransform)
    slicer.mrmlScene.AddNode(trackerToRigidBodyTransform)

    # # Get vtk matrix from transform:
    # pointerToTrackerTransform.GetMatrixTransformToParent(self.matrixPointerToTrackerTransform)
    # rigidBodyToTrackerTransform.GetMatrixTransformToParent(self.matrixRigidBodyToTrackerTransform)
    # trackerToRigidBodyTransform.GetMatrixTransformToParent(self.matrixTrackerToRigidBodyTransform)

    # self.skull.ApplyTransformMatrix(self.matrixPointerToTrackerTransform)

    # Build transform tree for fiducial registration
    pointerToTrackerTransform.SetAndObserveTransformNodeID(trackerToRigidBodyTransform.GetID())
    self.pointer.SetAndObserveTransformNodeID(pointerToTrackerTransform.GetID())
    # # Build transform tree for navigation
    # self.skullToRigidBodyTransform.SetAndObserveTransformNodeID(self.rigidBodyToTrackerTransform.GetID())
    # self.skull.SetAndObserveTransformNodeID(self.skullToRigidBodyTransform.GetID())
    # self.needleTipToNeedle.SetAndObserveTransformNodeID(self.needleToReference.GetID())
    # self.pointer.SetAndObserveTransformNodeID(self.pointerToTrackerTransform.GetID())
    
  def hasImageData(self,volumeNode):
    """This is a dummy logic method that
    returns true if the passed in volume
    node has valid image data
    """
    if not volumeNode:
      print('no volume node')
      return False
    if volumeNode.GetImageData() == None:
      print('no image data')
      return False
    return True

  def takeScreenshot(self,name,description,type=-1):
    # show the message even if not taking a screen shot
    self.delayDisplay(description)

    if self.enableScreenshots == 0:
      return

    lm = slicer.app.layoutManager()
    # switch on the type to get the requested window
    widget = 0
    if type == slicer.qMRMLScreenShotDialog.FullLayout:
      # full layout
      widget = lm.viewport()
    elif type == slicer.qMRMLScreenShotDialog.ThreeD:
      # just the 3D window
      widget = lm.threeDWidget(0).threeDView()
    elif type == slicer.qMRMLScreenShotDialog.Red:
      # red slice window
      widget = lm.sliceWidget("Red")
    elif type == slicer.qMRMLScreenShotDialog.Yellow:
      # yellow slice window
      widget = lm.sliceWidget("Yellow")
    elif type == slicer.qMRMLScreenShotDialog.Green:
      # green slice window
      widget = lm.sliceWidget("Green")
    else:
      # default to using the full window
      widget = slicer.util.mainWindow()
      # reset the type so that the node is set correctly
      type = slicer.qMRMLScreenShotDialog.FullLayout

    # grab and convert to vtk image data
    qpixMap = qt.QPixmap().grabWidget(widget)
    qimage = qpixMap.toImage()
    imageData = vtk.vtkImageData()
    slicer.qMRMLUtils().qImageToVtkImageData(qimage,imageData)

    annotationLogic = slicer.modules.annotations.logic()
    annotationLogic.CreateSnapShot(name, description, type, self.screenshotScaleFactor, imageData)

  def run(self,inputVolume,outputVolume,enableScreenshots=0,screenshotScaleFactor=1):
    """
    Run the actual algorithm
    """

    self.delayDisplay('Running the aglorithm')

    self.enableScreenshots = enableScreenshots
    self.screenshotScaleFactor = screenshotScaleFactor

    self.takeScreenshot('OptiTrackNavigation-Start','Start',-1)

    return True


class OptiTrackNavigationTest(ScriptedLoadableModuleTest):
  """
  This is the test case for your scripted module.
  Uses ScriptedLoadableModuleTest base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setUp(self):
    """ Do whatever is needed to reset the state - typically a scene clear will be enough.
    """
    slicer.mrmlScene.Clear(0)

  def runTest(self):
    """Run as few or as many tests as needed here.
    """
    self.setUp()
    self.test_OptiTrackNavigation1()

  def test_OptiTrackNavigation1(self):
    """ Ideally you should have several levels of tests.  At the lowest level
    tests sould exercise the functionality of the logic with different inputs
    (both valid and invalid).  At higher levels your tests should emulate the
    way the user would interact with your code and confirm that it still works
    the way you intended.
    One of the most important features of the tests is that it should alert other
    developers when their changes will have an impact on the behavior of your
    module.  For example, if a developer removes a feature that you depend on,
    your test should break so they know that the feature is needed.
    """

    self.delayDisplay("Starting the test")
    #
    # first, get some data
    #
    import urllib
    downloads = (
        ('http://slicer.kitware.com/midas3/download?items=5767', 'FA.nrrd', slicer.util.loadVolume),
        )

    for url,name,loader in downloads:
      filePath = slicer.app.temporaryPath + '/' + name
      if not os.path.exists(filePath) or os.stat(filePath).st_size == 0:
        print('Requesting download %s from %s...\n' % (name, url))
        urllib.urlretrieve(url, filePath)
      if loader:
        print('Loading %s...\n' % (name,))
        loader(filePath)
    self.delayDisplay('Finished with download and loading\n')

    volumeNode = slicer.util.getNode(pattern="FA")
    logic = OptiTrackNavigationLogic()
    self.assertTrue( logic.hasImageData(volumeNode) )
    self.delayDisplay('Test passed!')
