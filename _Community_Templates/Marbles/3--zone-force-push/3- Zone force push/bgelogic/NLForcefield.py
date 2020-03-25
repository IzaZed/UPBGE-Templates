#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    PAR0000 = bgelogic.ParameterObjectAttribute()
    PAR0001 = bgelogic.ParameterObjectAttribute()
    CON0002 = bgelogic.ConditionCollision()
    CON0003 = bgelogic.ConditionLogicOp()
    ACT0004 = bgelogic.ActionApplyForce()
    PAR0000.game_object = "Object:Sphere"
    PAR0000.attribute_name = "name"
    PAR0001.game_object = CON0002.TARGET
    PAR0001.attribute_name = "name"
    CON0002.game_object = "Object:Cube.001"
    CON0003.param_a = PAR0001
    CON0003.param_b = PAR0000
    CON0003.operator = 0
    ACT0004.local = False
    ACT0004.condition = CON0003
    ACT0004.game_object = "Object:Sphere"
    ACT0004.force = mathutils.Vector((0.0, 0.0, 20.0))
    network.add_cell(PAR0000)
    network.add_cell(CON0002)
    network.add_cell(PAR0001)
    network.add_cell(CON0003)
    network.add_cell(ACT0004)
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
