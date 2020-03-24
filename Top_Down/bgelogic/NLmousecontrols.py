#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionMousePressed()
    CON0001 = bgelogic.ConditionOnInit()
    ACT0002 = bgelogic.ActionSetObjectAttribute()
    ACT0003 = bgelogic.ActionMousePick()
    ACT0004 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0005 = bgelogic.ActionSetGameObjectGameProperty()
    PAR0006 = bgelogic.ParameterObjectAttribute()
    ACT0007 = bgelogic.ActionSetMouseCursorVisibility()
    CON0000.mouse_button_code = bge.events.LEFTMOUSE
    CON0000.pulse = True
    ACT0002.condition = ACT0003
    ACT0002.game_object = "Object:Aimer"
    ACT0002.attribute_value = ACT0003.OUTPOINT
    ACT0002.value_type = 'worldPosition'
    ACT0003.condition = CON0000
    ACT0003.camera = "Object:Camera"
    ACT0003.property = "ground"
    ACT0003.distance = 100.0
    ACT0004.condition = ACT0002.OUT
    ACT0004.game_object = "Object:Player"
    ACT0004.property_name = "aim"
    ACT0004.property_value = ACT0003.OUTPOINT
    ACT0005.condition = ACT0007.OUT
    ACT0005.game_object = "Object:Player"
    ACT0005.property_name = "aim"
    ACT0005.property_value = PAR0006
    PAR0006.game_object = "Object:Aimer"
    PAR0006.attribute_name = "worldPosition"
    ACT0007.condition = CON0001
    ACT0007.visibility_status = True
    network.add_cell(CON0000)
    network.add_cell(ACT0003)
    network.add_cell(PAR0006)
    network.add_cell(CON0001)
    network.add_cell(ACT0007)
    network.add_cell(ACT0002)
    network.add_cell(ACT0005)
    network.add_cell(ACT0004)
    owner["mouse_controls"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__mouse_controls')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("mouse_controls")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
