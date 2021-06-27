# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionKeyPressed()
    CON0001 = bgelogic.ConditionKeyPressed()
    CON0002 = bgelogic.ConditionKeyPressed()
    CON0003 = bgelogic.ConditionKeyPressed()
    PAR0004 = bgelogic.ParameterArithmeticOp()
    PAR0005 = bgelogic.ParameterArithmeticOp()
    PAR0006 = bgelogic.ParameterVector2Simple()
    PAR0007 = bgelogic.ParameterVectorMath()
    PAR0008 = bgelogic.ParameterSimpleValue()
    PAR0009 = bgelogic.ParameterArithmeticOp()
    ACT0010 = bgelogic.ActionSetCharacterWalkDir()
    CON0011 = bgelogic.ConditionOnUpdate()
    ACT0012 = bgelogic.ActionMouseLook()
    CON0013 = bgelogic.ConditionMousePressed()
    ACT0014 = bgelogic.ActionCameraPick()
    ACT0015 = bgelogic.ActionApplyImpulse()
    ACT0016 = bgelogic.ActionSetObjectAttribute()
    ACT0017 = bgelogic.InvertValue()
    ACT0018 = bgelogic.ActionSetParent()
    ACT0019 = bgelogic.ActionAddObject()
    CON0020 = bgelogic.ConditionMousePressedOn()
    ACT0021 = bgelogic.ActionToggleGameObjectGameProperty()
    PAR0022 = bgelogic.ParameterObjectProperty()
    ACT0023 = bgelogic.SetEeveeAO()
    CON0024 = bgelogic.ConditionKeyPressed()
    ACT0025 = bgelogic.ActionSetGameObjectVisibility()
    ACT0026 = bgelogic.ActionSetGameObjectVisibility()
    ACT0027 = bgelogic.InvertBool()
    PAR0028 = bgelogic.ParameterObjectAttribute()
    ACT0029 = bgelogic.ActionPlayAction()
    CON0030 = bgelogic.GE_OnInit()
    CON0000.key_code = bge.events.WKEY
    CON0000.pulse = True
    CON0001.key_code = bge.events.SKEY
    CON0001.pulse = True
    CON0002.key_code = bge.events.AKEY
    CON0002.pulse = True
    CON0003.key_code = bge.events.DKEY
    CON0003.pulse = True
    PAR0004.operator = bgelogic.ParameterArithmeticOp.op_by_code("SUB")
    PAR0004.operand_a = CON0000
    PAR0004.operand_b = CON0001
    PAR0005.operator = bgelogic.ParameterArithmeticOp.op_by_code("SUB")
    PAR0005.operand_a = CON0002
    PAR0005.operand_b = CON0003
    PAR0006.input_x = PAR0004
    PAR0006.input_y = PAR0005
    PAR0007.vector = PAR0006.OUTV
    PAR0007.vector_2 = mathutils.Vector((0.0, 0.0, 0.0))
    PAR0007.factor = 1.0
    PAR0007.op = 'normalize'
    PAR0008.value = 0.07000000029802322
    PAR0009.operator = bgelogic.ParameterArithmeticOp.op_by_code("MUL")
    PAR0009.operand_a = PAR0007
    PAR0009.operand_b = PAR0008
    ACT0010.local = True
    ACT0010.condition = CON0011
    ACT0010.game_object = "NLO:U_O"
    ACT0010.walkDir = PAR0009
    ACT0012.condition = CON0011
    ACT0012.game_object_x = "NLO:U_O"
    ACT0012.game_object_y = "NLO:Head"
    ACT0012.inverted = {'x': False, 'y': False}
    ACT0012.sensitivity = 1.0
    ACT0012.use_cap_z = False
    ACT0012.cap_z = mathutils.Vector((0.0, 0.0))
    ACT0012.use_cap_y = True
    ACT0012.cap_y = mathutils.Vector((1.5533430576324463, 1.5533430576324463))
    ACT0012.smooth = 0.20000000298023224
    CON0013.mouse_button_code = bge.events.LEFTMOUSE
    CON0013.pulse = False
    ACT0014.condition = CON0013
    ACT0014.camera = "NLO:Player_Camera"
    ACT0014.aim = mathutils.Vector((0.5, 0.5))
    ACT0014.property_name = ""
    ACT0014.xray = False
    ACT0014.distance = 100.0
    ACT0015.local = False
    ACT0015.condition = ACT0014
    ACT0015.game_object = ACT0014.PICKED_OBJECT
    ACT0015.point = ACT0014.PICKED_POINT
    ACT0015.impulse = ACT0017.OUT
    ACT0016.condition = ACT0019.OUT
    ACT0016.xyz = {'x': True, 'y': True, 'z': True}
    ACT0016.game_object = ACT0019.OBJ
    ACT0016.attribute_value = ACT0014.PICKED_POINT
    ACT0016.value_type = 'worldPosition'
    ACT0017.value = ACT0014.PICKED_NORMAL
    ACT0018.condition = ACT0016.OUT
    ACT0018.child_object = ACT0019.OBJ
    ACT0018.parent_object = ACT0014.PICKED_OBJECT
    ACT0018.compound = False
    ACT0018.ghost = False
    ACT0019.condition = ACT0015.OUT
    ACT0019.name = "Projectile"
    ACT0019.reference = "NLO:U_O"
    ACT0019.life = 200
    CON0020.mouse_button = bge.events.LEFTMOUSE
    CON0020.game_object = "NLO:Cube.029"
    ACT0021.condition = CON0020
    ACT0021.game_object = "NLO:Cube.029"
    ACT0021.property_name = "use"
    PAR0022.game_object = "NLO:Cube.029"
    PAR0022.property_name = "use"
    ACT0023.condition = ACT0021.OUT
    ACT0023.value = PAR0022
    CON0024.key_code = bge.events.SPACEKEY
    CON0024.pulse = False
    ACT0025.condition = ACT0026.OUT
    ACT0025.game_object = "NLO:Light"
    ACT0025.visible = ACT0027.OUT
    ACT0025.recursive = False
    ACT0026.condition = CON0024
    ACT0026.game_object = "NLO:Light.001"
    ACT0026.visible = PAR0028
    ACT0026.recursive = False
    ACT0027.value = PAR0028
    PAR0028.game_object = "NLO:Light"
    PAR0028.attribute_name = "visible"
    ACT0029.condition = CON0030
    ACT0029.game_object = "NLO:Player"
    ACT0029.action_name = "Shader NodetreeAction"
    ACT0029.start_frame = 0.0
    ACT0029.end_frame = 24.0
    ACT0029.layer = 0
    ACT0029.priority = 0
    ACT0029.play_mode = bge.logic.KX_ACTION_MODE_LOOP
    ACT0029.stop = False
    ACT0029.layer_weight = 1.0
    ACT0029.speed = 1.0
    ACT0029.blendin = 0.0
    ACT0029.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    network.add_cell(CON0000)
    network.add_cell(CON0002)
    network.add_cell(PAR0008)
    network.add_cell(CON0011)
    network.add_cell(CON0013)
    network.add_cell(CON0020)
    network.add_cell(PAR0022)
    network.add_cell(CON0024)
    network.add_cell(PAR0028)
    network.add_cell(CON0030)
    network.add_cell(CON0001)
    network.add_cell(PAR0004)
    network.add_cell(ACT0012)
    network.add_cell(ACT0021)
    network.add_cell(ACT0026)
    network.add_cell(ACT0029)
    network.add_cell(CON0003)
    network.add_cell(ACT0014)
    network.add_cell(ACT0017)
    network.add_cell(ACT0023)
    network.add_cell(ACT0027)
    network.add_cell(PAR0005)
    network.add_cell(ACT0015)
    network.add_cell(ACT0019)
    network.add_cell(PAR0006)
    network.add_cell(ACT0016)
    network.add_cell(ACT0025)
    network.add_cell(PAR0007)
    network.add_cell(ACT0018)
    network.add_cell(PAR0009)
    network.add_cell(ACT0010)
    owner["IGNLTree_FPS_Player"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__FPS_Player')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_FPS_Player")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
