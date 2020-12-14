# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.ActionSetObjectAttribute()
    CON0001 = bgelogic.ConditionOnUpdate()
    PAR0002 = bgelogic.ParameterVector3Split()
    PAR0003 = bgelogic.ParameterArithmeticOp()
    PAR0004 = bgelogic.ParameterArithmeticOp()
    PAR0005 = bgelogic.ParameterObjectAttribute()
    PAR0006 = bgelogic.ParameterSimpleValue()
    PAR0007 = bgelogic.ParameterSimpleValue()
    PAR0008 = bgelogic.ParameterVector3Simple()
    PAR0009 = bgelogic.ParameterObjectAttribute()
    PAR0010 = bgelogic.ParameterVectorMath()
    PAR0011 = bgelogic.ParameterActiveCamera()
    ACT0000.condition = CON0001
    ACT0000.xyz = {'x': True, 'y': True, 'z': True}
    ACT0000.game_object = PAR0011
    ACT0000.attribute_value = PAR0010
    ACT0000.value_type = 'worldPosition'
    PAR0002.input_v = PAR0005
    PAR0003.operator = bgelogic.ParameterArithmeticOp.op_by_code("ADD")
    PAR0003.operand_a = PAR0002.OUTX
    PAR0003.operand_b = PAR0006
    PAR0004.operator = bgelogic.ParameterArithmeticOp.op_by_code("ADD")
    PAR0004.operand_a = PAR0002.OUTZ
    PAR0004.operand_b = 1.0
    PAR0005.game_object = "NLO:U_O"
    PAR0005.attribute_name = "worldPosition"
    PAR0006.value = 30.0
    PAR0007.value = 0.15000000596046448
    PAR0008.input_x = PAR0003
    PAR0008.input_y = PAR0002.OUTY
    PAR0008.input_z = PAR0004
    PAR0009.game_object = PAR0011
    PAR0009.attribute_name = "worldPosition"
    PAR0010.op = 'lerp'
    PAR0010.vector = PAR0009
    PAR0010.vector_2 = PAR0008.OUTV
    PAR0010.factor = PAR0007
    network.add_cell(CON0001)
    network.add_cell(PAR0005)
    network.add_cell(PAR0007)
    network.add_cell(PAR0011)
    network.add_cell(PAR0002)
    network.add_cell(PAR0004)
    network.add_cell(PAR0009)
    network.add_cell(PAR0006)
    network.add_cell(PAR0003)
    network.add_cell(PAR0008)
    network.add_cell(PAR0010)
    network.add_cell(ACT0000)
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
