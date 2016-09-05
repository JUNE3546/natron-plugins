# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named VignetteExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from VignetteExt import *
except ImportError:
    pass

def getPluginID():
    return "PostPollux.Vignette"

def getLabel():
    return "Vignette"

def getVersion():
    return 1

def getIconPath():
    return "Vignette.png"

def getGrouping():
    return "Draw"

def getPluginDescription():
    return "This effect adds a vignette to the image. \nA vignette is a reduction of the images brightness at the peripherie compared to the image center."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.controls = lastNode.createPageParam("controls", "Controls")
    param = lastNode.createChoiceParam("Merge1operation", "Operation")
    param.setDefaultValue(26)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Merge1operation = param
    del param

    param = lastNode.createColorParam("Constant1color", "Color", True)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(1, 1)
    param.setDisplayMinimum(0, 2)
    param.setDisplayMaximum(1, 2)
    param.setDisplayMinimum(0, 3)
    param.setDisplayMaximum(1, 3)

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("Color of the vignette.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Constant1color = param
    del param

    param = lastNode.createDoubleParam("softness", "Softness")
    param.setMinimum(0, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("Controles the softness of the vignette.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.softness = param
    del param

    param = lastNode.createDouble2DParam("ScaleTransformscale", "Scale")
    param.setMinimum(0, 0)
    param.setMaximum(10000, 0)
    param.setDisplayMinimum(0.1, 0)
    param.setDisplayMaximum(5, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)
    param.setMinimum(0, 1)
    param.setMaximum(10000, 1)
    param.setDisplayMinimum(0.1, 1)
    param.setDisplayMaximum(5, 1)
    param.setDefaultValue(1, 1)
    param.restoreDefaultValue(1)

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("Scales the vignette.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.ScaleTransformscale = param
    del param

    param = lastNode.createDoubleParam("opacity", "Opacity")
    param.setMinimum(0, 0)
    param.setMaximum(4, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(4, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("Controles the opacity of the vignette.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.opacity = param
    del param

    param = lastNode.createSeparatorParam("separator1", "")

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistant(False)
    param.setEvaluateOnChange(False)
    lastNode.separator1 = param
    del param

    param = lastNode.createBooleanParam("preserveHighlights", "Preserve Highlights")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("When checked, this tries to preserve the highlights, so that you won\'t loose them at the edges. ")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.preserveHighlights = param
    del param

    param = lastNode.createColorParam("Grade1multiply", "Highlight Control", True)
    param.setMinimum(0, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(10, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)
    param.setMinimum(0, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(10, 1)
    param.setDefaultValue(1, 1)
    param.restoreDefaultValue(1)
    param.setMinimum(0, 2)
    param.setDisplayMinimum(0, 2)
    param.setDisplayMaximum(10, 2)
    param.setDefaultValue(1, 2)
    param.restoreDefaultValue(2)
    param.setMinimum(0, 3)
    param.setDisplayMinimum(0, 3)
    param.setDisplayMaximum(10, 3)
    param.setDefaultValue(1, 3)
    param.restoreDefaultValue(3)

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("Finetune the highlight preservation here.\n\n0 -> same as turned of\n4 -> preserve more light areas")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Grade1multiply = param
    del param

    lastNode.userNatron = lastNode.createPageParam("userNatron", "User")
    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['controls', 'Node', 'Settings', 'Info', 'userNatron'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Merge1"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1")
    lastNode.setLabel("Merge1")
    lastNode.setPosition(809, 134)
    lastNode.setSize(104, 74)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("multiply")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("multiply")
        del param

    param = lastNode.getParam("AChannelsA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("mix")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(multiply)</Natron>")
        del param

    param = lastNode.getParam("enableMask_Mask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Merge1"

    # Start of node "Constant"
    lastNode = app.createNode("net.sf.openfx.ConstantPlugin", 1, group)
    lastNode.setScriptName("Constant")
    lastNode.setLabel("Constant")
    lastNode.setPosition(562, 146)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupConstant = lastNode

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video 640x480")
        del param

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Constant"

    # Start of node "Radial"
    lastNode = app.createNode("net.sf.openfx.Radial", 2, group)
    lastNode.setScriptName("Radial")
    lastNode.setLabel("Radial")
    lastNode.setPosition(1789, -428)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupRadial = lastNode

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video 640x480")
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    param = lastNode.getParam("softness")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("color0")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(1, 1)
        param.setValue(1, 2)
        param.setValue(1, 3)
        del param

    param = lastNode.getParam("color1")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        param.setValue(0, 3)
        del param

    param = lastNode.getParam("expandRoD")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Radial"

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setScriptName("Output1")
    lastNode.setLabel("Output1")
    lastNode.setPosition(809, 946)
    lastNode.setSize(104, 31)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Input1"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Input1")
    lastNode.setLabel("Input1")
    lastNode.setPosition(812, -1051)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupInput1 = lastNode

    del lastNode
    # End of node "Input1"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(854, -538)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Dot2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot2")
    lastNode.setLabel("Dot2")
    lastNode.setPosition(607, -538)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot2 = lastNode

    del lastNode
    # End of node "Dot2"

    # Start of node "Mask_Merge"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Mask_Merge")
    lastNode.setLabel("Mask_Merge")
    lastNode.setPosition(1493, 132)
    lastNode.setSize(104, 74)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMask_Merge = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("mask")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("mask")
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(mask)</Natron>")
        del param

    del lastNode
    # End of node "Mask_Merge"

    # Start of node "mask"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("mask")
    lastNode.setLabel("mask")
    lastNode.setPosition(2109, 147)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupmask = lastNode

    param = lastNode.getParam("optional")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("isMask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "mask"

    # Start of node "BlackAlpha"
    lastNode = app.createNode("net.sf.openfx.ConstantPlugin", 1, group)
    lastNode.setScriptName("BlackAlpha")
    lastNode.setLabel("BlackAlpha")
    lastNode.setPosition(1494, -637)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupBlackAlpha = lastNode

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video 640x480")
        del param

    del lastNode
    # End of node "BlackAlpha"

    # Start of node "ZeroToAlpha"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("ZeroToAlpha")
    lastNode.setLabel("ZeroToAlpha")
    lastNode.setPosition(1494, -564)
    lastNode.setSize(104, 74)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupZeroToAlpha = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("copy")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("copy")
        del param

    param = lastNode.getParam("AChannelsA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("BChannelsR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("BChannelsG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("BChannelsB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(copy)</Natron>")
        del param

    del lastNode
    # End of node "ZeroToAlpha"

    # Start of node "Dot3"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot3")
    lastNode.setLabel("Dot3")
    lastNode.setPosition(857, -623)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot3 = lastNode

    del lastNode
    # End of node "Dot3"

    # Start of node "Highlights_Merge"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Highlights_Merge")
    lastNode.setLabel("Highlights_Merge")
    lastNode.setPosition(1492, -82)
    lastNode.setSize(104, 74)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupHighlights_Merge = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("mask")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("mask")
        del param

    param = lastNode.getParam("mix")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(mask)</Natron>")
        del param

    del lastNode
    # End of node "Highlights_Merge"

    # Start of node "Saturation1"
    lastNode = app.createNode("net.sf.openfx.SaturationPlugin", 2, group)
    lastNode.setScriptName("Saturation1")
    lastNode.setLabel("Saturation1")
    lastNode.setPosition(1283, -424)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupSaturation1 = lastNode

    param = lastNode.getParam("saturation")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Saturation1"

    # Start of node "RedToAlpha"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("RedToAlpha")
    lastNode.setLabel("RedToAlpha")
    lastNode.setPosition(1283, -186)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupRedToAlpha = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGBA")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputG")
    if param is not None:
        param.set("A.r")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputB")
    if param is not None:
        param.set("A.r")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("A.r")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    del lastNode
    # End of node "RedToAlpha"

    # Start of node "Invert"
    lastNode = app.createNode("net.sf.openfx.Invert", 2, group)
    lastNode.setScriptName("Invert")
    lastNode.setLabel("Invert")
    lastNode.setPosition(1284, -70)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupInvert = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Invert"

    # Start of node "Grade"
    lastNode = app.createNode("net.sf.openfx.GradePlugin", 2, group)
    lastNode.setScriptName("Grade")
    lastNode.setLabel("Grade")
    lastNode.setPosition(1283, -307)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupGrade = lastNode

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("multiply")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(1, 1)
        param.setValue(1, 2)
        param.setValue(1, 3)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Grade"

    # Start of node "Clamp"
    lastNode = app.createNode("net.sf.openfx.Clamp", 2, group)
    lastNode.setScriptName("Clamp")
    lastNode.setLabel("Clamp")
    lastNode.setPosition(1493, 56)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupClamp = lastNode

    param = lastNode.getParam("premult")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Clamp"

    # Start of node "Merge1_2"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1_2")
    lastNode.setLabel("Merge1_2")
    lastNode.setPosition(809, 272)
    lastNode.setSize(104, 74)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1_2 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("multiply")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("multiply")
        del param

    param = lastNode.getParam("AChannelsA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("mix")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(multiply)</Natron>")
        del param

    param = lastNode.getParam("enableMask_Mask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Merge1_2"

    # Start of node "Merge1_3"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1_3")
    lastNode.setLabel("Merge1_3")
    lastNode.setPosition(809, 404)
    lastNode.setSize(104, 74)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1_3 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("multiply")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("multiply")
        del param

    param = lastNode.getParam("AChannelsA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("mix")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(multiply)</Natron>")
        del param

    param = lastNode.getParam("enableMask_Mask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Merge1_3"

    # Start of node "Dot5"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot5")
    lastNode.setLabel("Dot5")
    lastNode.setPosition(1052, 159)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot5 = lastNode

    del lastNode
    # End of node "Dot5"

    # Start of node "Dot6"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot6")
    lastNode.setLabel("Dot6")
    lastNode.setPosition(1052, 296)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot6 = lastNode

    del lastNode
    # End of node "Dot6"

    # Start of node "Dot7"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot7")
    lastNode.setLabel("Dot7")
    lastNode.setPosition(1055, 429)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot7 = lastNode

    del lastNode
    # End of node "Dot7"

    # Start of node "Dot8"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot8")
    lastNode.setLabel("Dot8")
    lastNode.setPosition(698, 160)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot8 = lastNode

    del lastNode
    # End of node "Dot8"

    # Start of node "Dot9"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot9")
    lastNode.setLabel("Dot9")
    lastNode.setPosition(698, 298)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot9 = lastNode

    del lastNode
    # End of node "Dot9"

    # Start of node "Dot10"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot10")
    lastNode.setLabel("Dot10")
    lastNode.setPosition(698, 430)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot10 = lastNode

    del lastNode
    # End of node "Dot10"

    # Start of node "Vignette_Mask"
    lastNode = app.createNode("fr.inria.built-in.BackDrop", 1, group)
    lastNode.setScriptName("Vignette_Mask")
    lastNode.setLabel("Vignette_Mask")
    lastNode.setPosition(1145, -808)
    lastNode.setSize(846, 1088)
    lastNode.setColor(0.45, 0.45, 0.45)
    groupVignette_Mask = lastNode

    param = lastNode.getParam("Label")
    if param is not None:
        param.setValue("<font size=\"12\" color=\"#000000\" face=\"Droid Sans\">Vignette Mask Creation</font>")
        del param

    del lastNode
    # End of node "Vignette_Mask"

    # Start of node "Merge1_4"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1_4")
    lastNode.setLabel("Merge1_4")
    lastNode.setPosition(809, 563)
    lastNode.setSize(104, 74)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1_4 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("multiply")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("multiply")
        del param

    param = lastNode.getParam("AChannelsA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("mix")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(multiply)</Natron>")
        del param

    param = lastNode.getParam("enableMask_Mask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Merge1_4"

    # Start of node "Dot7_2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot7_2")
    lastNode.setLabel("Dot7_2")
    lastNode.setPosition(1055, 589)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot7_2 = lastNode

    del lastNode
    # End of node "Dot7_2"

    # Start of node "Dot10_2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot10_2")
    lastNode.setLabel("Dot10_2")
    lastNode.setPosition(698, 589)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot10_2 = lastNode

    del lastNode
    # End of node "Dot10_2"

    # Start of node "Shuffle1_2"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle1_2")
    lastNode.setLabel("Shuffle1_2")
    lastNode.setPosition(1492, -326)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle1_2 = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGBA")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("A.g")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("A.b")
        del param

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("1")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("1")
        del param

    del lastNode
    # End of node "Shuffle1_2"

    # Start of node "Merge2"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge2")
    lastNode.setLabel("Merge2")
    lastNode.setPosition(1492, -217)
    lastNode.setSize(104, 74)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge2 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("copy")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("copy")
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(copy)</Natron>")
        del param

    param = lastNode.getParam("enableMask_Mask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Merge2"

    # Start of node "Shuffle1"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle1")
    lastNode.setLabel("Shuffle1")
    lastNode.setPosition(1790, -205)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle1 = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGBA")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("A.g")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("A.b")
        del param

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("1")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("1")
        del param

    del lastNode
    # End of node "Shuffle1"

    # Start of node "Dot11"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot11")
    lastNode.setLabel("Dot11")
    lastNode.setPosition(1537, -410)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot11 = lastNode

    del lastNode
    # End of node "Dot11"

    # Start of node "SoftnessTransform"
    lastNode = app.createNode("net.sf.openfx.TransformPlugin", 1, group)
    lastNode.setScriptName("SoftnessTransform")
    lastNode.setLabel("SoftnessTransform")
    lastNode.setPosition(1786, -355)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupSoftnessTransform = lastNode

    param = lastNode.getParam("scale")
    if param is not None:
        param.setValue(2, 0)
        param.setValue(2, 1)
        del param

    param = lastNode.getParam("center")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    param = lastNode.getParam("black_outside")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "SoftnessTransform"

    # Start of node "ScaleTransform"
    lastNode = app.createNode("net.sf.openfx.TransformPlugin", 1, group)
    lastNode.setScriptName("ScaleTransform")
    lastNode.setLabel("ScaleTransform")
    lastNode.setPosition(1786, -273)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupScaleTransform = lastNode

    param = lastNode.getParam("scale")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(1, 1)
        del param

    param = lastNode.getParam("center")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    param = lastNode.getParam("black_outside")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "ScaleTransform"

    # Start of node "preserve_Highlights"
    lastNode = app.createNode("fr.inria.built-in.BackDrop", 1, group)
    lastNode.setScriptName("preserve_Highlights")
    lastNode.setLabel("preserve Highlights")
    lastNode.setPosition(1223, -519)
    lastNode.setSize(240, 537)
    lastNode.setColor(0.7804, 0.7804, 0.7804)
    grouppreserve_Highlights = lastNode

    del lastNode
    # End of node "preserve_Highlights"

    # Now that all nodes are created we can connect them together, restore expressions
    groupMerge1.connectInput(0, groupDot1)
    groupMerge1.connectInput(1, groupDot8)
    groupMerge1.connectInput(2, groupDot5)
    groupConstant.connectInput(0, groupDot2)
    groupRadial.connectInput(0, groupDot11)
    groupOutput1.connectInput(0, groupMerge1_4)
    groupDot1.connectInput(0, groupDot3)
    groupDot2.connectInput(0, groupDot1)
    groupMask_Merge.connectInput(0, groupClamp)
    groupMask_Merge.connectInput(1, groupmask)
    groupBlackAlpha.connectInput(0, groupDot3)
    groupZeroToAlpha.connectInput(0, groupBlackAlpha)
    groupZeroToAlpha.connectInput(1, groupDot1)
    groupDot3.connectInput(0, groupInput1)
    groupHighlights_Merge.connectInput(0, groupMerge2)
    groupHighlights_Merge.connectInput(1, groupInvert)
    groupSaturation1.connectInput(0, groupDot11)
    groupRedToAlpha.connectInput(1, groupGrade)
    groupInvert.connectInput(0, groupRedToAlpha)
    groupGrade.connectInput(0, groupSaturation1)
    groupClamp.connectInput(0, groupHighlights_Merge)
    groupMerge1_2.connectInput(0, groupMerge1)
    groupMerge1_2.connectInput(1, groupDot9)
    groupMerge1_2.connectInput(2, groupDot6)
    groupMerge1_3.connectInput(0, groupMerge1_2)
    groupMerge1_3.connectInput(1, groupDot10)
    groupMerge1_3.connectInput(2, groupDot7)
    groupDot5.connectInput(0, groupMask_Merge)
    groupDot6.connectInput(0, groupDot5)
    groupDot7.connectInput(0, groupDot6)
    groupDot8.connectInput(0, groupConstant)
    groupDot9.connectInput(0, groupDot8)
    groupDot10.connectInput(0, groupDot9)
    groupMerge1_4.connectInput(0, groupMerge1_3)
    groupMerge1_4.connectInput(1, groupDot10_2)
    groupMerge1_4.connectInput(2, groupDot7_2)
    groupDot7_2.connectInput(0, groupDot7)
    groupDot10_2.connectInput(0, groupDot10)
    groupShuffle1_2.connectInput(1, groupDot11)
    groupMerge2.connectInput(0, groupShuffle1_2)
    groupMerge2.connectInput(1, groupScaleTransform)
    groupMerge2.connectInput(2, groupShuffle1)
    groupShuffle1.connectInput(1, groupScaleTransform)
    groupDot11.connectInput(0, groupZeroToAlpha)
    groupSoftnessTransform.connectInput(0, groupRadial)
    groupScaleTransform.connectInput(0, groupSoftnessTransform)

    param = groupMerge1.getParam("operation")
    group.getParam("Merge1operation").setAsAlias(param)
    del param
    param = groupMerge1.getParam("mix")
    param.setExpression("opacity = thisGroup.opacity.get()\nif opacity > 0:\n\tret = (opacity % 1)\n\tif opacity >=1:\n\t\tret = 1\nelse:\n\tret =0 ", True, 0)
    del param
    param = groupConstant.getParam("color")
    group.getParam("Constant1color").setAsAlias(param)
    del param
    param = groupRadial.getParam("size")
    param.setExpression("rod = ZeroToAlpha.getRegionOfDefinition(frame, 0)\nret = rod.width()", True, 0)
    param.setExpression("rod = ZeroToAlpha.getRegionOfDefinition(frame, 0)\nret = rod.height()", True, 1)
    del param
    param = groupRadial.getParam("softness")
    param.setExpression("thisGroup.softness.get()", False, 0)
    del param
    param = groupHighlights_Merge.getParam("mix")
    param.setExpression("thisGroup.preserveHighlights.get()", False, 0)
    del param
    param = groupGrade.getParam("multiply")
    group.getParam("Grade1multiply").setAsAlias(param)
    del param
    param = groupMerge1_2.getParam("operation")
    group.getParam("Merge1operation").setAsAlias(param)
    del param
    param = groupMerge1_2.getParam("mix")
    param.setExpression("opacity = thisGroup.opacity.get()\nif opacity > 1:\n\tret = (opacity % 1)\n\tif opacity >=2:\n\t\tret = 1\nelse:\n\tret =0 \n", True, 0)
    del param
    param = groupMerge1_3.getParam("operation")
    group.getParam("Merge1operation").setAsAlias(param)
    del param
    param = groupMerge1_3.getParam("mix")
    param.setExpression("opacity = thisGroup.opacity.get()\nif opacity > 2:\n\tret = (opacity % 1)\n\tif opacity >=3:\n\t\tret = 1\nelse:\n\tret =0 ", True, 0)
    del param
    param = groupMerge1_4.getParam("operation")
    group.getParam("Merge1operation").setAsAlias(param)
    del param
    param = groupMerge1_4.getParam("mix")
    param.setExpression("opacity = thisGroup.opacity.get()\nif opacity > 3:\n\tret = (opacity % 1)\n\tif opacity >=4:\n\t\tret = 1\nelse:\n\tret =0 ", True, 0)
    del param
    param = groupSoftnessTransform.getParam("scale")
    param.setExpression("1+thisGroup.softness.get()", False, 0)
    param.setExpression("1+thisGroup.softness.get()", False, 1)
    del param
    param = groupSoftnessTransform.getParam("center")
    param.setExpression("rod = ZeroToAlpha.getRegionOfDefinition(frame, 0)\nret = rod.width()/2", True, 0)
    param.setExpression("rod = ZeroToAlpha.getRegionOfDefinition(frame, 0)\nret = rod.height()/2", True, 1)
    del param
    param = groupScaleTransform.getParam("scale")
    group.getParam("ScaleTransformscale").setAsAlias(param)
    del param
    param = groupScaleTransform.getParam("center")
    param.setExpression("thisGroup.SoftnessTransform.center.get()[0]", False, 0)
    param.setExpression("thisGroup.SoftnessTransform.center.get()[1]", False, 1)
    del param

    try:
        extModule = sys.modules["VignetteExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
