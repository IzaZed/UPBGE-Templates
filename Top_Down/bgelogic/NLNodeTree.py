#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.ActionMousePick()
    ACT0001 = bgelogic.ActionSetObjectAttribute()
    CON0002 = bgelogic.ConditionMousePressed()
    ACT0000.condition = CON0002
    ACT0000.camera = "Object:Camera"
    ACT0000.property = "ground"
    ACT0000.distance = 100.0
    ACT0001.condition = ACT0000
    ACT0001.game_object = "Object:Torus"
    ACT0001.attribute_value = ACT0000.OUTPOINT
    ACT0001.value_type = 'worldPosition'
    CON0002.mouse_button_code = bge.events.LEFTMOUSE
    CON0002.pulse = False
    network.add_cell(CON0002)
    network.add_cell(ACT0000)
    network.add_cell(ACT0001)
    owner["NodeTree"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__NodeTree')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("NodeTree")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
