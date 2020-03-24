#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionOnUpdate()
    ACT0001 = bgelogic.ActionRotateTo()
    ACT0002 = bgelogic.ActionMousePick()
    ACT0003 = bgelogic.ActionSetObjectAttribute()
    ACT0004 = bgelogic.ActionAlignAxisToVector()
    ACT0005 = bgelogic.ActionRotateTo()
    ACT0006 = bgelogic.ActionAlignAxisToVector()
    PAR0007 = bgelogic.ParameterObjectAttribute()
    PAR0008 = bgelogic.ParameterObjectAttribute()
    ACT0009 = bgelogic.ActionAddObject()
    CON0010 = bgelogic.ConditionMousePressed()
    ACT0011 = bgelogic.ActionSetObjectAttribute()
    PAR0012 = bgelogic.ParameterObjectAttribute()
    ACT0013 = bgelogic.ActionSetObjectAttribute()
    ACT0014 = bgelogic.ActionSetObjectAttribute()
    ACT0001.condition = CON0000
    ACT0001.moving_object = "Object:Turret"
    ACT0001.target_point = PAR0007
    ACT0001.rot_axis = 2
    ACT0001.front_axis = 1
    ACT0002.condition = CON0000
    ACT0002.camera = "Object:Camera"
    ACT0002.property = "target"
    ACT0002.distance = 100.0
    ACT0003.condition = ACT0002
    ACT0003.game_object = "Object:Aim"
    ACT0003.attribute_value = ACT0002.OUTPOINT
    ACT0003.value_type = 'worldPosition'
    ACT0004.condition = ACT0003.OUT
    ACT0004.game_object = "Object:Aim"
    ACT0004.vector = ACT0002.OUTNORMAL
    ACT0004.axis = 2
    ACT0004.factor = 0.4000000059604645
    ACT0005.condition = None
    ACT0005.moving_object = "Object:Cannon"
    ACT0005.target_point = PAR0007
    ACT0005.rot_axis = 0
    ACT0005.front_axis = 2
    ACT0006.condition = ACT0001
    ACT0006.game_object = "Object:Cannon"
    ACT0006.vector = PAR0007
    ACT0006.axis = 2
    ACT0006.factor = 0.20000000298023224
    PAR0007.game_object = "Object:Aim"
    PAR0007.attribute_name = "worldPosition"
    PAR0008.game_object = "Object:Empty"
    PAR0008.attribute_name = "worldPosition"
    ACT0009.condition = CON0010
    ACT0009.name = "Cube.001"
    ACT0009.life = 200
    CON0010.mouse_button_code = bge.events.LEFTMOUSE
    CON0010.pulse = False
    ACT0011.condition = ACT0009.OUT
    ACT0011.game_object = ACT0009.OBJ
    ACT0011.attribute_value = PAR0008
    ACT0011.value_type = 'worldPosition'
    PAR0012.game_object = "Object:Empty"
    PAR0012.attribute_name = "worldOrientation"
    ACT0013.condition = ACT0014.OUT
    ACT0013.game_object = ACT0009.OBJ
    ACT0013.attribute_value = mathutils.Vector((0.0, 0.0, 20.0))
    ACT0013.value_type = 'localLinearVelocity'
    ACT0014.condition = ACT0011.OUT
    ACT0014.game_object = ACT0009.OBJ
    ACT0014.attribute_value = PAR0012
    ACT0014.value_type = 'worldOrientation'
    network.add_cell(CON0000)
    network.add_cell(ACT0002)
    network.add_cell(PAR0007)
    network.add_cell(CON0010)
    network.add_cell(PAR0012)
    network.add_cell(ACT0001)
    network.add_cell(ACT0005)
    network.add_cell(PAR0008)
    network.add_cell(ACT0003)
    network.add_cell(ACT0006)
    network.add_cell(ACT0004)
    network.add_cell(ACT0009)
    network.add_cell(ACT0011)
    network.add_cell(ACT0014)
    network.add_cell(ACT0013)
    owner["Static_Shooter"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__Static_Shooter')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("Static_Shooter")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
