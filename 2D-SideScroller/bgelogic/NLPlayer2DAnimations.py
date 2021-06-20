# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    PAR0000 = bgelogic.ParameterGetCharacterInfo()
    PAR0001 = bgelogic.ParameterObjectProperty()
    PAR0002 = bgelogic.ParameterObjectProperty()
    PAR0003 = bgelogic.ParameterObjectProperty()
    PAR0004 = bgelogic.ParameterObjectProperty()
    ACT0005 = bgelogic.ActionSetGameObjectGameProperty()
    CON0006 = bgelogic.ConditionValueChanged()
    ACT0007 = bgelogic.ActionPlayAction()
    ACT0008 = bgelogic.ActionStopAnimation()
    PAR0009 = bgelogic.ParameterFindChildByName()
    PAR0010 = bgelogic.ParameterMathFun()
    ACT0011 = bgelogic.AbsoluteValue()
    PAR0012 = bgelogic.ValueSwitch()
    PAR0013 = bgelogic.ParameterGetCharacterInfo()
    PAR0014 = bgelogic.ParameterObjectProperty()
    CON0015 = bgelogic.GE_OnInit()
    ACT0016 = bgelogic.ActionPlayAction()
    ACT0017 = bgelogic.ActionPlayAction()
    ACT0018 = bgelogic.ActionPlayAction()
    PAR0000.local = True
    PAR0000.game_object = "NLO:U_O"
    PAR0001.game_object = "NLO:U_O"
    PAR0001.property_name = "running"
    PAR0002.game_object = "NLO:U_O"
    PAR0002.property_name = "falling"
    PAR0003.game_object = "NLO:U_O"
    PAR0003.property_name = "jumped"
    PAR0004.game_object = "NLO:U_O"
    PAR0004.property_name = "landed"
    ACT0005.condition = CON0006
    ACT0005.game_object = "NLO:U_O"
    ACT0005.property_name = "start_falling"
    ACT0005.property_value = CON0006.CURRENT_VALUE
    CON0006.initialize = False
    CON0006.current_value = ACT0007.FINISHED
    ACT0007.condition = PAR0003
    ACT0007.game_object = PAR0009
    ACT0007.action_name = "Jump"
    ACT0007.start_frame = 0.0
    ACT0007.end_frame = 60.0
    ACT0007.layer = 3
    ACT0007.priority = 0
    ACT0007.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0007.stop = True
    ACT0007.layer_weight = PAR0010
    ACT0007.speed = 1.0
    ACT0007.blendin = 0.0
    ACT0007.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0008.condition = PAR0004
    ACT0008.game_object = PAR0009
    ACT0008.action_layer = 3
    PAR0009.from_parent = "NLO:U_O"
    PAR0009.child = "Player_Rig"
    PAR0010.formula = "1.1 - (a * 1.6) "
    PAR0010.a = PAR0002
    PAR0010.b = 0.0
    ACT0011.value = PAR0001
    PAR0012.condition = PAR0013.ON_GROUND
    PAR0012.val_a = ACT0011.OUT
    PAR0012.val_b = 0.0
    PAR0013.local = True
    PAR0013.game_object = "NLO:U_O"
    PAR0014.game_object = "NLO:U_O"
    PAR0014.property_name = "grounded"
    ACT0016.condition = ACT0018.STARTED
    ACT0016.game_object = PAR0009
    ACT0016.action_name = "Run"
    ACT0016.start_frame = 0.0
    ACT0016.end_frame = 42.0
    ACT0016.layer = 2
    ACT0016.priority = 0
    ACT0016.play_mode = bge.logic.KX_ACTION_MODE_LOOP
    ACT0016.stop = False
    ACT0016.layer_weight = PAR0012.VAL
    ACT0016.speed = 1.5
    ACT0016.blendin = 0.0
    ACT0016.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0017.condition = ACT0016.STARTED
    ACT0017.game_object = PAR0009
    ACT0017.action_name = "Fall"
    ACT0017.start_frame = 0.0
    ACT0017.end_frame = 42.0
    ACT0017.layer = 0
    ACT0017.priority = 0
    ACT0017.play_mode = bge.logic.KX_ACTION_MODE_LOOP
    ACT0017.stop = False
    ACT0017.layer_weight = 1.0
    ACT0017.speed = 1.0
    ACT0017.blendin = 6.0
    ACT0017.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0018.condition = CON0015
    ACT0018.game_object = PAR0009
    ACT0018.action_name = "Idle"
    ACT0018.start_frame = 0.0
    ACT0018.end_frame = 250.0
    ACT0018.layer = 1
    ACT0018.priority = 0
    ACT0018.play_mode = bge.logic.KX_ACTION_MODE_LOOP
    ACT0018.stop = False
    ACT0018.layer_weight = PAR0014
    ACT0018.speed = 1.0
    ACT0018.blendin = 0.0
    ACT0018.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    network.add_cell(PAR0000)
    network.add_cell(PAR0002)
    network.add_cell(PAR0004)
    network.add_cell(PAR0009)
    network.add_cell(PAR0013)
    network.add_cell(CON0015)
    network.add_cell(PAR0001)
    network.add_cell(ACT0008)
    network.add_cell(ACT0011)
    network.add_cell(PAR0014)
    network.add_cell(ACT0018)
    network.add_cell(PAR0003)
    network.add_cell(PAR0010)
    network.add_cell(ACT0007)
    network.add_cell(CON0006)
    network.add_cell(ACT0005)
    network.add_cell(PAR0012)
    network.add_cell(ACT0016)
    network.add_cell(ACT0017)
    owner["IGNLTree_Player_2D_Animations"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__Player_2D_Animations')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_Player_2D_Animations")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
