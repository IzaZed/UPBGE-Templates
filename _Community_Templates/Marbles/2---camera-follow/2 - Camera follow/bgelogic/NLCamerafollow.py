#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.ActionSetObjectAttribute()
    PAR0001 = bgelogic.ParameterVector3Split()
    PAR0002 = bgelogic.ParameterObjectAttribute()
    PAR0003 = bgelogic.ParameterObjectAttribute()
    PAR0004 = bgelogic.ParameterVector3Split()
    PAR0005 = bgelogic.ParameterVector3Simple()
    CON0006 = bgelogic.ConditionOnUpdate()
    PAR0007 = bgelogic.ParameterMathFun()
    PAR0008 = bgelogic.ParameterArithmeticOp()
    ACT0000.condition = CON0006
    ACT0000.game_object = "Object:Camera.001"
    ACT0000.attribute_value = PAR0005.OUTV
    ACT0000.value_type = 'worldPosition'
    PAR0001.input_v = PAR0002
    PAR0002.game_object = "Object:Sphere"
    PAR0002.attribute_name = "worldPosition"
    PAR0003.game_object = "Object:Camera.001"
    PAR0003.attribute_name = "worldPosition"
    PAR0004.input_v = PAR0003
    PAR0005.input_x = PAR0001.OUTX
    PAR0005.input_y = PAR0007
    PAR0005.input_z = PAR0004.OUTZ
    PAR0007.formula = "a - b"
    PAR0007.a = PAR0001.OUTY
    PAR0007.b = 40.0
    PAR0008.operator = bgelogic.ParameterArithmeticOp.op_by_code("ADD")
    PAR0008.operand_a = 0.0
    PAR0008.operand_b = 0.0
    network.add_cell(PAR0002)
    network.add_cell(CON0006)
    network.add_cell(PAR0008)
    network.add_cell(PAR0001)
    network.add_cell(PAR0007)
    network.add_cell(PAR0003)
    network.add_cell(PAR0004)
    network.add_cell(PAR0005)
    network.add_cell(ACT0000)
    owner["Camera follow"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__Camera follow')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("Camera follow")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
