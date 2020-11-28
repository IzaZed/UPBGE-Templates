# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.ActionPlayAction()
    PAR0001 = bgelogic.ValueSwitch()
    ACT0002 = bgelogic.ActionGetCharacterInfo()
    PAR0003 = bgelogic.ParameterObjectProperty()
    PAR0004 = bgelogic.ParameterObjectProperty()
    ACT0005 = bgelogic.AbsoluteValue()
    ACT0006 = bgelogic.ActionPlayAction()
    ACT0007 = bgelogic.ActionPlayAction()
    PAR0008 = bgelogic.ParameterFindChildByName()
    CON0009 = bgelogic.ConditionOnInit()
    PAR0010 = bgelogic.ParameterObjectProperty()
    ACT0011 = bgelogic.ActionStopAnimation()
    PAR0012 = bgelogic.ParameterObjectProperty()
    PAR0013 = bgelogic.ParameterObjectProperty()
    PAR0014 = bgelogic.ParameterObjectProperty()
    ACT0015 = bgelogic.ActionSetGameObjectGameProperty()
    CON0016 = bgelogic.ConditionValueChanged()
    ACT0017 = bgelogic.ActionPlayAction()
    PAR0018 = bgelogic.ParameterMathFun()
    ACT0000.condition = ACT0006.STARTED
    ACT0000.game_object = PAR0008
    ACT0000.action_name = 'Run'
    ACT0000.stop = False
    ACT0000.start_frame = 0.0
    ACT0000.end_frame = 42.0
    ACT0000.layer = 2
    ACT0000.priority = 0
    ACT0000.play_mode = bge.logic.KX_ACTION_MODE_LOOP
    ACT0000.layer_weight = PAR0001.VAL
    ACT0000.speed = 1.5
    ACT0000.blendin = 0.0
    ACT0000.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    PAR0001.condition = ACT0002.ON_GROUND
    PAR0001.val_a = 0.0
    PAR0001.val_b = ACT0005.OUT
    ACT0002.condition = True
    ACT0002.game_object = "NLO:U_O"
    PAR0003.game_object = "NLO:U_O"
    PAR0003.property_name = "grounded"
    PAR0004.game_object = "NLO:U_O"
    PAR0004.property_name = "running"
    ACT0005.value = PAR0004
    ACT0006.condition = CON0009
    ACT0006.game_object = PAR0008
    ACT0006.action_name = 'Idle'
    ACT0006.stop = False
    ACT0006.start_frame = 0.0
    ACT0006.end_frame = 250.0
    ACT0006.layer = 1
    ACT0006.priority = 0
    ACT0006.play_mode = bge.logic.KX_ACTION_MODE_LOOP
    ACT0006.layer_weight = PAR0003
    ACT0006.speed = 1.0
    ACT0006.blendin = 0.0
    ACT0006.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0007.condition = ACT0000.STARTED
    ACT0007.game_object = PAR0008
    ACT0007.action_name = 'Fall'
    ACT0007.stop = False
    ACT0007.start_frame = 0.0
    ACT0007.end_frame = 42.0
    ACT0007.layer = 0
    ACT0007.priority = 0
    ACT0007.play_mode = bge.logic.KX_ACTION_MODE_LOOP
    ACT0007.layer_weight = 0.41999998688697815
    ACT0007.speed = 1.0
    ACT0007.blendin = 6.0
    ACT0007.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    PAR0008.from_parent = "NLO:U_O"
    PAR0008.child = "Player_Rig"
    PAR0010.game_object = "NLO:U_O"
    PAR0010.property_name = "landed"
    ACT0011.condition = PAR0010
    ACT0011.game_object = PAR0008
    ACT0011.action_layer = 3
    PAR0012.game_object = "NLO:U_O"
    PAR0012.property_name = "jumped"
    PAR0013.game_object = "NLO:U_O"
    PAR0013.property_name = "falling"
    PAR0014.game_object = "NLO:U_O"
    PAR0014.property_name = "falling"
    ACT0015.condition = CON0016
    ACT0015.game_object = "NLO:U_O"
    ACT0015.property_name = "start_falling"
    ACT0015.property_value = CON0016.CURRENT_VALUE
    CON0016.initialize = False
    CON0016.current_value = ACT0017.FINISHED
    ACT0017.condition = PAR0012
    ACT0017.game_object = PAR0008
    ACT0017.action_name = 'Jump'
    ACT0017.stop = True
    ACT0017.start_frame = 0.0
    ACT0017.end_frame = 60.0
    ACT0017.layer = 3
    ACT0017.priority = 0
    ACT0017.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0017.layer_weight = PAR0018
    ACT0017.speed = 1.0
    ACT0017.blendin = 3.0
    ACT0017.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    PAR0018.formula = "1.1 - (a  / 2) "
    PAR0018.a = PAR0013
    PAR0018.b = 0.0
    network.add_cell(ACT0002)
    network.add_cell(PAR0004)
    network.add_cell(PAR0008)
    network.add_cell(PAR0010)
    network.add_cell(PAR0012)
    network.add_cell(PAR0014)
    network.add_cell(PAR0003)
    network.add_cell(CON0009)
    network.add_cell(PAR0013)
    network.add_cell(PAR0018)
    network.add_cell(ACT0005)
    network.add_cell(ACT0011)
    network.add_cell(ACT0017)
    network.add_cell(PAR0001)
    network.add_cell(CON0016)
    network.add_cell(ACT0006)
    network.add_cell(ACT0015)
    network.add_cell(ACT0000)
    network.add_cell(ACT0007)
    owner["Player_2D_Animations"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__Player_2D_Animations')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("Player_2D_Animations")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
