#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    PAR0000 = bgelogic.ParameterObjectAttribute()
    CON0001 = bgelogic.ConditionOnUpdate()
    ACT0002 = bgelogic.ActionSetObjectAttribute()
    PAR0003 = bgelogic.ParameterVector3Simple()
    PAR0004 = bgelogic.ParameterMathFun()
    ACT0005 = bgelogic.ActionSetObjectAttribute()
    PAR0006 = bgelogic.ParameterObjectProperty()
    PAR0007 = bgelogic.ParameterVector3Simple()
    PAR0008 = bgelogic.ParameterVector3Split()
    PAR0009 = bgelogic.ParameterVector3Split()
    PAR0000.game_object = "Object:Sphere"
    PAR0000.attribute_name = "worldPosition"
    ACT0002.condition = CON0001
    ACT0002.game_object = "Object:HP"
    ACT0002.attribute_value = PAR0003.OUTV
    ACT0002.value_type = 'worldPosition'
    PAR0003.input_x = PAR0009.OUTX
    PAR0003.input_y = PAR0009.OUTY
    PAR0003.input_z = PAR0004
    PAR0004.formula = "a + b"
    PAR0004.a = PAR0009.OUTZ
    PAR0004.b = 3.0
    ACT0005.condition = ACT0002.OUT
    ACT0005.game_object = "Object:HP"
    ACT0005.attribute_value = PAR0007.OUTV
    ACT0005.value_type = 'localScale'
    PAR0006.game_object = "Object:Sphere"
    PAR0006.property_name = "HP"
    PAR0007.input_x = PAR0006
    PAR0007.input_y = PAR0008.OUTY
    PAR0007.input_z = PAR0008.OUTZ
    PAR0008.input_v = mathutils.Vector((0.0, 1.0, 1.0))
    PAR0009.input_v = PAR0000
    network.add_cell(PAR0000)
    network.add_cell(PAR0006)
    network.add_cell(PAR0008)
    network.add_cell(CON0001)
    network.add_cell(PAR0007)
    network.add_cell(PAR0009)
    network.add_cell(PAR0004)
    network.add_cell(PAR0003)
    network.add_cell(ACT0002)
    network.add_cell(ACT0005)
    owner["Healtbar"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__Healtbar')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("Healtbar")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
