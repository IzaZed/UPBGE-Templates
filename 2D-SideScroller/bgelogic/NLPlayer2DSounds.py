# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.ActionStart3DSound()
    ACT0001 = bgelogic.ActionStartSound()
    CON0002 = bgelogic.ConditionOnInit()
    ACT0003 = bgelogic.InitNewList()
    PAR0004 = bgelogic.ParameterSimpleValue()
    PAR0005 = bgelogic.ParameterSimpleValue()
    PAR0006 = bgelogic.ParameterSimpleValue()
    PAR0007 = bgelogic.ParameterObjectProperty()
    PAR0008 = bgelogic.ParameterFindChildByName()
    PAR0009 = bgelogic.ParameterActionStatus()
    CON0010 = bgelogic.ConditionLogicOp()
    CON0011 = bgelogic.ConditionLogicOp()
    CON0012 = bgelogic.ConditionOrList()
    CON0013 = bgelogic.ConditionOnce()
    PAR0014 = bgelogic.ValueSwitch()
    PAR0015 = bgelogic.ParameterArithmeticOp()
    PAR0016 = bgelogic.ParameterObjectProperty()
    ACT0017 = bgelogic.AbsoluteValue()
    ACT0018 = bgelogic.ActionGetCharacterInfo()
    PAR0019 = bgelogic.ValueSwitch()
    PAR0020 = bgelogic.ParameterRandomListIndex()
    ACT0000.condition = CON0013
    ACT0000.speaker = "NLO:U_O"
    ACT0000.sound = PAR0020
    ACT0000.loop_count = 0
    ACT0000.pitch = 0.0
    ACT0000.volume = PAR0014.VAL
    ACT0000.distance_max = 500.0
    ACT0001.condition = CON0002
    ACT0001.sound = "//Sounds/Podington_Bear_-_Bountiful.mp3"
    ACT0001.loop_count = -1
    ACT0001.pitch = 0.0
    ACT0001.volume = 1.0
    ACT0003.value = PAR0005
    ACT0003.value2 = PAR0006
    ACT0003.value3 = PAR0004
    ACT0003.value4 = None
    ACT0003.value5 = None
    ACT0003.value6 = None
    PAR0004.value = "//Sounds/FootStep03.wav"
    PAR0005.value = "//Sounds/FootStep01.wav"
    PAR0006.value = "//Sounds/FootStep02.wav"
    PAR0007.game_object = "NLO:U_O"
    PAR0007.property_name = "landed"
    PAR0008.from_parent = "NLO:U_O"
    PAR0008.child = "Player_Rig"
    PAR0009.game_object = PAR0008
    PAR0009.action_layer = 2
    CON0010.threshold = 1.0
    CON0010.param_a = PAR0009.ACTION_FRAME
    CON0010.param_b = 40
    CON0010.operator = 0
    CON0011.threshold = 0.6000000238418579
    CON0011.param_a = PAR0009.ACTION_FRAME
    CON0011.param_b = 20
    CON0011.operator = 0
    CON0012.ca = CON0010
    CON0012.cb = CON0011
    CON0012.cc = PAR0007
    CON0012.cd = False
    CON0012.ce = False
    CON0012.cf = False
    CON0013.input_condition = CON0012
    CON0013.repeat = True
    CON0013.reset_time = 0.5
    PAR0014.condition = PAR0007
    PAR0014.val_a = PAR0019.VAL
    PAR0014.val_b = 10.0
    PAR0015.operator = bgelogic.ParameterArithmeticOp.op_by_code("MUL")
    PAR0015.operand_a = ACT0017.OUT
    PAR0015.operand_b = 5.0
    PAR0016.game_object = "NLO:U_O"
    PAR0016.property_name = "running"
    ACT0017.value = PAR0016
    ACT0018.condition = True
    ACT0018.game_object = "NLO:U_O"
    PAR0019.condition = ACT0018.ON_GROUND
    PAR0019.val_a = 0.0
    PAR0019.val_b = PAR0015
    PAR0020.condition = CON0013
    PAR0020.list = ACT0003.LIST
    network.add_cell(CON0002)
    network.add_cell(PAR0004)
    network.add_cell(PAR0006)
    network.add_cell(PAR0008)
    network.add_cell(PAR0016)
    network.add_cell(ACT0018)
    network.add_cell(ACT0001)
    network.add_cell(PAR0005)
    network.add_cell(PAR0009)
    network.add_cell(CON0011)
    network.add_cell(ACT0017)
    network.add_cell(ACT0003)
    network.add_cell(CON0010)
    network.add_cell(PAR0015)
    network.add_cell(PAR0007)
    network.add_cell(PAR0019)
    network.add_cell(CON0012)
    network.add_cell(PAR0014)
    network.add_cell(CON0013)
    network.add_cell(PAR0020)
    network.add_cell(ACT0000)
    owner["Player_2D_Sounds"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__Player_2D_Sounds')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("Player_2D_Sounds")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
