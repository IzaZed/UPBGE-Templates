# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.ActionSetObjectAttribute()
    ACT0001 = bgelogic.ActionRotateTo()
    PAR0002 = bgelogic.ParameterVector3Simple()
    PAR0003 = bgelogic.ParameterObjectAttribute()
    PAR0004 = bgelogic.ParameterArithmeticOp()
    PAR0005 = bgelogic.ParameterObjectProperty()
    ACT0006 = bgelogic.ActionSetCharacterWalkDir()
    PAR0007 = bgelogic.ParameterArithmeticOp()
    CON0008 = bgelogic.ConditionOnUpdate()
    ACT0009 = bgelogic.ActionSetObjectAttribute()
    CON0010 = bgelogic.ConditionCollision()
    ACT0000.condition = ACT0001
    ACT0000.xyz = {'x': True, 'y': False, 'z': False}
    ACT0000.game_object = "NLO:U_O"
    ACT0000.attribute_value = mathutils.Vector((0.0, 0.0, 0.0))
    ACT0000.value_type = 'worldPosition'
    ACT0001.condition = CON0008
    ACT0001.moving_object = "NLO:U_O"
    ACT0001.target_point = PAR0007
    ACT0001.rot_axis = 2
    ACT0001.front_axis = 1
    PAR0002.input_x = 0.0
    PAR0002.input_y = PAR0004
    PAR0002.input_z = 0.0
    PAR0003.game_object = "NLO:U_O"
    PAR0003.attribute_name = "worldPosition"
    PAR0004.operator = bgelogic.ParameterArithmeticOp.op_by_code("MUL")
    PAR0004.operand_a = PAR0005
    PAR0004.operand_b = 0.20000000298023224
    PAR0005.game_object = "NLO:U_O"
    PAR0005.property_name = "running"
    ACT0006.local = False
    ACT0006.condition = ACT0001
    ACT0006.game_object = "NLO:U_O"
    ACT0006.walkDir = PAR0002.OUTV
    PAR0007.operator = bgelogic.ParameterArithmeticOp.op_by_code("ADD")
    PAR0007.operand_a = PAR0002.OUTV
    PAR0007.operand_b = PAR0003
    ACT0009.condition = CON0010
    ACT0009.xyz = {'x': True, 'y': True, 'z': True}
    ACT0009.game_object = "NLO:U_O"
    ACT0009.attribute_value = mathutils.Vector((0.0, 0.0, 0.0))
    ACT0009.value_type = 'worldPosition'
    CON0010.game_object = "NLO:U_O"
    CON0010.use_mat = False
    CON0010.prop = "bedrock"
    CON0010.material = None
    CON0010.pulse = True
    network.add_cell(PAR0003)
    network.add_cell(PAR0005)
    network.add_cell(CON0008)
    network.add_cell(CON0010)
    network.add_cell(PAR0004)
    network.add_cell(ACT0009)
    network.add_cell(PAR0002)
    network.add_cell(PAR0007)
    network.add_cell(ACT0001)
    network.add_cell(ACT0000)
    network.add_cell(ACT0006)
    owner["IGNLTree_Player_2D_Movement"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__Player_2D_Movement')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_Player_2D_Movement")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
