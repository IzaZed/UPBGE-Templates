#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.ActionSetObjectAttribute()
    PAR0001 = bgelogic.ParameterObjectAttribute()
    ACT0002 = bgelogic.ActionSetObjectAttribute()
    ACT0003 = bgelogic.ActionAddObject()
    PAR0004 = bgelogic.ParameterObjectAttribute()
    ACT0005 = bgelogic.ActionSetObjectAttribute()
    CON0006 = bgelogic.ConditionMousePressed()
    ACT0007 = bgelogic.ActionRotateTo()
    ACT0008 = bgelogic.ActionMousePick()
    ACT0009 = bgelogic.ActionSetObjectAttribute()
    PAR0010 = bgelogic.ParameterObjectAttribute()
    ACT0011 = bgelogic.ActionAlignAxisToVector()
    CON0012 = bgelogic.ConditionOnUpdate()
    ACT0013 = bgelogic.ActionAlignAxisToVector()
    ACT0014 = bgelogic.ActionRotateTo()
    PAR0015 = bgelogic.ParameterActiveCamera()
    ACT0000.condition = ACT0005.OUT
    ACT0000.game_object = ACT0003.OBJ
    ACT0000.attribute_value = mathutils.Vector((0.0, 0.0, 20.0))
    ACT0000.value_type = 'localLinearVelocity'
    PAR0001.game_object = "Object:Empty"
    PAR0001.attribute_name = "worldOrientation"
    ACT0002.condition = ACT0003.OUT
    ACT0002.game_object = ACT0003.OBJ
    ACT0002.attribute_value = PAR0004
    ACT0002.value_type = 'worldPosition'
    ACT0003.condition = CON0006
    ACT0003.name = "Cube.001"
    ACT0003.life = 200
    PAR0004.game_object = "Object:Empty"
    PAR0004.attribute_name = "worldPosition"
    ACT0005.condition = ACT0002.OUT
    ACT0005.game_object = ACT0003.OBJ
    ACT0005.attribute_value = PAR0001
    ACT0005.value_type = 'worldOrientation'
    CON0006.mouse_button_code = bge.events.LEFTMOUSE
    CON0006.pulse = False
    ACT0007.condition = CON0012
    ACT0007.moving_object = "Object:Turret"
    ACT0007.target_point = PAR0010
    ACT0007.rot_axis = 2
    ACT0007.front_axis = 1
    ACT0008.condition = CON0012
    ACT0008.camera = PAR0015
    ACT0008.property = "target"
    ACT0008.distance = 100.0
    ACT0009.condition = ACT0008
    ACT0009.game_object = "Object:Aim"
    ACT0009.attribute_value = ACT0008.OUTPOINT
    ACT0009.value_type = 'worldPosition'
    PAR0010.game_object = "Object:Aim"
    PAR0010.attribute_name = "worldPosition"
    ACT0011.condition = ACT0009.OUT
    ACT0011.game_object = "Object:Aim"
    ACT0011.vector = ACT0008.OUTNORMAL
    ACT0011.axis = 2
    ACT0011.factor = 0.4000000059604645
    ACT0013.condition = ACT0007
    ACT0013.game_object = "Object:Cannon"
    ACT0013.vector = PAR0010
    ACT0013.axis = 2
    ACT0013.factor = 0.20000000298023224
    ACT0014.condition = None
    ACT0014.moving_object = "Object:Cannon"
    ACT0014.target_point = PAR0010
    ACT0014.rot_axis = 0
    ACT0014.front_axis = 2
    network.add_cell(PAR0001)
    network.add_cell(PAR0004)
    network.add_cell(CON0006)
    network.add_cell(PAR0010)
    network.add_cell(CON0012)
    network.add_cell(ACT0014)
    network.add_cell(ACT0003)
    network.add_cell(ACT0007)
    network.add_cell(ACT0013)
    network.add_cell(ACT0002)
    network.add_cell(PAR0015)
    network.add_cell(ACT0005)
    network.add_cell(ACT0000)
    network.add_cell(ACT0008)
    network.add_cell(ACT0009)
    network.add_cell(ACT0011)
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
