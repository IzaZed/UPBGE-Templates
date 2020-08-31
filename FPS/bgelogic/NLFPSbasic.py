# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionKeyPressed()
    CON0001 = bgelogic.ConditionKeyPressed()
    CON0002 = bgelogic.ConditionKeyPressed()
    CON0003 = bgelogic.ConditionKeyPressed()
    ACT0004 = bgelogic.ActionSetGlobalValue()
    ACT0005 = bgelogic.ActionSetGlobalValue()
    ACT0006 = bgelogic.ActionSetGlobalValue()
    ACT0007 = bgelogic.ActionSetGlobalValue()
    CON0008 = bgelogic.ConditionOr()
    CON0009 = bgelogic.ConditionOr()
    ACT0010 = bgelogic.InvertBool()
    ACT0011 = bgelogic.InvertBool()
    ACT0012 = bgelogic.ActionSetGlobalValue()
    ACT0013 = bgelogic.ActionSetGlobalValue()
    PAR0014 = bgelogic.ParameterGetGlobalValue()
    PAR0015 = bgelogic.ParameterGetGlobalValue()
    PAR0016 = bgelogic.ParameterVector3Simple()
    PAR0017 = bgelogic.ParameterVectorMath()
    PAR0018 = bgelogic.ParameterSimpleValue()
    PAR0019 = bgelogic.ParameterArithmeticOp()
    CON0020 = bgelogic.ConditionOnUpdate()
    PAR0021 = bgelogic.ParamOwnerObject()
    ACT0022 = bgelogic.ActionApplyLocation()
    CON0023 = bgelogic.ConditionKeyPressed()
    ACT0024 = bgelogic.ActionCharacterJump()
    PAR0025 = bgelogic.ValueSwitch()
    CON0026 = bgelogic.ConditionKeyPressed()
    CON0027 = bgelogic.ConditionOnUpdate()
    CON0028 = bgelogic.ConditionMousePressed()
    ACT0029 = bgelogic.ActionMouseLook()
    PAR0030 = bgelogic.ValueSwitch()
    PAR0031 = bgelogic.ParameterObjectAttribute()
    PAR0032 = bgelogic.ParameterObjectAttribute()
    CON0033 = bgelogic.ConditionMousePressed()
    ACT0034 = bgelogic.ActionRayPick()
    ACT0035 = bgelogic.ActionApplyImpulse()
    CON0000.key_code = bge.events.WKEY
    CON0000.pulse = True
    CON0001.key_code = bge.events.SKEY
    CON0001.pulse = True
    CON0002.key_code = bge.events.AKEY
    CON0002.pulse = True
    CON0003.key_code = bge.events.DKEY
    CON0003.pulse = True
    ACT0004.condition = CON0000
    ACT0004.data_id = "movement"
    ACT0004.persistent = False
    ACT0004.key = "x"
    ACT0004.value = 1
    ACT0005.condition = CON0001
    ACT0005.data_id = "movement"
    ACT0005.persistent = False
    ACT0005.key = "x"
    ACT0005.value = -1
    ACT0006.condition = CON0002
    ACT0006.data_id = "movement"
    ACT0006.persistent = False
    ACT0006.key = "y"
    ACT0006.value = 1
    ACT0007.condition = CON0003
    ACT0007.data_id = "movement"
    ACT0007.persistent = False
    ACT0007.key = "y"
    ACT0007.value = -1
    CON0008.condition_a = ACT0004.OUT
    CON0008.condition_b = ACT0005.OUT
    CON0009.condition_a = ACT0006.OUT
    CON0009.condition_b = ACT0007.OUT
    ACT0010.value = CON0008
    ACT0011.value = CON0009
    ACT0012.condition = ACT0010.OUT
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
    PAR0018.value = PAR0025.VAL
    PAR0019.operator = bgelogic.ParameterArithmeticOp.op_by_code("MUL")
    PAR0019.operand_a = PAR0017
    PAR0019.operand_b = PAR0018
    ACT0022.local = True
    ACT0022.condition = CON0020
    ACT0022.game_object = PAR0021
    ACT0022.movement = PAR0019
    CON0023.key_code = bge.events.SPACEKEY
    CON0023.pulse = False
    ACT0024.condition = CON0023
    ACT0024.game_object = "Object:Player"
    PAR0025.condition = CON0026
    PAR0025.val_a = 0.10000000149011612
    PAR0025.val_b = 0.15000000596046448
    CON0026.key_code = bge.events.LEFTSHIFTKEY
    CON0026.pulse = True
    CON0028.mouse_button_code = bge.events.RIGHTMOUSE
    CON0028.pulse = True
    ACT0029.condition = CON0027
    ACT0029.game_object_x = "Object:Player"
    ACT0029.game_object_y = "Object:Player_Head"
    ACT0029.inverted = False
    ACT0029.sensitivity = PAR0030.VAL
    ACT0029.use_cap_z = False
    ACT0029.cap_z = mathutils.Vector((0.0, 0.0))
    ACT0029.use_cap_y = True
    ACT0029.cap_y = mathutils.Vector((70.0, 70.0))
    PAR0030.condition = CON0028
    PAR0030.val_a = 1.0
    PAR0030.val_b = 0.30000001192092896
    PAR0031.game_object = "Object:Aim"
    PAR0031.attribute_name = "worldPosition"
    PAR0032.game_object = "Object:Nozzle"
    PAR0032.attribute_name = "worldPosition"
    CON0033.mouse_button_code = bge.events.LEFTMOUSE
    CON0033.pulse = False
    ACT0034.condition = CON0033
    ACT0034.origin = PAR0032
    ACT0034.destination = PAR0031
    ACT0034.property_name = ""
    ACT0034.distance = 100.0
    ACT0035.local = False
    ACT0035.condition = ACT0034
    ACT0035.game_object = ACT0034.PICKED_OBJECT
    ACT0035.point = ACT0034.POINT
    ACT0035.impulse = ACT0034.DIRECTION
    network.add_cell(CON0000)
    network.add_cell(CON0002)
    network.add_cell(ACT0004)
    network.add_cell(ACT0006)
    network.add_cell(PAR0014)
    network.add_cell(CON0020)
    network.add_cell(CON0023)
    network.add_cell(CON0026)
    network.add_cell(CON0028)
    network.add_cell(PAR0030)
    network.add_cell(PAR0032)
    network.add_cell(CON0001)
    network.add_cell(ACT0005)
    network.add_cell(CON0008)
    network.add_cell(ACT0010)
    network.add_cell(ACT0012)
    network.add_cell(PAR0015)
    network.add_cell(PAR0021)
    network.add_cell(ACT0024)
    network.add_cell(CON0027)
    network.add_cell(PAR0031)
    network.add_cell(CON0003)
    network.add_cell(PAR0016)
    network.add_cell(PAR0025)
    network.add_cell(CON0033)
    network.add_cell(ACT0007)
    network.add_cell(PAR0017)
    network.add_cell(ACT0029)
    network.add_cell(CON0009)
    network.add_cell(PAR0018)
    network.add_cell(ACT0034)
    network.add_cell(ACT0011)
    network.add_cell(PAR0019)
    network.add_cell(ACT0035)
    network.add_cell(ACT0013)
    network.add_cell(ACT0022)
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
