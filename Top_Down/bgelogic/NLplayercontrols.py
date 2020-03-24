#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.ActionNavigateWithNavmesh()
    CON0001 = bgelogic.ConditionOnUpdate()
    PAR0002 = bgelogic.ParameterObjectProperty()
    ACT0000.condition = CON0001
    ACT0000.moving_object = "Object:Player"
    ACT0000.rotating_object = "Object:Player"
    ACT0000.navmesh_object = "Object:Navmesh"
    ACT0000.destination_point = PAR0002
    ACT0000.move_dynamic = False
    ACT0000.linear_speed = 10.0
    ACT0000.reach_threshold = 1.0
    ACT0000.look_at = True
    ACT0000.rot_axis = 0
    ACT0000.front_axis = 0
    ACT0000.rot_speed = 1.0
    PAR0002.game_object = "Object:Player"
    PAR0002.property_name = "aim"
    network.add_cell(CON0001)
    network.add_cell(PAR0002)
    network.add_cell(ACT0000)
    owner["player_controls"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__player_controls')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("player_controls")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
