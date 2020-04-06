#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionCollision()
    PAR0001 = bgelogic.ParameterObjectAttribute()
    PAR0002 = bgelogic.ParameterObjectAttribute()
    CON0003 = bgelogic.ConditionLogicOp()
    CON0004 = bgelogic.ConditionAnd()
    ACT0005 = bgelogic.ActionPlayAction()
    CON0000.game_object = "Object:Cube.001"
    PAR0001.game_object = "Object:Sphere"
    PAR0001.attribute_name = "name"
    PAR0002.game_object = CON0000.TARGET
    PAR0002.attribute_name = "name"
    CON0003.param_a = PAR0002
    CON0003.param_b = PAR0001
    CON0003.operator = 0
    CON0004.condition_a = CON0000
    CON0004.condition_b = CON0003
    ACT0005.condition = CON0004
    ACT0005.game_object = "Object:Door"
    ACT0005.action_name = "Door3"
    ACT0005.stop = True
    ACT0005.start_frame = 0.0
    ACT0005.end_frame = 240.0
    ACT0005.layer = 0
    ACT0005.priority = 0
    ACT0005.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0005.layer_weight = 1.0
    ACT0005.speed = 1.0
    ACT0005.blendin = 0.0
    ACT0005.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    network.add_cell(CON0000)
    network.add_cell(PAR0002)
    network.add_cell(PAR0001)
    network.add_cell(CON0003)
    network.add_cell(CON0004)
    network.add_cell(ACT0005)
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
