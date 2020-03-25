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
    ACT0003 = bgelogic.VehicleApplyBraking()
    ACT0004 = bgelogic.VehicleApplyForce()
    PAR0005 = bgelogic.ParameterObjectProperty()
    CON0006 = bgelogic.ConditionKeyPressed()
    CON0007 = bgelogic.ConditionKeyPressed()
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
    ACT0003.condition = CON0006
    ACT0003.constraint = PAR0005
    ACT0003.wheelcount = 85
    ACT0003.power = 0.07000000029802322
    ACT0003.value_type = 'ALL'
    ACT0004.condition = CON0007
    ACT0004.constraint = PAR0005
    ACT0004.wheelcount = 2
    ACT0004.power = 5.0
    ACT0004.value_type = 'FRONT'
    PAR0005.game_object = "Object:Vehicle"
    PAR0005.property_name = "vehicle_wrapper"
    CON0006.key_code = bge.events.SKEY
    CON0006.pulse = True
    CON0007.key_code = bge.events.WKEY
    CON0007.pulse = True
    network.add_cell(CON0000)
    network.add_cell(ACT0002)
    network.add_cell(PAR0005)
    network.add_cell(CON0007)
    network.add_cell(ACT0001)
    network.add_cell(ACT0004)
    network.add_cell(CON0006)
    network.add_cell(ACT0003)
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
