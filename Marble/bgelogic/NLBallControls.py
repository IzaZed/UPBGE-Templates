# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.InvertValue()
    PAR0001 = bgelogic.ParameterVector3Simple()
    CON0002 = bgelogic.ConditionKeyPressed()
    CON0003 = bgelogic.ConditionKeyPressed()
    PAR0004 = bgelogic.ParameterVector3Simple()
    CON0005 = bgelogic.ConditionKeyPressed()
    ACT0006 = bgelogic.ActionApplyTorque()
    ACT0007 = bgelogic.ActionApplyTorque()
    ACT0008 = bgelogic.ActionApplyTorque()
    ACT0009 = bgelogic.ActionApplyTorque()
    CON0010 = bgelogic.ConditionKeyPressed()
    ACT0011 = bgelogic.ActionPrint()
    PAR0012 = bgelogic.ParameterVector3Simple()
    PAR0013 = bgelogic.ParameterVector3Simple()
    PAR0014 = bgelogic.ParameterSimpleValue()
    ACT0000.value = PAR0014
    PAR0001.input_x = PAR0014
    PAR0001.input_y = 0.0
    PAR0001.input_z = 0.0
    CON0002.key_code = bge.events.SKEY
    CON0002.pulse = True
    CON0003.key_code = bge.events.AKEY
    CON0003.pulse = True
    PAR0004.input_x = ACT0000.OUT
    PAR0004.input_y = 0.0
    PAR0004.input_z = 0.0
    CON0005.key_code = bge.events.DKEY
    CON0005.pulse = True
    ACT0006.local = False
    ACT0006.condition = CON0002
    ACT0006.game_object = "NLO:Sphere"
    ACT0006.torque = PAR0013.OUTV
    ACT0007.local = False
    ACT0007.condition = CON0003
    ACT0007.game_object = "NLO:Sphere"
    ACT0007.torque = PAR0004.OUTV
    ACT0008.local = False
    ACT0008.condition = CON0005
    ACT0008.game_object = "NLO:Sphere"
    ACT0008.torque = PAR0001.OUTV
    ACT0009.local = False
    ACT0009.condition = CON0010
    ACT0009.game_object = "NLO:Sphere"
    ACT0009.torque = PAR0012.OUTV
    CON0010.key_code = bge.events.WKEY
    CON0010.pulse = True
    ACT0011.condition = False
    ACT0011.value = ""
    PAR0012.input_x = 0.0
    PAR0012.input_y = PAR0014
    PAR0012.input_z = 0.0
    PAR0013.input_x = 0.0
    PAR0013.input_y = ACT0000.OUT
    PAR0013.input_z = 0.0
    PAR0014.value = 5.0
    network.add_cell(CON0002)
    network.add_cell(CON0005)
    network.add_cell(CON0010)
    network.add_cell(PAR0014)
    network.add_cell(ACT0000)
    network.add_cell(CON0003)
    network.add_cell(ACT0011)
    network.add_cell(PAR0013)
    network.add_cell(PAR0001)
    network.add_cell(ACT0006)
    network.add_cell(ACT0008)
    network.add_cell(PAR0012)
    network.add_cell(PAR0004)
    network.add_cell(ACT0009)
    network.add_cell(ACT0007)
    owner["IGNLTree_BallControls"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__BallControls')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_BallControls")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
