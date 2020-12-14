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
    PAR0003 = bgelogic.ParameterSimpleValue()
    PAR0004 = bgelogic.ParameterSimpleValue()
    PAR0005 = bgelogic.ParameterSimpleValue()
    PAR0006 = bgelogic.ParameterRandomListIndex()
    PAR0007 = bgelogic.ValueSwitch()
    ACT0008 = bgelogic.ActionGetCharacterInfo()
    ACT0009 = bgelogic.AbsoluteValue()
    PAR0010 = bgelogic.ParameterArithmeticOp()
    PAR0011 = bgelogic.ValueSwitch()
    PAR0012 = bgelogic.ParameterObjectProperty()
    ACT0013 = bgelogic.InitNewList()
    CON0014 = bgelogic.ConditionOrList()
    CON0015 = bgelogic.ConditionOnce()
    PAR0016 = bgelogic.ParameterObjectProperty()
    PAR0017 = bgelogic.ParameterFindChildByName()
    PAR0018 = bgelogic.ParameterActionStatus()
    CON0019 = bgelogic.ConditionLogicOp()
    CON0020 = bgelogic.ConditionLogicOp()
    ACT0000.condition = CON0015
    ACT0000.speaker = "NLO:U_O"
    ACT0000.sound = PAR0006
    ACT0000.loop_count = 0
    ACT0000.pitch = 0.0
    ACT0000.volume = PAR0011.VAL
    ACT0000.distance_max = 500.0
    ACT0001.condition = CON0002
    ACT0001.sound = "//Sounds/Podington_Bear_-_Bountiful.mp3"
    ACT0001.loop_count = -1
    ACT0001.pitch = 0.0
    ACT0001.volume = 1.0
    PAR0003.value = "//Sounds/FootStep03.wav"
    PAR0004.value = "//Sounds/FootStep01.wav"
    PAR0005.value = "//Sounds/FootStep02.wav"
    PAR0006.condition = CON0015
    PAR0006.list = ACT0013.LIST
    PAR0007.condition = ACT0008.ON_GROUND
    PAR0007.val_a = 0.0
    PAR0007.val_b = PAR0010
    ACT0008.condition = True
    ACT0008.game_object = "NLO:U_O"
    ACT0009.value = PAR0012
    PAR0010.operator = bgelogic.ParameterArithmeticOp.op_by_code("MUL")
    PAR0010.operand_a = ACT0009.OUT
    PAR0010.operand_b = 5.0
    PAR0011.condition = PAR0016
    PAR0011.val_a = PAR0007.VAL
    PAR0011.val_b = 10.0
    PAR0012.game_object = "NLO:U_O"
    PAR0012.property_name = "running"
    ACT0013.value = PAR0004
    ACT0013.value2 = PAR0005
    ACT0013.value3 = PAR0003
    ACT0013.value4 = None
    ACT0013.value5 = None
    ACT0013.value6 = None
    CON0014.ca = CON0019
    CON0014.cb = CON0020
    CON0014.cc = PAR0016
    CON0014.cd = False
    CON0014.ce = False
    CON0014.cf = False
    CON0015.input_condition = CON0014
    CON0015.repeat = True
    CON0015.reset_time = 0.5
    PAR0016.game_object = "NLO:U_O"
    PAR0016.property_name = "landed"
    PAR0017.from_parent = "NLO:U_O"
    PAR0017.child = "Player_Rig"
    PAR0018.game_object = PAR0017
    PAR0018.action_layer = 2
    CON0019.threshold = 0.6000000238418579
    CON0019.param_a = PAR0018.ACTION_FRAME
    CON0019.param_b = 40
    CON0019.operator = 0
    CON0020.threshold = 0.6000000238418579
    CON0020.param_a = PAR0018.ACTION_FRAME
    CON0020.param_b = 20
    CON0020.operator = 0
    network.add_cell(CON0002)
    network.add_cell(PAR0004)
    network.add_cell(ACT0008)
    network.add_cell(PAR0012)
    network.add_cell(PAR0016)
    network.add_cell(ACT0001)
    network.add_cell(PAR0005)
    network.add_cell(ACT0009)
    network.add_cell(PAR0017)
    network.add_cell(PAR0003)
    network.add_cell(PAR0010)
    network.add_cell(ACT0013)
    network.add_cell(PAR0018)
    network.add_cell(CON0020)
    network.add_cell(PAR0007)
    network.add_cell(CON0019)
    network.add_cell(PAR0011)
    network.add_cell(CON0014)
    network.add_cell(CON0015)
    network.add_cell(PAR0006)
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
