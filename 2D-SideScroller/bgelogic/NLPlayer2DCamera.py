# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    PAR0000 = bgelogic.ParameterSimpleValue()
    PAR0001 = bgelogic.ParameterSimpleValue()
    PAR0002 = bgelogic.ParameterActiveCamera()
    ACT0003 = bgelogic.ActionSetObjectAttribute()
    CON0004 = bgelogic.ConditionOnUpdate()
    PAR0005 = bgelogic.ParameterVectorMath()
    PAR0006 = bgelogic.ParameterVector3Simple()
    PAR0007 = bgelogic.ParameterObjectAttribute()
    PAR0008 = bgelogic.ParameterVector3Split()
    PAR0009 = bgelogic.ParameterArithmeticOp()
    PAR0010 = bgelogic.ParameterArithmeticOp()
    PAR0011 = bgelogic.ParameterObjectAttribute()
    PAR0000.value = 30.0
    PAR0001.value = 0.15000000596046448
    ACT0003.condition = CON0004
    ACT0003.xyz = {'x': True, 'y': True, 'z': True}
    ACT0003.game_object = PAR0002
    ACT0003.attribute_value = PAR0005
    ACT0003.value_type = 'worldPosition'
    PAR0005.op = 'lerp'
    PAR0005.vector = PAR0007
    PAR0005.vector_2 = PAR0006.OUTV
    PAR0005.factor = PAR0001
    PAR0006.input_x = PAR0009
    PAR0006.input_y = PAR0008.OUTY
    PAR0006.input_z = PAR0010
    PAR0007.game_object = PAR0002
    PAR0007.attribute_name = "worldPosition"
    PAR0008.input_v = PAR0011
    PAR0009.operator = bgelogic.ParameterArithmeticOp.op_by_code("ADD")
    PAR0009.operand_a = PAR0008.OUTX
    PAR0009.operand_b = PAR0000
    PAR0010.operator = bgelogic.ParameterArithmeticOp.op_by_code("ADD")
    PAR0010.operand_a = PAR0008.OUTZ
    PAR0010.operand_b = 1.0
    PAR0011.game_object = "NLO:U_O"
    PAR0011.attribute_name = "worldPosition"
    network.add_cell(PAR0000)
    network.add_cell(PAR0002)
    network.add_cell(CON0004)
    network.add_cell(PAR0007)
    network.add_cell(PAR0011)
    network.add_cell(PAR0001)
    network.add_cell(PAR0008)
    network.add_cell(PAR0010)
    network.add_cell(PAR0009)
    network.add_cell(PAR0006)
    network.add_cell(PAR0005)
    network.add_cell(ACT0003)
    owner["Player_2D_Camera"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__Player_2D_Camera')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("Player_2D_Camera")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
