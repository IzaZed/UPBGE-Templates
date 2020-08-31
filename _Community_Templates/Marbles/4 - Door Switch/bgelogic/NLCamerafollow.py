#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.ActionSetObjectAttribute()
    PAR0001 = bgelogic.ParameterObjectAttribute()
    PAR0002 = bgelogic.ParameterObjectAttribute()
    PAR0003 = bgelogic.ParameterVector3Split()
    CON0004 = bgelogic.ConditionOnUpdate()
    ACT0005 = bgelogic.ActionAddScene()
    PAR0006 = bgelogic.ParameterVector3Split()
    PAR0007 = bgelogic.ParameterVector3Simple()
    PAR0008 = bgelogic.ParameterMathFun()
    PAR0009 = bgelogic.ParameterMathFun()
    ACT0000.condition = CON0004
    ACT0000.game_object = "Object:Camera.001"
    ACT0000.attribute_value = PAR0007.OUTV
    ACT0000.value_type = 'worldPosition'
    PAR0001.game_object = "Object:Sphere"
    PAR0001.attribute_name = "worldPosition"
    PAR0002.game_object = "Object:Camera.001"
    PAR0002.attribute_name = "worldPosition"
    PAR0003.input_v = PAR0002
    ACT0005.overlay = 1
    ACT0005.condition = None
    ACT0005.scene_name = ""
    PAR0006.input_v = PAR0001
    PAR0007.input_x = PAR0006.OUTX
    PAR0007.input_y = PAR0008
    PAR0007.input_z = PAR0009
    PAR0008.formula = "a - b"
    PAR0008.a = PAR0006.OUTY
    PAR0008.b = 40.0
    PAR0009.formula = "a + b"
    PAR0009.a = PAR0006.OUTZ
    PAR0009.b = 20.0
    network.add_cell(PAR0001)
    network.add_cell(CON0004)
    network.add_cell(PAR0006)
    network.add_cell(PAR0008)
    network.add_cell(PAR0002)
    network.add_cell(ACT0005)
    network.add_cell(PAR0009)
    network.add_cell(PAR0003)
    network.add_cell(PAR0007)
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
