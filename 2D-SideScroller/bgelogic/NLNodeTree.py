# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
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
