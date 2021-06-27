# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    owner["IGNLTree_FPS_AI"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__FPS_AI')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_FPS_AI")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
