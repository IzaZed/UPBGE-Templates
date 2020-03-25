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
    PAR0006 = bgelogic.ParameterMathFun()
    CON0007 = bgelogic.ConditionOnUpdate()
    CON0008 = bgelogic.ConditionOnUpdate()
    ACT0009 = bgelogic.ActionAddScene()
    ACT0010 = bgelogic.ActionAddScene()
    ACT0000.condition = CON0007
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
    PAR0005.input_y = PAR0006
    PAR0005.input_z = PAR0004.OUTZ
    PAR0006.formula = "a - b"
    PAR0006.a = PAR0001.OUTY
    PAR0006.b = 40.0
    ACT0009.overlay = 1
    ACT0009.condition = None
    ACT0009.scene_name = ""
    ACT0010.overlay = 1
    ACT0010.condition = CON0008
    ACT0010.scene_name = "HUD"
    network.add_cell(PAR0002)
    network.add_cell(CON0007)
    network.add_cell(ACT0009)
    network.add_cell(PAR0001)
    network.add_cell(PAR0006)
    network.add_cell(PAR0003)
    network.add_cell(CON0008)
    network.add_cell(PAR0004)
    network.add_cell(ACT0010)
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
