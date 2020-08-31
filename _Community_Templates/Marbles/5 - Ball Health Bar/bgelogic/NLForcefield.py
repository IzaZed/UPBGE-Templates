#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.ActionSetGameObjectGameProperty()
    PAR0001 = bgelogic.ParameterMathFun()
    PAR0002 = bgelogic.ParameterObjectProperty()
    CON0003 = bgelogic.ConditionCollision()
    PAR0004 = bgelogic.ParameterObjectAttribute()
    PAR0005 = bgelogic.ParameterObjectAttribute()
    CON0006 = bgelogic.ConditionLogicOp()
    CON0007 = bgelogic.ConditionAnd()
    PAR0008 = bgelogic.ClampValue()
    ACT0000.condition = CON0007
    ACT0000.game_object = "Object:Sphere"
    ACT0000.property_name = "HP"
    ACT0000.property_value = PAR0008
    PAR0001.formula = "a - b"
    PAR0001.a = PAR0002
    PAR0001.b = 0.009999999776482582
    PAR0002.game_object = "Object:Sphere"
    PAR0002.property_name = "HP"
    CON0003.game_object = "Object:Trigger"
    PAR0004.game_object = "Object:Sphere"
    PAR0004.attribute_name = "name"
    PAR0005.game_object = CON0003.TARGET
    PAR0005.attribute_name = "name"
    CON0006.param_a = PAR0005
    CON0006.param_b = PAR0004
    CON0006.operator = 0
    CON0007.condition_a = CON0003
    CON0007.condition_b = CON0006
    PAR0008.value = PAR0001
    PAR0008.range = mathutils.Vector((0.0, 10.0))
    network.add_cell(PAR0002)
    network.add_cell(PAR0004)
    network.add_cell(PAR0001)
    network.add_cell(PAR0008)
    network.add_cell(CON0003)
    network.add_cell(PAR0005)
    network.add_cell(CON0006)
    network.add_cell(CON0007)
    network.add_cell(ACT0000)
    owner["Force field"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__Force field')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("Force field")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
