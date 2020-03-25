#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionOnInit()
    ACT0001 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0002 = bgelogic.ActionCreateVehicle()
    CON0003 = bgelogic.ConditionKeyPressed()
    CON0004 = bgelogic.ConditionKeyPressed()
    PAR0005 = bgelogic.ParameterObjectProperty()
    ACT0006 = bgelogic.VehicleApplyForce()
    ACT0007 = bgelogic.VehicleApplyBraking()
    ACT0001.condition = ACT0002.OUT
    ACT0001.game_object = "Object:Vehicle"
    ACT0001.property_name = "vehicle_wrapper"
    ACT0001.property_value = ACT0002.VEHICLE
    ACT0002.condition = CON0000
    ACT0002.game_object = "Object:Vehicle"
    ACT0002.wheels_steering = 'front_wheels'
    ACT0002.wheels = 'rear_wheels'
    ACT0002.suspension = 0.05999999865889549
    ACT0002.stiffness = 50.0
    ACT0002.damping = 5.0
    ACT0002.friction = 2.0
    CON0003.key_code = bge.events.WKEY
    CON0003.pulse = True
    CON0004.key_code = bge.events.SKEY
    CON0004.pulse = True
    PAR0005.game_object = "Object:Vehicle"
    PAR0005.property_name = "vehicle_wrapper"
    ACT0006.condition = CON0003
    ACT0006.constraint = PAR0005
    ACT0006.wheelcount = 2
    ACT0006.power = 5.0
    ACT0006.value_type = 'FRONT'
    ACT0007.condition = CON0004
    ACT0007.constraint = PAR0005
    ACT0007.wheelcount = 85
    ACT0007.power = 0.07000000029802322
    ACT0007.value_type = 'ALL'
    network.add_cell(CON0000)
    network.add_cell(ACT0002)
    network.add_cell(CON0004)
    network.add_cell(ACT0001)
    network.add_cell(PAR0005)
    network.add_cell(ACT0007)
    network.add_cell(CON0003)
    network.add_cell(ACT0006)
    owner["Vehicle"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__Vehicle')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("Vehicle")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
