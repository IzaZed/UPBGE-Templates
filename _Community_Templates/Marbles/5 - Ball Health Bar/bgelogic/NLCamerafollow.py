#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.ActionAddScene()
    ACT0001 = bgelogic.ActionSetObjectAttribute()
    PAR0002 = bgelogic.ParameterObjectAttribute()
    PAR0003 = bgelogic.ParameterObjectAttribute()
    PAR0004 = bgelogic.ParameterVector3Split()
    CON0005 = bgelogic.ConditionOnUpdate()
    PAR0006 = bgelogic.ParameterVector3Split()
    PAR0007 = bgelogic.ParameterMathFun()
    PAR0008 = bgelogic.ParameterMathFun()
    PAR0009 = bgelogic.ParameterVector3Simple()
    ACT0000.overlay = 1
    ACT0000.condition = None
    ACT0000.scene_name = ""
    ACT0001.condition = CON0005
    ACT0001.game_object = "Object:Camera.001"
    ACT0001.attribute_value = PAR0009.OUTV
    ACT0001.value_type = 'worldPosition'
    PAR0002.game_object = "Object:Sphere"
    PAR0002.attribute_name = "worldPosition"
    PAR0003.game_object = "Object:Camera.001"
    PAR0003.attribute_name = "worldPosition"
    PAR0004.input_v = PAR0003
    PAR0006.input_v = PAR0002
    PAR0007.formula = "a + b"
    PAR0007.a = PAR0006.OUTZ
    PAR0007.b = 20.0
    PAR0008.formula = "a - b"
    PAR0008.a = PAR0006.OUTY
    PAR0008.b = 40.0
    PAR0009.input_x = PAR0006.OUTX
    PAR0009.input_y = PAR0008
    PAR0009.input_z = PAR0007
    network.add_cell(ACT0000)
    network.add_cell(PAR0002)
    network.add_cell(CON0005)
    network.add_cell(PAR0003)
    network.add_cell(PAR0006)
    network.add_cell(PAR0008)
    network.add_cell(PAR0004)
    network.add_cell(PAR0007)
    network.add_cell(PAR0009)
    network.add_cell(ACT0001)
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
