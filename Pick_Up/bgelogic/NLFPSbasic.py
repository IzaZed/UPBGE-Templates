#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionKeyPressed()
    ACT0001 = bgelogic.ActionCharacterJump()
    PAR0002 = bgelogic.ValueSwitch()
    CON0003 = bgelogic.ConditionKeyPressed()
    CON0004 = bgelogic.ConditionOnUpdate()
    ACT0005 = bgelogic.ActionMouseLook()
    CON0006 = bgelogic.ConditionKeyPressed()
    CON0007 = bgelogic.ConditionKeyPressed()
    CON0008 = bgelogic.ConditionKeyPressed()
    ACT0009 = bgelogic.ActionSetGlobalValue()
    ACT0010 = bgelogic.ActionSetGlobalValue()
    ACT0011 = bgelogic.ActionSetGlobalValue()
    CON0012 = bgelogic.ConditionOr()
    CON0013 = bgelogic.ConditionOr()
    ACT0014 = bgelogic.InvertBool()
    ACT0015 = bgelogic.ActionSetGlobalValue()
    ACT0016 = bgelogic.ActionSetGlobalValue()
    PAR0017 = bgelogic.ParameterGetGlobalValue()
    PAR0018 = bgelogic.ParameterGetGlobalValue()
    PAR0019 = bgelogic.ParameterVector3Simple()
    PAR0020 = bgelogic.ParameterVectorMath()
    PAR0021 = bgelogic.ParameterArithmeticOp()
    CON0022 = bgelogic.ConditionOnUpdate()
    PAR0023 = bgelogic.ParamOwnerObject()
    ACT0024 = bgelogic.ActionApplyLocation()
    ACT0025 = bgelogic.InvertBool()
    PAR0026 = bgelogic.ParameterSimpleValue()
    ACT0027 = bgelogic.ActionSetGlobalValue()
    CON0028 = bgelogic.ConditionKeyPressed()
    PAR0029 = bgelogic.ParameterObjectAttribute()
    PAR0030 = bgelogic.ParameterObjectAttribute()
    CON0031 = bgelogic.ConditionOnUpdate()
    PAR0032 = bgelogic.ParameterObjectProperty()
    CON0033 = bgelogic.ConditionAndNot()
    ACT0034 = bgelogic.ActionRayPick()
    PAR0035 = bgelogic.ParameterSwitchValue()
    CON0036 = bgelogic.ConditionAnd()
    ACT0037 = bgelogic.ActionSetGameObjectVisibility()
    ACT0038 = bgelogic.ActionSetGameObjectVisibility()
    PAR0039 = bgelogic.ParameterObjectProperty()
    CON0040 = bgelogic.ConditionAnd()
    ACT0041 = bgelogic.ActionRemoveParent()
    ACT0042 = bgelogic.ActionSetGameObjectGameProperty()
    PAR0043 = bgelogic.ParameterObjectAttribute()
    ACT0044 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0045 = bgelogic.ActionSetObjectAttribute()
    ACT0046 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0047 = bgelogic.ActionSetParent()
    CON0048 = bgelogic.ConditionKeyPressed()
    CON0000.key_code = bge.events.SPACEKEY
    CON0000.pulse = False
    ACT0001.condition = CON0000
    ACT0001.game_object = "Object:Player"
    PAR0002.condition = CON0003
    PAR0002.val_a = 0.10000000149011612
    PAR0002.val_b = 0.15000000596046448
    CON0003.key_code = bge.events.LEFTSHIFTKEY
    CON0003.pulse = True
    ACT0005.condition = CON0004
    ACT0005.game_object_x = "Object:Player"
    ACT0005.game_object_y = "Object:Player_Head"
    ACT0005.inverted = False
    ACT0005.sensitivity = 1.0
    ACT0005.use_cap_z = False
    ACT0005.cap_z = mathutils.Vector((0.0, 0.0))
    ACT0005.use_cap_y = True
    ACT0005.cap_y = mathutils.Vector((70.0, 70.0))
    CON0006.key_code = bge.events.SKEY
    CON0006.pulse = True
    CON0007.key_code = bge.events.AKEY
    CON0007.pulse = True
    CON0008.key_code = bge.events.DKEY
    CON0008.pulse = True
    ACT0009.condition = CON0006
    ACT0009.data_id = "movement"
    ACT0009.persistent = False
    ACT0009.key = "x"
    ACT0009.value = -1
    ACT0010.condition = CON0007
    ACT0010.data_id = "movement"
    ACT0010.persistent = False
    ACT0010.key = "y"
    ACT0010.value = 1
    ACT0011.condition = CON0008
    ACT0011.data_id = "movement"
    ACT0011.persistent = False
    ACT0011.key = "y"
    ACT0011.value = -1
    CON0012.condition_a = ACT0027.OUT
    CON0012.condition_b = ACT0009.OUT
    CON0013.condition_a = ACT0010.OUT
    CON0013.condition_b = ACT0011.OUT
    ACT0014.value = CON0013
    ACT0015.condition = ACT0025.OUT
    ACT0015.data_id = "movement"
    ACT0015.persistent = False
    ACT0015.key = "x"
    ACT0015.value = 0
    ACT0016.condition = ACT0014.OUT
    ACT0016.data_id = "movement"
    ACT0016.persistent = False
    ACT0016.key = "y"
    ACT0016.value = 0
    PAR0017.data_id = "movement"
    PAR0017.key = "x"
    PAR0018.data_id = "movement"
    PAR0018.key = "y"
    PAR0019.input_x = PAR0017
    PAR0019.input_y = PAR0018
    PAR0019.input_z = 0.0
    PAR0020.op = 'normalize'
    PAR0020.vector = PAR0019.OUTV
    PAR0020.vector_2 = mathutils.Vector((0.0, 0.0, 0.0))
    PAR0020.factor = 0.0
    PAR0021.operator = bgelogic.ParameterArithmeticOp.op_by_code("MUL")
    PAR0021.operand_a = PAR0020
    PAR0021.operand_b = PAR0026
    ACT0024.local = True
    ACT0024.condition = CON0022
    ACT0024.game_object = PAR0023
    ACT0024.movement = PAR0021
    ACT0025.value = CON0012
    PAR0026.value = PAR0002.VAL
    ACT0027.condition = CON0028
    ACT0027.data_id = "movement"
    ACT0027.persistent = False
    ACT0027.key = "x"
    ACT0027.value = 1
    CON0028.key_code = bge.events.WKEY
    CON0028.pulse = True
    PAR0029.game_object = "Object:Empty"
    PAR0029.attribute_name = "worldPosition"
    PAR0030.game_object = "Object:Camera.001"
    PAR0030.attribute_name = "worldPosition"
    PAR0032.game_object = "Object:Player"
    PAR0032.property_name = "occupado"
    CON0033.condition_a = ACT0034
    CON0033.condition_b = PAR0032
    ACT0034.condition = CON0031
    ACT0034.origin = PAR0030
    ACT0034.destination = PAR0029
    ACT0034.property_name = "take_able"
    ACT0034.distance = 3.0
    PAR0035.state = CON0033
    CON0036.condition_a = CON0048
    CON0036.condition_b = PAR0035.TRUE
    ACT0037.condition = PAR0035.FALSE
    ACT0037.game_object = "Object:Text"
    ACT0037.visible = False
    ACT0037.recursive = False
    ACT0038.condition = PAR0035.TRUE
    ACT0038.game_object = "Object:Text"
    ACT0038.visible = True
    ACT0038.recursive = False
    PAR0039.game_object = "Object:Player"
    PAR0039.property_name = "object_taken"
    CON0040.condition_a = CON0048
    CON0040.condition_b = PAR0035.FALSE
    ACT0041.condition = CON0040
    ACT0041.child_object = PAR0039
    ACT0042.condition = ACT0041.OUT
    ACT0042.game_object = "Object:Player"
    ACT0042.property_name = "occupado"
    ACT0042.property_value = False
    PAR0043.game_object = "Object:Hand"
    PAR0043.attribute_name = "worldPosition"
    ACT0044.condition = ACT0045.OUT
    ACT0044.game_object = "Object:Player"
    ACT0044.property_name = "object_taken"
    ACT0044.property_value = ACT0034.PICKED_OBJECT
    ACT0045.condition = ACT0046.OUT
    ACT0045.game_object = ACT0034.PICKED_OBJECT
    ACT0045.attribute_value = PAR0043
    ACT0045.value_type = 'worldPosition'
    ACT0046.condition = ACT0047.OUT
    ACT0046.game_object = "Object:Player"
    ACT0046.property_name = "occupado"
    ACT0046.property_value = True
    ACT0047.condition = CON0036
    ACT0047.child_object = ACT0034.PICKED_OBJECT
    ACT0047.parent_object = "Object:Hand"
    ACT0047.compound = True
    ACT0047.ghost = True
    CON0048.key_code = bge.events.EKEY
    CON0048.pulse = False
    network.add_cell(CON0000)
    network.add_cell(CON0003)
    network.add_cell(CON0006)
    network.add_cell(CON0008)
    network.add_cell(ACT0011)
    network.add_cell(PAR0017)
    network.add_cell(CON0022)
    network.add_cell(CON0028)
    network.add_cell(PAR0030)
    network.add_cell(PAR0032)
    network.add_cell(PAR0039)
    network.add_cell(PAR0043)
    network.add_cell(CON0048)
    network.add_cell(ACT0001)
    network.add_cell(CON0004)
    network.add_cell(CON0007)
    network.add_cell(ACT0010)
    network.add_cell(CON0013)
    network.add_cell(PAR0018)
    network.add_cell(PAR0023)
    network.add_cell(ACT0027)
    network.add_cell(CON0031)
    network.add_cell(PAR0002)
    network.add_cell(ACT0009)
    network.add_cell(ACT0014)
    network.add_cell(ACT0016)
    network.add_cell(PAR0026)
    network.add_cell(ACT0005)
    network.add_cell(PAR0019)
    network.add_cell(PAR0029)
    network.add_cell(ACT0034)
    network.add_cell(CON0012)
    network.add_cell(PAR0020)
    network.add_cell(ACT0025)
    network.add_cell(ACT0015)
    network.add_cell(CON0033)
    network.add_cell(PAR0021)
    network.add_cell(PAR0035)
    network.add_cell(ACT0037)
    network.add_cell(CON0040)
    network.add_cell(ACT0024)
    network.add_cell(ACT0038)
    network.add_cell(CON0036)
    network.add_cell(ACT0047)
    network.add_cell(ACT0041)
    network.add_cell(ACT0046)
    network.add_cell(ACT0042)
    network.add_cell(ACT0045)
    network.add_cell(ACT0044)
    owner["FPS_basic"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__FPS_basic')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("FPS_basic")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
