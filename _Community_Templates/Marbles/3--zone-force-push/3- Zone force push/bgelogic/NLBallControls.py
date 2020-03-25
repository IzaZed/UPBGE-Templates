#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionKeyPressed()
    ACT0001 = bgelogic.ActionApplyForce()
    CON0002 = bgelogic.ConditionKeyPressed()
    ACT0003 = bgelogic.ActionApplyForce()
    PAR0004 = bgelogic.ParameterVector3Simple()
    CON0005 = bgelogic.ConditionKeyPressed()
    PAR0006 = bgelogic.ParameterVector3Simple()
    CON0007 = bgelogic.ConditionKeyPressed()
    PAR0008 = bgelogic.ParameterVector3Simple()
    ACT0009 = bgelogic.ActionApplyForce()
    ACT0010 = bgelogic.ActionApplyForce()
    PAR0011 = bgelogic.ParameterVector3Simple()
    PAR0012 = bgelogic.ParameterMathFun()
    PAR0013 = bgelogic.ParameterSimpleValue()
    CON0000.key_code = bge.events.DKEY
    CON0000.pulse = True
    ACT0001.local = False
    ACT0001.condition = CON0000
    ACT0001.game_object = "Object:Sphere"
    ACT0001.force = PAR0011.OUTV
    CON0002.key_code = bge.events.QKEY
    CON0002.pulse = True
    ACT0003.local = False
    ACT0003.condition = CON0002
    ACT0003.game_object = "Object:Sphere"
    ACT0003.force = PAR0004.OUTV
    PAR0004.input_x = PAR0012
    PAR0004.input_y = 0.0
    PAR0004.input_z = 0.0
    CON0005.key_code = bge.events.ZKEY
    CON0005.pulse = True
    PAR0006.input_x = 0.0
    PAR0006.input_y = PAR0013
    PAR0006.input_z = 0.0
    CON0007.key_code = bge.events.SKEY
    CON0007.pulse = True
    PAR0008.input_x = 0.0
    PAR0008.input_y = PAR0012
    PAR0008.input_z = 0.0
    ACT0009.local = False
    ACT0009.condition = CON0007
    ACT0009.game_object = "Object:Sphere"
    ACT0009.force = PAR0008.OUTV
    ACT0010.local = False
    ACT0010.condition = CON0005
    ACT0010.game_object = "Object:Sphere"
    ACT0010.force = PAR0006.OUTV
    PAR0011.input_x = PAR0013
    PAR0011.input_y = 0.0
    PAR0011.input_z = 0.0
    PAR0012.formula = "a * b"
    PAR0012.a = PAR0013
    PAR0012.b = -1.0
    PAR0013.value = 10.0
    network.add_cell(CON0000)
    network.add_cell(CON0002)
    network.add_cell(CON0005)
    network.add_cell(CON0007)
    network.add_cell(PAR0013)
    network.add_cell(PAR0006)
    network.add_cell(ACT0010)
    network.add_cell(PAR0012)
    network.add_cell(PAR0004)
    network.add_cell(PAR0011)
    network.add_cell(ACT0001)
    network.add_cell(PAR0008)
    network.add_cell(ACT0003)
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
