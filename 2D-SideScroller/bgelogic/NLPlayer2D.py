# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionKeyPressed()
    CON0001 = bgelogic.ConditionKeyPressed()
    CON0002 = bgelogic.ConditionOr()
    ACT0003 = bgelogic.ActionGetCharacterInfo()
    CON0004 = bgelogic.ConditionAnd()
    CON0005 = bgelogic.ConditionKeyPressed()
    PAR0006 = bgelogic.ParameterObjectProperty()
    CON0007 = bgelogic.ConditionOnUpdate()
    ACT0008 = bgelogic.ActionSetGameObjectGameProperty()
    PAR0009 = bgelogic.InterpolateValue()
    PAR0010 = bgelogic.ValueSwitch()
    PAR0011 = bgelogic.ValueSwitch()
    CON0012 = bgelogic.ConditionValueTrigger()
    PAR0013 = bgelogic.ParameterObjectProperty()
    CON0014 = bgelogic.ConditionOnUpdate()
    PAR0015 = bgelogic.InterpolateValue()
    ACT0016 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0017 = bgelogic.ActionCharacterJump()
    PAR0018 = bgelogic.ParameterFindChildByName()
    ACT0019 = bgelogic.ActionPlayAction()
    PAR0020 = bgelogic.ParameterObjectProperty()
    PAR0021 = bgelogic.ParameterObjectProperty()
    ACT0022 = bgelogic.ActionPlayAction()
    CON0023 = bgelogic.ConditionOnInit()
    ACT0024 = bgelogic.ActionPrint()
    ACT0025 = bgelogic.ActionPlayAction()
    ACT0026 = bgelogic.ActionPlayAction()
    CON0027 = bgelogic.ConditionOr()
    CON0028 = bgelogic.ConditionValueTrigger()
    ACT0029 = bgelogic.ActionStopAnimation()
    ACT0030 = bgelogic.ActionStopAnimation()
    ACT0031 = bgelogic.ActionStopAnimation()
    CON0000.key_code = bge.events.AKEY
    CON0000.pulse = True
    CON0001.key_code = bge.events.DKEY
    CON0001.pulse = True
    CON0002.condition_a = CON0000
    CON0002.condition_b = CON0001
    ACT0003.condition = True
    ACT0003.game_object = "NLO:U_O"
    CON0004.condition_a = ACT0003.ON_GROUND
    CON0004.condition_b = CON0002
    CON0005.key_code = bge.events.SPACEKEY
    CON0005.pulse = False
    PAR0006.game_object = "NLO:U_O"
    PAR0006.property_name = "running"
    ACT0008.condition = CON0007
    ACT0008.game_object = "NLO:U_O"
    ACT0008.property_name = "running"
    ACT0008.property_value = PAR0009
    PAR0009.value_a = PAR0006
    PAR0009.value_b = PAR0010.VAL
    PAR0009.factor = 0.30000001192092896
    PAR0010.condition = CON0004
    PAR0010.val_a = 0.0
    PAR0010.val_b = 1.0
    PAR0011.condition = ACT0003.ON_GROUND
    PAR0011.val_a = 0.0
    PAR0011.val_b = 1.0
    CON0012.monitored_value = ACT0003.ON_GROUND
    CON0012.trigger_value = True
    PAR0013.game_object = "NLO:U_O"
    PAR0013.property_name = "grounded"
    PAR0015.value_a = PAR0013
    PAR0015.value_b = PAR0011.VAL
    PAR0015.factor = 0.30000001192092896
    ACT0016.condition = CON0014
    ACT0016.game_object = "NLO:U_O"
    ACT0016.property_name = "grounded"
    ACT0016.property_value = PAR0015
    ACT0017.condition = CON0005
    ACT0017.game_object = "NLO:U_O"
    PAR0018.from_parent = "NLO:U_O"
    PAR0018.child = "Player_Rig"
    ACT0019.condition = CON0023
    ACT0019.game_object = PAR0018
    ACT0019.action_name = 'Idle'
    ACT0019.stop = False
    ACT0019.start_frame = 0.0
    ACT0019.end_frame = 250.0
    ACT0019.layer = 1
    ACT0019.priority = 0
    ACT0019.play_mode = bge.logic.KX_ACTION_MODE_LOOP
    ACT0019.layer_weight = PAR0021
    ACT0019.speed = 1.0
    ACT0019.blendin = 0.0
    ACT0019.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    PAR0020.game_object = "NLO:U_O"
    PAR0020.property_name = "running"
    PAR0021.game_object = "NLO:U_O"
    PAR0021.property_name = "grounded"
    ACT0022.condition = ACT0019.STARTED
    ACT0022.game_object = PAR0018
    ACT0022.action_name = 'Run'
    ACT0022.stop = False
    ACT0022.start_frame = 0.0
    ACT0022.end_frame = 42.0
    ACT0022.layer = 2
    ACT0022.priority = 0
    ACT0022.play_mode = bge.logic.KX_ACTION_MODE_LOOP
    ACT0022.layer_weight = PAR0020
    ACT0022.speed = 1.2999999523162842
    ACT0022.blendin = 0.0
    ACT0022.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0024.condition = True
    ACT0024.value = ACT0017.OUT
    ACT0025.condition = CON0027
    ACT0025.game_object = PAR0018
    ACT0025.action_name = 'Fall'
    ACT0025.stop = False
    ACT0025.start_frame = 0.0
    ACT0025.end_frame = 43.0
    ACT0025.layer = 0
    ACT0025.priority = 0
    ACT0025.play_mode = bge.logic.KX_ACTION_MODE_LOOP
    ACT0025.layer_weight = 0.41999998688697815
    ACT0025.speed = 1.0
    ACT0025.blendin = 6.0
    ACT0025.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0026.condition = ACT0017.OUT
    ACT0026.game_object = PAR0018
    ACT0026.action_name = 'Jump'
    ACT0026.stop = True
    ACT0026.start_frame = 0.0
    ACT0026.end_frame = 44.0
    ACT0026.layer = 3
    ACT0026.priority = 0
    ACT0026.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0026.layer_weight = 1.0
    ACT0026.speed = 1.0
    ACT0026.blendin = 3.0
    ACT0026.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0027.condition_a = ACT0031.OUT
    CON0027.condition_b = CON0028
    CON0028.monitored_value = ACT0003.ON_GROUND
    CON0028.trigger_value = False
    ACT0029.condition = CON0012
    ACT0029.game_object = PAR0018
    ACT0029.action_layer = 3
    ACT0030.condition = ACT0029.OUT
    ACT0030.game_object = PAR0018
    ACT0030.action_layer = 0
    ACT0031.condition = ACT0026.FINISHED
    ACT0031.game_object = PAR0018
    ACT0031.action_layer = 0
    network.add_cell(CON0000)
    network.add_cell(ACT0003)
    network.add_cell(CON0005)
    network.add_cell(CON0007)
    network.add_cell(PAR0011)
    network.add_cell(PAR0013)
    network.add_cell(PAR0015)
    network.add_cell(ACT0017)
    network.add_cell(PAR0020)
    network.add_cell(CON0023)
    network.add_cell(CON0028)
    network.add_cell(CON0001)
    network.add_cell(PAR0006)
    network.add_cell(CON0012)
    network.add_cell(PAR0018)
    network.add_cell(PAR0021)
    network.add_cell(ACT0024)
    network.add_cell(ACT0026)
    network.add_cell(ACT0029)
    network.add_cell(ACT0031)
    network.add_cell(CON0002)
    network.add_cell(CON0014)
    network.add_cell(ACT0019)
    network.add_cell(CON0027)
    network.add_cell(CON0004)
    network.add_cell(PAR0010)
    network.add_cell(ACT0022)
    network.add_cell(ACT0030)
    network.add_cell(PAR0009)
    network.add_cell(ACT0025)
    network.add_cell(ACT0008)
    network.add_cell(ACT0016)
    owner["Player_2D"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__Player_2D')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("Player_2D")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
