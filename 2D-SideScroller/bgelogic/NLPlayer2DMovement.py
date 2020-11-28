# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.ActionSetObjectAttribute()
    PAR0001 = bgelogic.ParameterVector3Simple()
    PAR0002 = bgelogic.ParameterObjectAttribute()
    PAR0003 = bgelogic.ParameterArithmeticOp()
    PAR0004 = bgelogic.ParameterObjectProperty()
    ACT0005 = bgelogic.ActionSetCharacterWalkDir()
    PAR0006 = bgelogic.ParameterArithmeticOp()
    CON0007 = bgelogic.ConditionOnUpdate()
    ACT0008 = bgelogic.ActionRotateTo()
    ACT0000.condition = ACT0008
    ACT0000.xyz = {'x': True, 'y': False, 'z': False}
    ACT0000.game_object = "NLO:U_O"
    ACT0000.attribute_value = mathutils.Vector((0.0, 0.0, 0.0))
    ACT0000.value_type = 'worldPosition'
    PAR0001.input_x = 0.0
    PAR0001.input_y = PAR0003
    PAR0001.input_z = 0.0
    PAR0002.game_object = "NLO:U_O"
    PAR0002.attribute_name = "worldPosition"
    PAR0003.operator = bgelogic.ParameterArithmeticOp.op_by_code("MUL")
    PAR0003.operand_a = PAR0004
    PAR0003.operand_b = 0.20000000298023224
    PAR0004.game_object = "NLO:U_O"
    PAR0004.property_name = "running"
    ACT0005.condition = ACT0008
    ACT0005.game_object = "NLO:U_O"
    ACT0005.walkDir = PAR0001.OUTV
    PAR0006.operator = bgelogic.ParameterArithmeticOp.op_by_code("ADD")
    PAR0006.operand_a = PAR0001.OUTV
    PAR0006.operand_b = PAR0002
    ACT0008.condition = CON0007
    ACT0008.moving_object = "NLO:U_O"
    ACT0008.target_point = PAR0006
    ACT0008.rot_axis = 2
    ACT0008.front_axis = 1
    network.add_cell(PAR0002)
    network.add_cell(PAR0004)
    network.add_cell(CON0007)
    network.add_cell(PAR0003)
    network.add_cell(PAR0001)
    network.add_cell(PAR0006)
    network.add_cell(ACT0008)
    network.add_cell(ACT0000)
    network.add_cell(ACT0005)
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
