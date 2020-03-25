#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    PAR0000 = bgelogic.ParameterVector3Simple()
    CON0001 = bgelogic.ConditionKeyPressed()
    ACT0002 = bgelogic.ActionApplyForce()
    PAR0003 = bgelogic.ParameterVector3Simple()
    CON0004 = bgelogic.ConditionKeyPressed()
    PAR0005 = bgelogic.ParameterVector3Simple()
    CON0006 = bgelogic.ConditionKeyPressed()
    PAR0007 = bgelogic.ParameterVector3Simple()
    CON0008 = bgelogic.ConditionKeyPressed()
    ACT0009 = bgelogic.ActionApplyForce()
    ACT0010 = bgelogic.ActionApplyForce()
    ACT0011 = bgelogic.InvertValue()
    ACT0012 = bgelogic.ActionApplyForce()
    PAR0013 = bgelogic.ParameterSimpleValue()
    PAR0000.input_x = 0.0
    PAR0000.input_y = ACT0011.OUT
    PAR0000.input_z = 0.0
    CON0001.key_code = bge.events.WKEY
    CON0001.pulse = True
    ACT0002.local = False
    ACT0002.condition = CON0001
    ACT0002.game_object = "Object:Sphere"
    ACT0002.force = PAR0005.OUTV
    PAR0003.input_x = ACT0011.OUT
    PAR0003.input_y = 0.0
    PAR0003.input_z = 0.0
    CON0004.key_code = bge.events.SKEY
    CON0004.pulse = True
    PAR0005.input_x = PAR0013
    PAR0005.input_y = 0.0
    PAR0005.input_z = 0.0
    CON0006.key_code = bge.events.AKEY
    CON0006.pulse = True
    PAR0007.input_x = 0.0
    PAR0007.input_y = PAR0013
    PAR0007.input_z = 0.0
    CON0008.key_code = bge.events.DKEY
    CON0008.pulse = True
    ACT0009.local = False
    ACT0009.condition = CON0006
    ACT0009.game_object = "Object:Sphere"
    ACT0009.force = PAR0007.OUTV
    ACT0010.local = False
    ACT0010.condition = CON0004
    ACT0010.game_object = "Object:Sphere"
    ACT0010.force = PAR0003.OUTV
    ACT0011.value = PAR0013
    ACT0012.local = False
    ACT0012.condition = CON0008
    ACT0012.game_object = "Object:Sphere"
    ACT0012.force = PAR0000.OUTV
    PAR0013.value = 10.0
    network.add_cell(CON0001)
    network.add_cell(CON0004)
    network.add_cell(CON0006)
    network.add_cell(CON0008)
    network.add_cell(PAR0013)
    network.add_cell(PAR0005)
    network.add_cell(ACT0011)
    network.add_cell(PAR0000)
    network.add_cell(PAR0003)
    network.add_cell(ACT0010)
    network.add_cell(ACT0002)
    network.add_cell(ACT0012)
    network.add_cell(PAR0007)
    network.add_cell(ACT0009)
    owner["BallControls"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__BallControls')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("BallControls")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
