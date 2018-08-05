# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Ls_Dollface_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Ls_Dollface_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Ls_Dollface_GL"

def getLabel():
    return "Ls_Dollface_GL"

def getVersion():
    return 1

def getIconPath():
    return "Ls_Dollface_GL.png"

def getGrouping():
    return "Community/GLSL/Effect"

def getPluginDescription():
    return "Blend similar colours with a bilateral filter whilst preserving edges, to remove grain or wrinkles."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(1, 0.2353, 0.2353)

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createSeparatorParam("SETUP", "Setup")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.SETUP = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy_pass1paramValueFloat0", "Sigma : ")
    param.setMinimum(0, 0)
    param.setMaximum(100, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(40, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Amount of softening in similar areas.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy_pass1paramValueFloat0 = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy_pass1paramValueFloat1", "Threshold : ")
    param.setMinimum(0.001, 0)
    param.setMaximum(100, 0)
    param.setDisplayMinimum(0.001, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(40, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Increase to keep more edges - if this is quite high you may want to blur the result a little because edges can get very hard.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy_pass1paramValueFloat1 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createIntParam("Shadertoy_pass1paramValueInt2", "Quality : ")
    param.setMinimum(0, 0)
    param.setMaximum(3, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(3, 0)
    param.setDefaultValue(3, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Increase to remove artifacts.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy_pass1paramValueInt2 = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createSeparatorParam("LINE01", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LINE01 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy_pass1paramValueBool3", "Precise blending : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Use very slow but accurate algorithm.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy_pass1paramValueBool3 = param
    del param

    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep09 = param
    del param

    param = lastNode.createStringParam("sep10", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep10 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep101", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep101 = param
    del param

    param = lastNode.createStringParam("sep102", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep102 = param
    del param

    param = lastNode.createSeparatorParam("NAME", "Ls_Dollface_GL v1.0")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.NAME = param
    del param

    param = lastNode.createStringParam("sep103", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep103 = param
    del param

    param = lastNode.createStringParam("sep104", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep104 = param
    del param

    param = lastNode.createSeparatorParam("LINE101", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LINE101 = param
    del param

    param = lastNode.createStringParam("sep105", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep105 = param
    del param

    param = lastNode.createStringParam("sep106", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep106 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("sep107", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep107 = param
    del param

    param = lastNode.createStringParam("sep108", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep108 = param
    del param

    param = lastNode.createSeparatorParam("CONVERSION", " (Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CONVERSION = param
    del param

    param = lastNode.createStringParam("sep109", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep109 = param
    del param

    param = lastNode.createStringParam("sep110", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep110 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4138, 4454)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(4139, 3683)
    lastNode.setSize(80, 36)
    lastNode.setColor(1, 1, 1)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Strength_map"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Strength_map")
    lastNode.setLabel("Strength_map")
    lastNode.setPosition(4329, 3972)
    lastNode.setSize(80, 36)
    lastNode.setColor(1, 1, 1)
    groupStrength_map = lastNode

    del lastNode
    # End of node "Strength_map"

    # Start of node "Shadertoy_pass1"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy_pass1")
    lastNode.setLabel("Shadertoy_pass1")
    lastNode.setPosition(4137, 3976)
    lastNode.setSize(80, 55)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy_pass1 = lastNode

    param = lastNode.getParam("paramValueFloat0")
    if param is not None:
        param.setValue(40, 0)
        del param

    param = lastNode.getParam("paramValueFloat1")
    if param is not None:
        param.setValue(40, 0)
        del param

    param = lastNode.getParam("paramValueInt2")
    if param is not None:
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("paramValueBool3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramValueInt3")
    if param is not None:
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("//\n//\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//                        MM.                          .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\n//                   MM.  .MmM              MMMM      MMM.  .MM\n//                  MM.  .MMM                 MM       MMM.  .MM\n//                 MM.  .MMM                   M        MMM.  .MM\n//                MM.  .MMM                              MMM.  .MM\n//                 MM.  .MMM                            MMM.  .MM\n//                  MM.  .MMM       M                  MMM.  .MM\n//                   MM.  .MMM      MM                MMM.  .MM\n//                    MM.  .MMM     MMM              MMM.  .MM\n//                     MM.  .MMM    MMMM            MMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                        MM.                          .MM\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//\n//\n//\n//\n// Adaptation pour Natron par F. Fernandez\n// Code original : Ls_Dollface Matchbox pour Autodesk Flame\n\n// Adapted to Natron by F.Fernandez\n// Original code : LS_Dollface Matchbox for Autodesk Flame\n\n\n// iChannel0: Source, filter = nearest\n// iChannel1: Strength map, filter = nearest\n// BBox: iChannel0\n\n\n\n\n// Blur only similar pixels\n// Pass 2: horizontal blur\n// lewis@lewissaunders.com\n\n\n\n\n\nuniform float sigma = 40.0; // Sigma : (sigma), min=0, max=100\nuniform float threshold = 40.0; // Threshold : (threshold), min=0.001, max=100\nuniform int quality = 3; // Quality : (quality), min=0, max=3\n\nuniform bool slow = false;\n\n\n\n\n\n\nconst float pi = 3.141592653589793238462643383279502884197969;\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\tvec2 xy = fragCoord.xy;\n\tvec2 px = vec2(1.0) / vec2(iResolution.x, iResolution.y);\n\n\tfloat strength_here = texture2D(iChannel1, xy * px).b;\n\tfloat sigma_here = sigma * strength_here;\n\n\tint support = int(sigma_here * 3.0);\n\n\tfloat kernelhyp = length(vec2(support, support));\n\tfloat rgbhyp = length(vec3(1.0, 1.0, 1.0));\n\n\tif(slow) {\n\t\t// Use straightforward but slow algorithm\n\t\tvec4 centre = texture2D(iChannel0, xy * px);\n\n\t\tvec4 a = vec4(0.0);\n\t\tfloat energy = 0.0;\n\n\t\tfloat inc = pow(2.0, 3.0 - float(quality));\n\n\t\t// Factor to make apparant sharpness of two algorithms similar\n\t\tfloat m = 1.666;\n\n\t\t// Yes, this is brute force and dirty\n\t\t// Making bilateral filtering separable is really hard\n\t\t// c.f. any number of SIGGRAPH papers\n\t\tfor(float x = -sigma_here * m; x <= sigma_here * m; x += inc) {\n\t\t\tfor(float y = -sigma_here * m; y <= sigma_here * m; y += inc) {\n\t\t\t\tvec4 b = texture2D(iChannel0, (xy + vec2(x, y)) * px);\n\t\t\t\tb.a = 1.0;\n\n\t\t\t\t// Mult this sample by colour similarity\n\t\t\t\tfloat fac = 1.0 - (length(b - centre) / rgbhyp);\n\t\t\t\tfac = pow(fac, threshold);\n\t\t\t\tb *= clamp(fac, 0.001, 1.0);\n\n\t\t\t\t// Mult this sample by distance from centre, i.e. triangular kernel\n\t\t\t\tb *= kernelhyp - length(vec2(x, y));\n\n\t\t\t\t// Accumulate\n\t\t\t\ta += b;\n\t\t\t\tenergy += b.a;\n\t\t\t}\n\t\t}\n\n\t\tif(energy < 0.05) {\n\t\t\t// No samples were taken!\n\t\t\tfragColor = texture2D(iChannel0, xy * px);\n\t\t\treturn;\n\t\t}\n\n\t\ta /= energy;\n\t\tfragColor = a;\n\t\treturn;\n\t}\n\n\t// Okay.  On to complicated two-pass algorithm\n\t// Incremental coefficient calculation setup as per GPU Gems 3\n\tvec3 g;\n\tg.x = 1.0 / (sqrt(2.0 * pi) * sigma_here);\n\tg.y = exp(-0.5 / (sigma_here * sigma_here));\n\tg.z = g.y * g.y;\n\n\tif(sigma_here == 0.0) {\n\t\tg.x = 1.0;\n\t}\n\n\tvec4 a, b, c;\n\ta = vec4(0.0);\n\tfloat fac, energy = 0.0;\n\n\t// Centre sample\n\tvec4 orig = texture2D(iChannel0, xy * px);\n\ta += g.x * orig;\n\tenergy += g.x;\n\tg.xy *= g.yz;\n\n\tint inc = int(pow(2.0, 3.0 - float(quality)));\n\n\t// The rest\n\tfor(int i = 1; i <= support; i += inc) {\n\t\tb = texture2D(iChannel0, (xy - vec2(float(i), 0.0)) * px);\n\t\tc = texture2D(iChannel0, (xy + vec2(float(i), 0.0)) * px);\n\n\t\tb.a = 1.0;\n\t\tc.a = 1.0;\n\n\t\tfac = 1.0 - (length(b - orig) / rgbhyp);\n\t\tfac = pow(fac, threshold);\n\t\tb *= g.x * clamp(fac, 0.001, 1.0);\n\t\ta += b;\n\t\tenergy += b.a;\n\n\t\tfac = 1.0 - (length(c - orig) / rgbhyp);\n\t\tfac = pow(fac, threshold);\n\t\tc *= g.x * clamp(fac, 0.001, 1.0);\n\t\ta += c;\n\t\tenergy += c.a;\n\n\t\tg.xy *= g.yz;\n\t}\n\ta /= energy;\n\n\tfragColor = a;\n}\n")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("nearest")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("Source")
        del param

    param = lastNode.getParam("mipmap1")
    if param is not None:
        param.set("nearest")
        del param

    param = lastNode.getParam("inputLabel1")
    if param is not None:
        param.setValue("Strength map")
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(4, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("sigma")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Sigma :")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("sigma")
        del param

    param = lastNode.getParam("paramDefaultFloat0")
    if param is not None:
        param.setValue(40, 0)
        del param

    param = lastNode.getParam("paramMinFloat0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat0")
    if param is not None:
        param.setValue(99.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("threshold")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Threshold :")
        del param

    param = lastNode.getParam("paramHint1")
    if param is not None:
        param.setValue("threshold")
        del param

    param = lastNode.getParam("paramDefaultFloat1")
    if param is not None:
        param.setValue(40, 0)
        del param

    param = lastNode.getParam("paramMinFloat1")
    if param is not None:
        param.setValue(0.001, 0)
        del param

    param = lastNode.getParam("paramMaxFloat1")
    if param is not None:
        param.setValue(99.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("quality")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Quality :")
        del param

    param = lastNode.getParam("paramHint2")
    if param is not None:
        param.setValue("quality")
        del param

    param = lastNode.getParam("paramDefaultInt2")
    if param is not None:
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("paramMinInt2")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxInt2")
    if param is not None:
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("slow")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("slow")
        del param

    del lastNode
    # End of node "Shadertoy_pass1"

    # Start of node "Shadertoy_pass2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy_pass2")
    lastNode.setLabel("Shadertoy_pass2")
    lastNode.setPosition(4137, 4149)
    lastNode.setSize(80, 55)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy_pass2 = lastNode

    param = lastNode.getParam("paramValueFloat0")
    if param is not None:
        param.setValue(40, 0)
        del param

    param = lastNode.getParam("paramValueFloat1")
    if param is not None:
        param.setValue(40, 0)
        del param

    param = lastNode.getParam("paramValueInt2")
    if param is not None:
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("paramValueInt3")
    if param is not None:
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("//\n//\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//                        MM.                          .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\n//                   MM.  .MmM              MMMM      MMM.  .MM\n//                  MM.  .MMM                 MM       MMM.  .MM\n//                 MM.  .MMM                   M        MMM.  .MM\n//                MM.  .MMM                              MMM.  .MM\n//                 MM.  .MMM                            MMM.  .MM\n//                  MM.  .MMM       M                  MMM.  .MM\n//                   MM.  .MMM      MM                MMM.  .MM\n//                    MM.  .MMM     MMM              MMM.  .MM\n//                     MM.  .MMM    MMMM            MMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                        MM.                          .MM\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//\n//\n//\n//\n// Adaptation pour Natron par F. Fernandez\n// Code original : Ls_Dollface Matchbox pour Autodesk Flame\n\n// Adapted to Natron by F.Fernandez\n// Original code : LS_Dollface Matchbox for Autodesk Flame\n\n\n// iChannel0: Source, filter = nearest\n// iChannel1: Strength map, filter = nearest\n// BBox: iChannel0\n\n\n\n\n// Blur only similar pixels\n// Pass 2: horizontal blur\n// lewis@lewissaunders.com\n\n\n\n\n\nuniform float sigma = 40.0; // Sigma : (sigma), min=0, max=100\nuniform float threshold = 40.0; // Threshold : (threshold), min=0.001, max=100\nuniform int quality = 3; // Quality : (quality), min=0, max=3\n\nuniform bool slow = false;\n\n\n\n\n\n\nconst float pi = 3.141592653589793238462643383279502884197969;\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\tvec2 xy = fragCoord.xy;\n\tvec2 px = vec2(1.0) / vec2(iResolution.x, iResolution.y);\n\n\tfloat strength_here = texture2D(iChannel1, xy * px).b;\n\tfloat sigma_here = sigma * strength_here;\n\n\tint support = int(sigma_here * 3.0);\n\n\tfloat kernelhyp = length(vec2(support, support));\n\tfloat rgbhyp = length(vec3(1.0, 1.0, 1.0));\n\n\tif(slow) {\n\t\t// Use pass 1 results and quit\n\t\tfragColor = texture2D(iChannel0, xy * px);\n\t\treturn;\n\t}\n\n\t// Incremental coefficient calculation setup as per GPU Gems 3\n\tvec3 g;\n\tg.x = 1.0 / (sqrt(2.0 * pi) * sigma_here);\n\tg.y = exp(-0.5 / (sigma_here * sigma_here));\n\tg.z = g.y * g.y;\n\n\tif(sigma_here == 0.0) {\n\t\tg.x = 1.0;\n\t}\n\n\tvec4 a, b, c;\n\ta = vec4(0.0);\n\tfloat fac, energy = 0.0;\n\n\t// Centre sample\n\tvec4 orig = texture2D(iChannel0, xy * px);\n\ta += g.x * orig;\n\tenergy += g.x;\n\tg.xy *= g.yz;\n\n\tint inc = int(pow(2.0, 3.0 - float(quality)));\n\n\t// The rest\n\tfor(int i = 1; i <= support; i += inc) {\n\t\tb = texture2D(iChannel0, (xy - vec2(0.0, float(i))) * px);\n\t\tc = texture2D(iChannel0, (xy + vec2(0.0, float(i))) * px);\n\n\t\tb.a = 1.0;\n\t\tc.a = 1.0;\n\n\t\tfac = 1.0 - (length(b - orig) / rgbhyp);\n\t\tfac = pow(fac, threshold);\n\t\tb *= g.x * clamp(fac, 0.001, 1.0);\n\t\ta += b;\n\t\tenergy += b.a;\n\n\t\tfac = 1.0 - (length(c - orig) / rgbhyp);\n\t\tfac = pow(fac, threshold);\n\t\tc *= g.x * clamp(fac, 0.001, 1.0);\n\t\ta += c;\n\t\tenergy += c.a;\n\n\t\tg.xy *= g.yz;\n\t}\n\ta /= energy;\n\n\tfragColor = a;\n}\n")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("nearest")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("Source")
        del param

    param = lastNode.getParam("mipmap1")
    if param is not None:
        param.set("nearest")
        del param

    param = lastNode.getParam("inputLabel1")
    if param is not None:
        param.setValue("Strength map")
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(4, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("sigma")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Sigma :")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("sigma")
        del param

    param = lastNode.getParam("paramDefaultFloat0")
    if param is not None:
        param.setValue(40, 0)
        del param

    param = lastNode.getParam("paramMinFloat0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat0")
    if param is not None:
        param.setValue(99.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("threshold")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Threshold :")
        del param

    param = lastNode.getParam("paramHint1")
    if param is not None:
        param.setValue("threshold")
        del param

    param = lastNode.getParam("paramDefaultFloat1")
    if param is not None:
        param.setValue(40, 0)
        del param

    param = lastNode.getParam("paramMinFloat1")
    if param is not None:
        param.setValue(0.001, 0)
        del param

    param = lastNode.getParam("paramMaxFloat1")
    if param is not None:
        param.setValue(99.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("quality")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Quality :")
        del param

    param = lastNode.getParam("paramHint2")
    if param is not None:
        param.setValue("quality")
        del param

    param = lastNode.getParam("paramDefaultInt2")
    if param is not None:
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("paramMinInt2")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxInt2")
    if param is not None:
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("slow")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("slow")
        del param

    del lastNode
    # End of node "Shadertoy_pass2"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(4037, 4084)
    lastNode.setSize(16, 16)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Crop_Source"
    lastNode = app.createNode("net.sf.openfx.CropPlugin", 1, group)
    lastNode.setScriptName("Crop_Source")
    lastNode.setLabel("Crop_Source")
    lastNode.setPosition(4134, 3798)
    lastNode.setSize(90, 36)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupCrop_Source = lastNode

    param = lastNode.getParam("rectangleInteractEnable")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(1920, 0)
        param.setValue(1080, 1)
        del param

    param = lastNode.getParam("reformat")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Crop_Source"

    # Start of node "Crop_Strength"
    lastNode = app.createNode("net.sf.openfx.CropPlugin", 1, group)
    lastNode.setScriptName("Crop_Strength")
    lastNode.setLabel("Crop_Strength")
    lastNode.setPosition(4324, 4054)
    lastNode.setSize(90, 36)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupCrop_Strength = lastNode

    param = lastNode.getParam("rectangleInteractEnable")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(1920, 0)
        param.setValue(1080, 1)
        del param

    param = lastNode.getParam("reformat")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Crop_Strength"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupShadertoy_pass2)
    groupShadertoy_pass1.connectInput(0, groupCrop_Source)
    groupShadertoy_pass1.connectInput(1, groupCrop_Strength)
    groupShadertoy_pass2.connectInput(0, groupDot1)
    groupShadertoy_pass2.connectInput(1, groupCrop_Strength)
    groupDot1.connectInput(0, groupShadertoy_pass1)
    groupCrop_Source.connectInput(0, groupSource)
    groupCrop_Strength.connectInput(0, groupStrength_map)

    param = groupShadertoy_pass1.getParam("paramValueFloat0")
    group.getParam("Shadertoy_pass1paramValueFloat0").setAsAlias(param)
    del param
    param = groupShadertoy_pass1.getParam("paramValueFloat1")
    group.getParam("Shadertoy_pass1paramValueFloat1").setAsAlias(param)
    del param
    param = groupShadertoy_pass1.getParam("paramValueInt2")
    group.getParam("Shadertoy_pass1paramValueInt2").setAsAlias(param)
    del param
    param = groupShadertoy_pass1.getParam("paramValueBool3")
    group.getParam("Shadertoy_pass1paramValueBool3").setAsAlias(param)
    del param
    param = groupShadertoy_pass2.getParam("paramValueFloat0")
    param.slaveTo(groupShadertoy_pass1.getParam("paramValueFloat0"), 0, 0)
    del param
    param = groupShadertoy_pass2.getParam("paramValueFloat1")
    param.slaveTo(groupShadertoy_pass1.getParam("paramValueFloat1"), 0, 0)
    del param
    param = groupShadertoy_pass2.getParam("paramValueInt2")
    param.slaveTo(groupShadertoy_pass1.getParam("paramValueInt2"), 0, 0)
    del param
    param = groupCrop_Source.getParam("size")
    param.setExpression("myWidth = Source.getOutputFormat().width()\nret = myWidth", True, 0)
    param.setExpression("myWidth = Source.getOutputFormat().height()\nret = myWidth", True, 1)
    del param
    param = groupCrop_Strength.getParam("size")
    param.setExpression("myWidth = Strength_map.getOutputFormat().width()\nret = myWidth", True, 0)
    param.setExpression("myWidth = Strength_map.getOutputFormat().height()\nret = myWidth", True, 1)
    del param

    try:
        extModule = sys.modules["Ls_Dollface_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
