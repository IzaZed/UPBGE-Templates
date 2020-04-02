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
    ACT0006 = bgelogic.ActionSetGlobalValue()
    ACT0007 = bgelogic.ActionSetGlobalValue()
    ACT0008 = bgelogic.ActionSetGlobalValue()
    CON0009 = bgelogic.ConditionOr()
    CON0010 = bgelogic.ConditionOr()
    ACT0011 = bgelogic.InvertBool()
    ACT0012 = bgelogic.ActionSetGlobalValue()
    ACT0013 = bgelogic.ActionSetGlobalValue()
    PAR0014 = bgelogic.ParameterGetGlobalValue()
    PAR0015 = bgelogic.ParameterGetGlobalValue()
    PAR0016 = bgelogic.ParameterVector3Simple()
    PAR0017 = bgelogic.ParameterVectorMath()
    PAR0018 = bgelogic.ParameterArithmeticOp()
    CON0019 = bgelogic.ConditionOnUpdate()
    PAR0020 = bgelogic.ParamOwnerObject()
    ACT0021 = bgelogic.ActionApplyLocation()
    ACT0022 = bgelogic.InvertBool()
    PAR0023 = bgelogic.ParameterSimpleValue()
    ACT0024 = bgelogic.ActionSetGlobalValue()
    PAR0025 = bgelogic.ParameterObjectProperty()
    CON0026 = bgelogic.ConditionAnd()
    ACT0027 = bgelogic.ActionRemoveParent()
    ACT0028 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0029 = bgelogic.ActionSetGameObjectVisibility()
    ACT0030 = bgelogic.ActionSetGameObjectVisibility()
    CON0031 = bgelogic.ConditionKeyPressed()
    ACT0032 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0033 = bgelogic.ActionSetParent()
    ACT0034 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0035 = bgelogic.ActionSetObjectAttribute()
    PAR0036 = bgelogic.ParameterObjectAttribute()
    CON0037 = bgelogic.ConditionKeyPressed()
    CON0038 = bgelogic.ConditionKeyPressed()
    CON0039 = bgelogic.ConditionKeyPressed()
    CON0040 = bgelogic.ConditionKeyPressed()
    PAR0041 = bgelogic.ParameterObjectAttribute()
    PAR0042 = bgelogic.ParameterObjectAttribute()
    CON0043 = bgelogic.ConditionOnUpdate()
    PAR0044 = bgelogic.ParameterObjectProperty()
    CON0045 = bgelogic.ConditionAndNot()
    ACT0046 = bgelogic.ActionRayPick()
    PAR0047 = bgelogic.ParameterSwitchValue()
    CON0048 = bgelogic.ConditionAnd()
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
    ACT0006.condition = CON0037
    ACT0006.data_id = "movement"
    ACT0006.persistent = False
    ACT0006.key = "x"
    ACT0006.value = -1
    ACT0007.condition = CON0038
    ACT0007.data_id = "movement"
    ACT0007.persistent = False
    ACT0007.key = "y"
    ACT0007.value = 1
    ACT0008.condition = CON0039
    ACT0008.data_id = "movement"
    ACT0008.persistent = False
    ACT0008.key = "y"
    ACT0008.value = -1
    CON0009.condition_a = ACT0024.OUT
    CON0009.condition_b = ACT0006.OUT
    CON0010.condition_a = ACT0007.OUT
    CON0010.condition_b = ACT0008.OUT
    ACT0011.value = CON0010
    ACT0012.condition = ACT0022.OUT
    ACT0012.data_id = "movement"
    ACT0012.persistent = False
    ACT0012.key = "x"
    ACT0012.value = 0
    ACT0013.condition = ACT0011.OUT
    ACT0013.data_id = "movement"
    ACT0013.persistent = False
    ACT0013.key = "y"
    ACT0013.value = 0
    PAR0014.data_id = "movement"
    PAR0014.key = "x"
    PAR0015.data_id = "movement"
    PAR0015.key = "y"
    PAR0016.input_x = PAR0014
    PAR0016.input_y = PAR0015
    PAR0016.input_z = 0.0
    PAR0017.op = 'normalize'
    PAR0017.vector = PAR0016.OUTV
    PAR0017.vector_2 = mathutils.Vector((0.0, 0.0, 0.0))
    PAR0017.factor = 0.0
    PAR0018.operator = bgelogic.ParameterArithmeticOp.op_by_code("MUL")
    PAR0018.operand_a = PAR0017
    PAR0018.operand_b = PAR0023
    ACT0021.local = True
    ACT0021.condition = CON0019
    ACT0021.game_object = PAR0020
    ACT0021.movement = PAR0018
    ACT0022.value = CON0009
    PAR0023.value = PAR0002.VAL
    ACT0024.condition = CON0040
    ACT0024.data_id = "movement"
    ACT0024.persistent = False
    ACT0024.key = "x"
    ACT0024.value = 1
    PAR0025.game_object = "Object:Player"
    PAR0025.property_name = "object_taken"
    CON0026.condition_a = CON0031
    CON0026.condition_b = PAR0047.FALSE
    ACT0027.condition = CON0026
    ACT0027.child_object = PAR0025
    ACT0028.condition = ACT0027.OUT
    ACT0028.game_object = "Object:Player"
    ACT0028.property_name = "occupado"
    ACT0028.property_value = False
    ACT0029.condition = PAR0047.TRUE
    ACT0029.game_object = "Object:Text"
    ACT0029.visible = True
    ACT0029.recursive = False
    ACT0030.condition = PAR0047.FALSE
    ACT0030.game_object = "Object:Text"
    ACT0030.visible = False
    ACT0030.recursive = False
    CON0031.key_code = bge.events.EKEY
    CON0031.pulse = False
    ACT0032.condition = ACT0035.OUT
    ACT0032.game_object = "Object:Player"
    ACT0032.property_name = "object_taken"
    ACT0032.property_value = ACT0046.PICKED_OBJECT
    ACT0033.condition = CON0048
    ACT0033.child_object = ACT0046.PICKED_OBJECT
    ACT0033.parent_object = "Object:Hand"
    ACT0033.compound = True
    ACT0033.ghost = True
    ACT0034.condition = ACT0033.OUT
    ACT0034.game_object = "Object:Player"
    ACT0034.property_name = "occupado"
    ACT0034.property_value = True
    ACT0035.condition = ACT0034.OUT
    ACT0035.game_object = ACT0046.PICKED_OBJECT
    ACT0035.attribute_value = PAR0036
    ACT0035.value_type = 'worldPosition'
    PAR0036.game_object = "Object:Hand"
    PAR0036.attribute_name = "worldPosition"
    CON0037.key_code = bge.events.SKEY
    CON0037.pulse = True
    CON0038.key_code = bge.events.AKEY
    CON0038.pulse = True
    CON0039.key_code = bge.events.DKEY
    CON0039.pulse = True
    CON0040.key_code = bge.events.WKEY
    CON0040.pulse = True
    PAR0041.game_object = "Object:Empty"
    PAR0041.attribute_name = "worldPosition"
    PAR0042.game_object = "Object:Camera.001"
    PAR0042.attribute_name = "worldPosition"
    PAR0044.game_object = "Object:Player"
    PAR0044.property_name = "occupado"
    CON0045.condition_a = ACT0046
    CON0045.condition_b = PAR0044
    ACT0046.condition = CON0043
    ACT0046.origin = PAR0042
    ACT0046.destination = PAR0041
    ACT0046.property_name = "take_able"
    ACT0046.distance = 3.0
    PAR0047.state = CON0045
    CON0048.condition_a = CON0031
    CON0048.condition_b = PAR0047.TRUE
    network.add_cell(CON0000)
    network.add_cell(CON0003)
    network.add_cell(PAR0014)
    network.add_cell(CON0019)
    network.add_cell(PAR0025)
    network.add_cell(CON0031)
    network.add_cell(PAR0036)
    network.add_cell(CON0038)
    network.add_cell(CON0040)
    network.add_cell(PAR0042)
    network.add_cell(PAR0044)
    network.add_cell(ACT0001)
    network.add_cell(CON0004)
    network.add_cell(ACT0007)
    network.add_cell(PAR0015)
    network.add_cell(PAR0020)
    network.add_cell(ACT0024)
    network.add_cell(CON0037)
    network.add_cell(PAR0041)
    network.add_cell(PAR0002)
    network.add_cell(ACT0006)
    network.add_cell(CON0009)
    network.add_cell(PAR0016)
    network.add_cell(ACT0022)
    network.add_cell(CON0039)
    network.add_cell(ACT0005)
    network.add_cell(ACT0012)
    network.add_cell(PAR0017)
    network.add_cell(PAR0023)
    network.add_cell(CON0043)
    network.add_cell(ACT0046)
    network.add_cell(ACT0008)
    network.add_cell(PAR0018)
    network.add_cell(CON0045)
    network.add_cell(CON0010)
    network.add_cell(ACT0021)
    network.add_cell(PAR0047)
    network.add_cell(ACT0011)
    network.add_cell(CON0026)
    network.add_cell(ACT0029)
    network.add_cell(CON0048)
    network.add_cell(ACT0013)
    network.add_cell(ACT0030)
    network.add_cell(ACT0033)
    network.add_cell(ACT0027)
    network.add_cell(ACT0034)
    network.add_cell(ACT0028)
    network.add_cell(ACT0035)
    network.add_cell(ACT0032)
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
