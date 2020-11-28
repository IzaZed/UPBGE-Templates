# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionKeyPressed()
    ACT0001 = bgelogic.ActionApplyLocation()
    ACT0002 = bgelogic.ActionApplyLocation()
    PAR0003 = bgelogic.ParameterVector3Simple()
    PAR0004 = bgelogic.ParameterVector3Simple()
    PAR0005 = bgelogic.ParameterSimpleValue()
    ACT0006 = bgelogic.InvertValue()
    CON0007 = bgelogic.ConditionKeyPressed()
    CON0008 = bgelogic.ConditionKeyPressed()
    CON0009 = bgelogic.ConditionAnd()
    PAR0010 = bgelogic.ParameterObjectProperty()
    CON0011 = bgelogic.ConditionAnd()
    CON0012 = bgelogic.ConditionCollision()
    PAR0013 = bgelogic.ParameterObjectHasProperty()
    ACT0014 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0015 = bgelogic.ActionApplyForce()
    ACT0016 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0017 = bgelogic.ActionApplyRotation()
    CON0018 = bgelogic.ConditionOnUpdate()
    CON0000.key_code = bge.events.AKEY
    CON0000.pulse = True
    ACT0001.local = True
    ACT0001.condition = CON0007
    ACT0001.game_object = "NLO:Cube.001"
    ACT0001.movement = PAR0004.OUTV
    ACT0002.local = True
    ACT0002.condition = CON0000
    ACT0002.game_object = "NLO:Cube.001"
    ACT0002.movement = PAR0003.OUTV
    PAR0003.input_x = 0.0
    PAR0003.input_y = ACT0006.OUT
    PAR0003.input_z = 0.0
    PAR0004.input_x = 0.0
    PAR0004.input_y = PAR0005
    PAR0004.input_z = 0.0
    PAR0005.value = 0.03999999910593033
    ACT0006.value = PAR0005
    CON0007.key_code = bge.events.DKEY
    CON0007.pulse = True
    CON0008.key_code = bge.events.SPACEKEY
    CON0008.pulse = False
    CON0009.condition_a = CON0008
    CON0009.condition_b = PAR0010
    PAR0010.game_object = "NLO:Cube.001"
    PAR0010.property_name = "grounded"
    CON0011.condition_a = CON0012
    CON0011.condition_b = PAR0013
    CON0012.game_object = "NLO:Cube.001"
    CON0012.pulse = False
    PAR0013.game_object = CON0012.TARGET
    PAR0013.property_name = "ground"
    ACT0014.condition = CON0011
    ACT0014.game_object = "NLO:Cube.001"
    ACT0014.property_name = "grounded"
    ACT0014.property_value = True
    ACT0015.local = True
    ACT0015.condition = CON0009
    ACT0015.game_object = "NLO:Cube.001"
    ACT0015.force = mathutils.Vector((0.0, 0.0, 200.0))
    ACT0016.condition = ACT0015.OUT
    ACT0016.game_object = "NLO:Cube.001"
    ACT0016.property_name = "grounded"
    ACT0016.property_value = False
    ACT0017.local = True
    ACT0017.condition = CON0018
    ACT0017.game_object = "NLO:Sphere"
    ACT0017.rotation = mathutils.Vector((0.004999999888241291, 0.0, 0.0))
    network.add_cell(CON0000)
    network.add_cell(PAR0005)
    network.add_cell(CON0007)
    network.add_cell(PAR0010)
    network.add_cell(CON0012)
    network.add_cell(CON0018)
    network.add_cell(PAR0004)
    network.add_cell(CON0008)
    network.add_cell(PAR0013)
    network.add_cell(ACT0017)
    network.add_cell(ACT0001)
    network.add_cell(ACT0006)
    network.add_cell(CON0011)
    network.add_cell(PAR0003)
    network.add_cell(ACT0014)
    network.add_cell(ACT0002)
    network.add_cell(CON0009)
    network.add_cell(ACT0015)
    network.add_cell(ACT0016)
    owner["2D_Template"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__2D_Template')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("2D_Template")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
