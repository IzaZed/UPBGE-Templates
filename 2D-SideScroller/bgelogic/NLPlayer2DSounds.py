# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    PAR0000 = bgelogic.ParameterSimpleValue()
    PAR0001 = bgelogic.ParameterSimpleValue()
    PAR0002 = bgelogic.ParameterSimpleValue()
    ACT0003 = bgelogic.InitNewList()
    CON0004 = bgelogic.GE_OnInit()
    CON0005 = bgelogic.ConditionOnce()
    PAR0006 = bgelogic.ParameterFindChildByName()
    PAR0007 = bgelogic.ParameterActionStatus()
    PAR0008 = bgelogic.ParameterObjectProperty()
    CON0009 = bgelogic.ConditionOrList()
    PAR0010 = bgelogic.ParameterRandomListIndex()
    ACT0011 = bgelogic.ActionStart3DSoundAdv()
    ACT0012 = bgelogic.ActionStartSound()
    CON0013 = bgelogic.ConditionLogicOp()
    CON0014 = bgelogic.ConditionLogicOp()
    PAR0015 = bgelogic.ParameterArithmeticOp()
    ACT0016 = bgelogic.AbsoluteValue()
    PAR0017 = bgelogic.ParameterObjectProperty()
    PAR0018 = bgelogic.ValueSwitch()
    PAR0019 = bgelogic.ValueSwitch()
    PAR0020 = bgelogic.ParameterGetCharacterInfo()
    PAR0000.value = "//Sounds/FootStep03.wav"
    PAR0001.value = "//Sounds/FootStep01.wav"
    PAR0002.value = "//Sounds/FootStep02.wav"
    ACT0003.value = PAR0001
    ACT0003.value2 = PAR0002
    ACT0003.value3 = PAR0000
    ACT0003.value4 = None
    ACT0003.value5 = None
    ACT0003.value6 = None
    CON0005.input_condition = CON0009
    CON0005.repeat = True
    CON0005.reset_time = 0.5
    PAR0006.from_parent = "NLO:U_O"
    PAR0006.child = "Player_Rig"
    PAR0007.game_object = PAR0006
    PAR0007.action_layer = 2
    PAR0008.game_object = "NLO:U_O"
    PAR0008.property_name = "landed"
    CON0009.ca = CON0013
    CON0009.cb = CON0014
    CON0009.cc = PAR0008
    CON0009.cd = None
    CON0009.ce = None
    CON0009.cf = None
    PAR0010.condition = CON0005
    PAR0010.items = ACT0003.LIST
    ACT0011.condition = CON0005
    ACT0011.speaker = "NLO:U_O"
    ACT0011.sound = PAR0010
    ACT0011.occlusion = False
    ACT0011.transition = 0.10000000149011612
    ACT0011.cutoff = 0.10000000149011612
    ACT0011.device_custom = "default3D"
    ACT0011.loop_count = 0
    ACT0011.pitch = 1.0
    ACT0011.volume = PAR0018.VAL
    ACT0011.attenuation = 1.0
    ACT0011.distance_ref = 1.0
    ACT0011.cone_angle = mathutils.Vector((360.0, 360.0))
    ACT0011.cone_outer_volume = 0.0
    ACT0012.condition = CON0004
    ACT0012.sound = "E:/Projects/2020/Node_Templates/2D-SideScroller/Sounds/Podington_Bear_-_Bountiful.mp3"
    ACT0012.loop_count = 0
    ACT0012.pitch = 1.0
    ACT0012.volume = 0.10000000149011612
    CON0013.param_a = PAR0007.ACTION_FRAME
    CON0013.param_b = 40
    CON0013.threshold = 1.0
    CON0013.operator = 0
    CON0014.param_a = PAR0007.ACTION_FRAME
    CON0014.param_b = 20
    CON0014.threshold = 1.0
    CON0014.operator = 0
    PAR0015.operator = bgelogic.ParameterArithmeticOp.op_by_code("MUL")
    PAR0015.operand_a = ACT0016.OUT
    PAR0015.operand_b = 5.0
    ACT0016.value = PAR0017
    PAR0017.game_object = "NLO:U_O"
    PAR0017.property_name = "running"
    PAR0018.condition = PAR0008
    PAR0018.val_a = 10.0
    PAR0018.val_b = PAR0019.VAL
    PAR0019.condition = PAR0020.ON_GROUND
    PAR0019.val_a = PAR0015
    PAR0019.val_b = 0.0
    PAR0020.local = False
    PAR0020.game_object = "NLO:U_O"
    network.add_cell(PAR0000)
    network.add_cell(PAR0002)
    network.add_cell(CON0004)
    network.add_cell(PAR0006)
    network.add_cell(PAR0008)
    network.add_cell(ACT0012)
    network.add_cell(PAR0017)
    network.add_cell(PAR0020)
    network.add_cell(PAR0001)
    network.add_cell(PAR0007)
    network.add_cell(CON0013)
    network.add_cell(ACT0016)
    network.add_cell(ACT0003)
    network.add_cell(CON0014)
    network.add_cell(CON0009)
    network.add_cell(PAR0015)
    network.add_cell(PAR0019)
    network.add_cell(CON0005)
    network.add_cell(PAR0018)
    network.add_cell(PAR0010)
    network.add_cell(ACT0011)
    owner["IGNLTree_Player_2D_Sounds"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__Player_2D_Sounds')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_Player_2D_Sounds")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
