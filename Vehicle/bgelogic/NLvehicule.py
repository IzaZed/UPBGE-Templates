#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.SetDictKeyValue()
    ACT0001 = bgelogic.SetDictKeyValue()
    ACT0002 = bgelogic.SetDictKeyValue()
    ACT0003 = bgelogic.SetDictKeyValue()
    ACT0004 = bgelogic.SetDictKeyValue()
    PAR0005 = bgelogic.ParameterObjectAttribute()
    CON0006 = bgelogic.ConditionOnUpdate()
    ACT0007 = bgelogic.ActionSetGameObjectGameProperty()
    PAR0008 = bgelogic.ParameterObjectProperty()
    ACT0009 = bgelogic.SetDictKeyValue()
    ACT0010 = bgelogic.SetDictKeyValue()
    ACT0011 = bgelogic.SetDictKeyValue()
    CON0012 = bgelogic.ConditionLogicOp()
    PAR0013 = bgelogic.ValueSwitch()
    CON0014 = bgelogic.ConditionKeyPressed()
    PAR0015 = bgelogic.ConditionGamepadTrigger()
    CON0016 = bgelogic.ConditionLogicOp()
    CON0017 = bgelogic.ConditionKeyPressed()
    PAR0018 = bgelogic.ConditionGamepadTrigger()
    PAR0019 = bgelogic.ValueSwitch()
    CON0020 = bgelogic.ConditionLogicOp()
    PAR0021 = bgelogic.ValueSwitch()
    PAR0022 = bgelogic.ValueSwitch()
    CON0023 = bgelogic.ConditionLogicOp()
    ACT0024 = bgelogic.InvertValue()
    PAR0025 = bgelogic.ConditionGamepadSticks()
    ACT0026 = bgelogic.ParameterPythonModuleFunction()
    PAR0027 = bgelogic.ParameterFindChildByName()
    PAR0028 = bgelogic.ParameterFindChildByName()
    PAR0029 = bgelogic.ParameterFindChildByName()
    PAR0030 = bgelogic.ParameterFindChildByName()
    PAR0031 = bgelogic.ParamOwnerObject()
    ACT0032 = bgelogic.SetLightEnergy()
    ACT0033 = bgelogic.SetLightEnergy()
    ACT0034 = bgelogic.SetLightEnergy()
    ACT0035 = bgelogic.SetLightEnergy()
    PAR0036 = bgelogic.ParameterSwitchValue()
    ACT0037 = bgelogic.SetLightEnergy()
    ACT0038 = bgelogic.SetLightEnergy()
    ACT0039 = bgelogic.SetLightEnergy()
    ACT0040 = bgelogic.SetLightEnergy()
    PAR0041 = bgelogic.ParameterSwitchValue()
    PAR0042 = bgelogic.ParameterObjectProperty()
    PAR0043 = bgelogic.ParameterDictionaryValue()
    CON0044 = bgelogic.ConditionKeyPressed()
    CON0045 = bgelogic.ConditionOr()
    CON0046 = bgelogic.ConditionGamepadButtons()
    PAR0047 = bgelogic.ConditionGamepadTrigger()
    CON0048 = bgelogic.ConditionKeyPressed()
    CON0049 = bgelogic.ConditionOr()
    CON0050 = bgelogic.ConditionOnce()
    CON0051 = bgelogic.ConditionKeyPressed()
    CON0052 = bgelogic.ConditionKeyPressed()
    PAR0053 = bgelogic.ValueSwitch()
    CON0054 = bgelogic.ConditionOnInit()
    ACT0055 = bgelogic.InitEmptyDict()
    PAR0056 = bgelogic.ValueSwitch()
    PAR0057 = bgelogic.ParamOwnerObject()
    ACT0058 = bgelogic.ActivateActuatorByName()
    ACT0059 = bgelogic.ActionMouseLook()
    PAR0060 = bgelogic.ParameterFindChildByName()
    CON0061 = bgelogic.ConditionOnUpdate()
    ACT0062 = bgelogic.ActionSetGameObjectGameProperty()
    PAR0063 = bgelogic.ParamOwnerObject()
    ACT0064 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0065 = bgelogic.ParameterPythonModuleFunction()
    PAR0066 = bgelogic.ParameterDictionaryValue()
    PAR0067 = bgelogic.ParameterDictionaryValue()
    ACT0000.condition = ACT0011.OUT
    ACT0000.dict = ACT0011.DICT
    ACT0000.key = "left"
    ACT0000.val = PAR0021.VAL
    ACT0001.condition = ACT0000.OUT
    ACT0001.dict = ACT0000.DICT
    ACT0001.key = "right"
    ACT0001.val = PAR0022.VAL
    ACT0002.condition = ACT0001.OUT
    ACT0002.dict = ACT0001.DICT
    ACT0002.key = "velocity"
    ACT0002.val = PAR0005
    ACT0003.condition = ACT0002.OUT
    ACT0003.dict = ACT0002.DICT
    ACT0003.key = "handbrake"
    ACT0003.val = CON0045
    ACT0004.condition = ACT0003.OUT
    ACT0004.dict = ACT0003.DICT
    ACT0004.key = "set_reverse"
    ACT0004.val = CON0049
    PAR0005.game_object = PAR0057
    PAR0005.attribute_name = "localLinearVelocity"
    ACT0007.condition = ACT0055.OUT
    ACT0007.game_object = PAR0063
    ACT0007.property_name = "_args"
    ACT0007.property_value = ACT0055.DICT
    PAR0008.game_object = PAR0057
    PAR0008.property_name = "_args"
    ACT0009.condition = CON0006
    ACT0009.dict = PAR0008
    ACT0009.key = "car"
    ACT0009.val = PAR0057
    ACT0010.condition = ACT0009.OUT
    ACT0010.dict = ACT0009.DICT
    ACT0010.key = "acc"
    ACT0010.val = PAR0013.VAL
    ACT0011.condition = ACT0010.OUT
    ACT0011.dict = ACT0010.DICT
    ACT0011.key = "brake"
    ACT0011.val = PAR0019.VAL
    CON0012.param_a = CON0014
    CON0012.param_b = PAR0015.VAL
    CON0012.operator = 2
    PAR0013.condition = CON0012
    PAR0013.val_a = PAR0015.VAL
    PAR0013.val_b = CON0014
    CON0014.key_code = bge.events.WKEY
    CON0014.pulse = True
    PAR0015.index = 0
    PAR0015.sensitivity = 1.0
    PAR0015.threshold = 0.05000000074505806
    PAR0015.axis = 1
    CON0016.param_a = CON0017
    CON0016.param_b = PAR0018.VAL
    CON0016.operator = 2
    CON0017.key_code = bge.events.SKEY
    CON0017.pulse = True
    PAR0018.index = 0
    PAR0018.sensitivity = 1.0
    PAR0018.threshold = 0.05000000074505806
    PAR0018.axis = 0
    PAR0019.condition = CON0016
    PAR0019.val_a = PAR0018.VAL
    PAR0019.val_b = CON0017
    CON0020.param_a = PAR0056.VAL
    CON0020.param_b = ACT0024.OUT
    CON0020.operator = 2
    PAR0021.condition = CON0020
    PAR0021.val_a = ACT0024.OUT
    PAR0021.val_b = PAR0056.VAL
    PAR0022.condition = PAR0053.VAL
    PAR0022.val_a = PAR0025.X
    PAR0022.val_b = PAR0053.VAL
    CON0023.param_a = CON0052
    CON0023.param_b = PAR0025.X
    CON0023.operator = 2
    ACT0024.value = PAR0025.X
    PAR0025.inverted = False
    PAR0025.index = 0
    PAR0025.sensitivity = 1.0
    PAR0025.threshold = 0.05000000074505806
    PAR0025.axis = 0
    ACT0026.condition = ACT0004.OUT
    ACT0026.module_name = "vehi"
    ACT0026.module_func = "control"
    ACT0026.use_arg = True
    ACT0026.arg = ACT0004.DICT
    PAR0027.from_parent = PAR0031
    PAR0027.child = "brake_L"
    PAR0028.from_parent = PAR0031
    PAR0028.child = "brake_R"
    PAR0029.from_parent = PAR0031
    PAR0029.child = "reverse_L"
    PAR0030.from_parent = PAR0031
    PAR0030.child = "reverse_R"
    ACT0032.condition = PAR0036.TRUE
    ACT0032.lamp = PAR0028
    ACT0032.energy = 10.0
    ACT0033.condition = PAR0036.TRUE
    ACT0033.lamp = PAR0027
    ACT0033.energy = 10.0
    ACT0034.condition = PAR0036.FALSE
    ACT0034.lamp = PAR0028
    ACT0034.energy = 5.0
    ACT0035.condition = PAR0036.FALSE
    ACT0035.lamp = PAR0027
    ACT0035.energy = 5.0
    PAR0036.state = PAR0043
    ACT0037.condition = PAR0041.TRUE
    ACT0037.lamp = PAR0030
    ACT0037.energy = 7.0
    ACT0038.condition = PAR0041.TRUE
    ACT0038.lamp = PAR0029
    ACT0038.energy = 7.0
    ACT0039.condition = PAR0041.FALSE
    ACT0039.lamp = PAR0030
    ACT0039.energy = 0.0
    ACT0040.condition = PAR0041.FALSE
    ACT0040.lamp = PAR0029
    ACT0040.energy = 0.0
    PAR0041.state = PAR0042
    PAR0042.game_object = PAR0031
    PAR0042.property_name = "_reverse"
    PAR0043.dict = ACT0026.VAL
    PAR0043.key = "is_braking"
    CON0044.key_code = bge.events.SPACEKEY
    CON0044.pulse = True
    CON0045.condition_a = CON0044
    CON0045.condition_b = CON0046.BUTTON
    CON0046.index = 0
    CON0046.pulse = True
    CON0046.button = 10
    PAR0047.index = 0
    PAR0047.sensitivity = 1.0
    PAR0047.threshold = 0.05000000074505806
    PAR0047.axis = 0
    CON0048.key_code = bge.events.SKEY
    CON0048.pulse = False
    CON0049.condition_a = CON0048
    CON0049.condition_b = CON0050
    CON0050.input_condition = PAR0047.VAL
    CON0051.key_code = bge.events.AKEY
    CON0051.pulse = True
    CON0052.key_code = bge.events.DKEY
    CON0052.pulse = True
    PAR0053.condition = CON0052
    PAR0053.val_a = 0.0
    PAR0053.val_b = 0.800000011920929
    ACT0055.condition = CON0054
    PAR0056.condition = CON0051
    PAR0056.val_a = 0.0
    PAR0056.val_b = 0.800000011920929
    ACT0058.condition = ACT0062.OUT
    ACT0058.actuator = "FXAA"
    ACT0059.condition = CON0061
    ACT0059.game_object_x = PAR0060
    ACT0059.game_object_y = None
    ACT0059.inverted = True
    ACT0059.sensitivity = 1.0
    ACT0059.use_cap_z = False
    ACT0059.cap_z = mathutils.Vector((0.0, 0.0))
    ACT0059.use_cap_y = True
    ACT0059.cap_y = mathutils.Vector((29.579999923706055, 0.0))
    PAR0060.from_parent = PAR0063
    PAR0060.child = "cam_controller"
    ACT0062.condition = ACT0065.OUT
    ACT0062.game_object = PAR0063
    ACT0062.property_name = "_car_wrapper"
    ACT0062.property_value = PAR0066
    ACT0064.condition = ACT0065.OUT
    ACT0064.game_object = PAR0063
    ACT0064.property_name = "_wheels"
    ACT0064.property_value = PAR0067
    ACT0065.condition = CON0054
    ACT0065.module_name = "vehi"
    ACT0065.module_func = "create"
    ACT0065.use_arg = True
    ACT0065.arg = PAR0063
    PAR0066.dict = ACT0065.VAL
    PAR0066.key = "car"
    PAR0067.dict = ACT0065.VAL
    PAR0067.key = "wheels"
    network.add_cell(CON0006)
    network.add_cell(CON0014)
    network.add_cell(CON0017)
    network.add_cell(PAR0025)
    network.add_cell(PAR0031)
    network.add_cell(PAR0042)
    network.add_cell(CON0044)
    network.add_cell(CON0046)
    network.add_cell(CON0048)
    network.add_cell(CON0051)
    network.add_cell(CON0054)
    network.add_cell(PAR0056)
    network.add_cell(CON0061)
    network.add_cell(PAR0063)
    network.add_cell(ACT0065)
    network.add_cell(PAR0067)
    network.add_cell(PAR0015)
    network.add_cell(PAR0018)
    network.add_cell(ACT0024)
    network.add_cell(PAR0027)
    network.add_cell(PAR0029)
    network.add_cell(PAR0041)
    network.add_cell(CON0045)
    network.add_cell(CON0052)
    network.add_cell(ACT0055)
    network.add_cell(PAR0060)
    network.add_cell(ACT0064)
    network.add_cell(ACT0007)
    network.add_cell(CON0012)
    network.add_cell(CON0016)
    network.add_cell(CON0020)
    network.add_cell(CON0023)
    network.add_cell(PAR0028)
    network.add_cell(ACT0038)
    network.add_cell(ACT0040)
    network.add_cell(PAR0047)
    network.add_cell(CON0050)
    network.add_cell(PAR0057)
    network.add_cell(ACT0059)
    network.add_cell(PAR0066)
    network.add_cell(PAR0005)
    network.add_cell(PAR0013)
    network.add_cell(PAR0021)
    network.add_cell(PAR0030)
    network.add_cell(ACT0037)
    network.add_cell(CON0049)
    network.add_cell(ACT0062)
    network.add_cell(PAR0008)
    network.add_cell(PAR0019)
    network.add_cell(ACT0039)
    network.add_cell(PAR0053)
    network.add_cell(ACT0009)
    network.add_cell(PAR0022)
    network.add_cell(ACT0058)
    network.add_cell(ACT0010)
    network.add_cell(ACT0011)
    network.add_cell(ACT0000)
    network.add_cell(ACT0001)
    network.add_cell(ACT0002)
    network.add_cell(ACT0003)
    network.add_cell(ACT0004)
    network.add_cell(ACT0026)
    network.add_cell(PAR0043)
    network.add_cell(PAR0036)
    network.add_cell(ACT0032)
    network.add_cell(ACT0034)
    network.add_cell(ACT0033)
    network.add_cell(ACT0035)
    owner["vehicule"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__vehicule')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("vehicule")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
