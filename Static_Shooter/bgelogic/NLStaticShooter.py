#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.ActionRotateTo()
    ACT0001 = bgelogic.ActionMousePick()
    ACT0002 = bgelogic.ActionSetObjectAttribute()
    PAR0003 = bgelogic.ParameterObjectAttribute()
    PAR0004 = bgelogic.ParameterObjectAttribute()
    ACT0005 = bgelogic.ActionAddObject()
    CON0006 = bgelogic.ConditionMousePressed()
    ACT0007 = bgelogic.ActionSetObjectAttribute()
    PAR0008 = bgelogic.ParameterObjectAttribute()
    ACT0009 = bgelogic.ActionSetObjectAttribute()
    ACT0010 = bgelogic.ActionSetObjectAttribute()
    ACT0011 = bgelogic.ActionAlignAxisToVector()
    CON0012 = bgelogic.ConditionOnUpdate()
    ACT0013 = bgelogic.ActionAlignAxisToVector()
    ACT0014 = bgelogic.ActionRotateTo()
    PAR0015 = bgelogic.ParameterActiveCamera()
    ACT0000.condition = CON0012
    ACT0000.moving_object = "Object:Turret"
    ACT0000.target_point = PAR0003
    ACT0000.rot_axis = 2
    ACT0000.front_axis = 1
    ACT0001.condition = CON0012
    ACT0001.camera = PAR0015
    ACT0001.property = "target"
    ACT0001.distance = 100.0
    ACT0002.condition = ACT0001
    ACT0002.game_object = "Object:Aim"
    ACT0002.attribute_value = ACT0001.OUTPOINT
    ACT0002.value_type = 'worldPosition'
    PAR0003.game_object = "Object:Aim"
    PAR0003.attribute_name = "worldPosition"
    PAR0004.game_object = "Object:Empty"
    PAR0004.attribute_name = "worldPosition"
    ACT0005.condition = CON0006
    ACT0005.name = "Cube.001"
    ACT0005.life = 200
    CON0006.mouse_button_code = bge.events.LEFTMOUSE
    CON0006.pulse = False
    ACT0007.condition = ACT0005.OUT
    ACT0007.game_object = ACT0005.OBJ
    ACT0007.attribute_value = PAR0004
    ACT0007.value_type = 'worldPosition'
    PAR0008.game_object = "Object:Empty"
    PAR0008.attribute_name = "worldOrientation"
    ACT0009.condition = ACT0010.OUT
    ACT0009.game_object = ACT0005.OBJ
    ACT0009.attribute_value = mathutils.Vector((0.0, 0.0, 20.0))
    ACT0009.value_type = 'localLinearVelocity'
    ACT0010.condition = ACT0007.OUT
    ACT0010.game_object = ACT0005.OBJ
    ACT0010.attribute_value = PAR0008
    ACT0010.value_type = 'worldOrientation'
    ACT0011.condition = ACT0002.OUT
    ACT0011.game_object = "Object:Aim"
    ACT0011.vector = ACT0001.OUTNORMAL
    ACT0011.axis = 2
    ACT0011.factor = 0.4000000059604645
    ACT0013.condition = ACT0000
    ACT0013.game_object = "Object:Cannon"
    ACT0013.vector = PAR0003
    ACT0013.axis = 2
    ACT0013.factor = 0.20000000298023224
    ACT0014.condition = None
    ACT0014.moving_object = "Object:Cannon"
    ACT0014.target_point = PAR0003
    ACT0014.rot_axis = 0
    ACT0014.front_axis = 2
    network.add_cell(PAR0003)
    network.add_cell(CON0006)
    network.add_cell(PAR0008)
    network.add_cell(CON0012)
    network.add_cell(ACT0014)
    network.add_cell(ACT0000)
    network.add_cell(PAR0004)
    network.add_cell(ACT0013)
    network.add_cell(ACT0005)
    network.add_cell(PAR0015)
    network.add_cell(ACT0001)
    network.add_cell(ACT0007)
    network.add_cell(ACT0010)
    network.add_cell(ACT0002)
    network.add_cell(ACT0011)
    network.add_cell(ACT0009)
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
