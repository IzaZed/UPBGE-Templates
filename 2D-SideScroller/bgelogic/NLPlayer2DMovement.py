# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionOnUpdate()
    PAR0001 = bgelogic.ParameterArithmeticOp()
    ACT0002 = bgelogic.ActionSetCharacterWalkDir()
    PAR0003 = bgelogic.ParameterObjectProperty()
    PAR0004 = bgelogic.ParameterArithmeticOp()
    PAR0005 = bgelogic.ParameterObjectAttribute()
    PAR0006 = bgelogic.ParameterVector3Simple()
    ACT0007 = bgelogic.ActionRotateTo()
    ACT0008 = bgelogic.ActionSetObjectAttribute()
    PAR0001.operator = bgelogic.ParameterArithmeticOp.op_by_code("ADD")
    PAR0001.operand_a = PAR0006.OUTV
    PAR0001.operand_b = PAR0005
    ACT0002.condition = ACT0007
    ACT0002.game_object = "NLO:U_O"
    ACT0002.walkDir = PAR0006.OUTV
    PAR0003.game_object = "NLO:U_O"
    PAR0003.property_name = "running"
    PAR0004.operator = bgelogic.ParameterArithmeticOp.op_by_code("MUL")
    PAR0004.operand_a = PAR0003
    PAR0004.operand_b = 0.20000000298023224
    PAR0005.game_object = "NLO:U_O"
    PAR0005.attribute_name = "worldPosition"
    PAR0006.input_x = 0.0
    PAR0006.input_y = PAR0004
    PAR0006.input_z = 0.0
    ACT0007.condition = CON0000
    ACT0007.moving_object = "NLO:U_O"
    ACT0007.target_point = PAR0001
    ACT0007.rot_axis = 2
    ACT0007.front_axis = 1
    ACT0008.condition = ACT0007
    ACT0008.xyz = {'x': True, 'y': False, 'z': False}
    ACT0008.game_object = "NLO:U_O"
    ACT0008.attribute_value = mathutils.Vector((0.0, 0.0, 0.0))
    ACT0008.value_type = 'worldPosition'
    network.add_cell(CON0000)
    network.add_cell(PAR0003)
    network.add_cell(PAR0005)
    network.add_cell(PAR0004)
    network.add_cell(PAR0006)
    network.add_cell(PAR0001)
    network.add_cell(ACT0007)
    network.add_cell(ACT0002)
    network.add_cell(ACT0008)
    owner["Player_2D_Movement"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__Player_2D_Movement')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("Player_2D_Movement")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
