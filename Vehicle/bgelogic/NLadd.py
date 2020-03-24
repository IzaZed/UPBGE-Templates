#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionOnInit()
    ACT0001 = bgelogic.ActionCreateVehicle()
    ACT0002 = bgelogic.ActionSetGameObjectGameProperty()
    CON0003 = bgelogic.ConditionKeyPressed()
    ACT0004 = bgelogic.VehicleApplyForce()
    CON0005 = bgelogic.ConditionKeyPressed()
    PAR0006 = bgelogic.ParameterObjectProperty()
    ACT0007 = bgelogic.VehicleApplyBraking()
    ACT0001.condition = CON0000
    ACT0001.game_object = "Object:Vehicle"
    ACT0001.wheels_steering = 'front_wheels'
    ACT0001.wheels = 'rear_wheels'
    ACT0001.suspension = 0.05999999865889549
    ACT0001.stiffness = 50.0
    ACT0001.damping = 5.0
    ACT0001.friction = 2.0
    ACT0002.condition = ACT0001.OUT
    ACT0002.game_object = "Object:Vehicle"
    ACT0002.property_name = "vehicle_wrapper"
    ACT0002.property_value = ACT0001.VEHICLE
    CON0003.key_code = bge.events.WKEY
    CON0003.pulse = True
    ACT0004.condition = CON0003
    ACT0004.constraint = PAR0006
    ACT0004.wheelcount = 2
    ACT0004.power = 5.0
    ACT0004.value_type = 'FRONT'
    CON0005.key_code = bge.events.SKEY
    CON0005.pulse = True
    PAR0006.game_object = "Object:Vehicle"
    PAR0006.property_name = "vehicle_wrapper"
    ACT0007.condition = CON0005
    ACT0007.constraint = PAR0006
    ACT0007.wheelcount = 85
    ACT0007.power = 0.07000000029802322
    ACT0007.value_type = 'ALL'
    network.add_cell(CON0000)
    network.add_cell(CON0003)
    network.add_cell(CON0005)
    network.add_cell(ACT0001)
    network.add_cell(PAR0006)
    network.add_cell(ACT0002)
    network.add_cell(ACT0007)
    network.add_cell(ACT0004)
    owner["add"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__add')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("add")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
