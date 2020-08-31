# MACHINE GENERATED
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
    PAR0004 = bgelogic.ParamOwnerObject()
    PAR0005 = bgelogic.InterpolateValue()
    CON0006 = bgelogic.ConditionKeyPressed()
    PAR0007 = bgelogic.ParameterObjectProperty()
    CON0008 = bgelogic.ConditionOr()
    ACT0009 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0010 = bgelogic.ActionSetGameObjectGameProperty()
    CON0011 = bgelogic.ConditionNot()
    PAR0012 = bgelogic.InterpolateValue()
    ACT0013 = bgelogic.ActionSetGameObjectGameProperty()
    PAR0014 = bgelogic.InterpolateValue()
    CON0015 = bgelogic.ConditionOnUpdate()
    ACT0016 = bgelogic.VehicleApplySteering()
    PAR0017 = bgelogic.ParameterObjectProperty()
    ACT0018 = bgelogic.VehicleSetAttributes()
    CON0019 = bgelogic.ConditionKeyPressed()
    CON0020 = bgelogic.ConditionKeyPressed()
    ACT0021 = bgelogic.VehicleApplyBraking()
    ACT0022 = bgelogic.VehicleApplyForce()
    PAR0023 = bgelogic.ParameterObjectProperty()
    PAR0024 = bgelogic.ValueSwitch()
    PAR0025 = bgelogic.ParameterSimpleValue()
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
    CON0003.key_code = bge.events.AKEY
    CON0003.pulse = True
    PAR0005.value_a = PAR0007
    PAR0005.value_b = 1.0
    PAR0005.factor = PAR0025
    CON0006.key_code = bge.events.DKEY
    CON0006.pulse = True
    PAR0007.game_object = PAR0004
    PAR0007.property_name = "steering"
    CON0008.condition_a = ACT0009.OUT
    CON0008.condition_b = ACT0013.OUT
    ACT0009.condition = CON0003
    ACT0009.game_object = PAR0004
    ACT0009.property_name = "steering"
    ACT0009.property_value = PAR0005
    ACT0010.condition = CON0011
    ACT0010.game_object = PAR0004
    ACT0010.property_name = "steering"
    ACT0010.property_value = PAR0014
    CON0011.condition = CON0008
    PAR0012.value_a = PAR0007
    PAR0012.value_b = -1.0
    PAR0012.factor = PAR0025
    ACT0013.condition = CON0006
    ACT0013.game_object = PAR0004
    ACT0013.property_name = "steering"
    ACT0013.property_value = PAR0012
    PAR0014.value_a = PAR0007
    PAR0014.value_b = 0.0
    PAR0014.factor = PAR0025
    ACT0016.condition = CON0015
    ACT0016.constraint = PAR0017
    ACT0016.wheelcount = 2
    ACT0016.power = PAR0007
    ACT0016.value_type = 'FRONT'
    PAR0017.game_object = "Object:Vehicle"
    PAR0017.property_name = "vehicle_wrapper"
    ACT0018.condition = ACT0022.OUT
    ACT0018.constraint = PAR0023
    ACT0018.wheelcount = 2
    ACT0018.set_suspension_compression = False
    ACT0018.suspension_compression = 0.0
    ACT0018.set_suspension_damping = False
    ACT0018.suspension_damping = 0.0
    ACT0018.set_suspension_stiffness = False
    ACT0018.suspension_stiffness = 0.0
    ACT0018.set_tyre_friction = True
    ACT0018.tyre_friction = PAR0024.VAL
    ACT0018.value_type = 'FRONT'
    CON0019.key_code = bge.events.SKEY
    CON0019.pulse = True
    CON0020.key_code = bge.events.WKEY
    CON0020.pulse = True
    ACT0021.condition = CON0019
    ACT0021.constraint = PAR0023
    ACT0021.wheelcount = 85
    ACT0021.power = 0.07000000029802322
    ACT0021.value_type = 'ALL'
    ACT0022.condition = CON0020
    ACT0022.constraint = PAR0023
    ACT0022.wheelcount = 2
    ACT0022.power = 3.0
    ACT0022.value_type = 'REAR'
    PAR0023.game_object = "Object:Vehicle"
    PAR0023.property_name = "vehicle_wrapper"
    PAR0024.condition = ACT0022.OUT
    PAR0024.val_a = 2.0
    PAR0024.val_b = 10.0
    PAR0025.value = 0.05000000074505806
    network.add_cell(CON0000)
    network.add_cell(ACT0002)
    network.add_cell(PAR0004)
    network.add_cell(CON0006)
    network.add_cell(CON0015)
    network.add_cell(PAR0017)
    network.add_cell(CON0019)
    network.add_cell(PAR0023)
    network.add_cell(PAR0025)
    network.add_cell(ACT0001)
    network.add_cell(PAR0007)
    network.add_cell(PAR0012)
    network.add_cell(PAR0014)
    network.add_cell(CON0020)
    network.add_cell(ACT0022)
    network.add_cell(CON0003)
    network.add_cell(ACT0013)
    network.add_cell(ACT0021)
    network.add_cell(PAR0005)
    network.add_cell(ACT0009)
    network.add_cell(ACT0016)
    network.add_cell(PAR0024)
    network.add_cell(CON0008)
    network.add_cell(CON0011)
    network.add_cell(ACT0010)
    network.add_cell(ACT0018)
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
