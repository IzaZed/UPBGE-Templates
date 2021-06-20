# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    PAR0000 = bgelogic.ParameterSimpleValue()
    ACT0001 = bgelogic.ActionSetGameObjectGameProperty()
    CON0002 = bgelogic.ConditionValueChanged()
    ACT0003 = bgelogic.ActionCharacterJump()
    CON0004 = bgelogic.ConditionAnd()
    CON0005 = bgelogic.ConditionKeyPressed()
    CON0006 = bgelogic.ConditionOr()
    ACT0007 = bgelogic.ActionSetGameObjectGameProperty()
    PAR0008 = bgelogic.ParameterObjectProperty()
    PAR0009 = bgelogic.InterpolateValue()
    CON0010 = bgelogic.ConditionKeyPressed()
    CON0011 = bgelogic.ConditionKeyPressed()
    PAR0012 = bgelogic.ValueSwitch()
    PAR0013 = bgelogic.ValueSwitch()
    PAR0014 = bgelogic.ValueSwitch()
    ACT0015 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0016 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0017 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0018 = bgelogic.ActionSetGameObjectGameProperty()
    CON0019 = bgelogic.ConditionValueTrigger()
    PAR0020 = bgelogic.ParameterObjectProperty()
    PAR0021 = bgelogic.ParameterObjectProperty()
    CON0022 = bgelogic.ConditionValueTrigger()
    CON0023 = bgelogic.ConditionValueChanged()
    CON0024 = bgelogic.ConditionValueTrigger()
    PAR0025 = bgelogic.InterpolateValue()
    CON0026 = bgelogic.ConditionOnUpdate()
    CON0027 = bgelogic.ConditionValueChanged()
    PAR0028 = bgelogic.ValueSwitch()
    PAR0029 = bgelogic.ParameterGetCharacterInfo()
    PAR0000.value = 0.10000000149011612
    ACT0001.condition = CON0002
    ACT0001.game_object = "NLO:U_O"
    ACT0001.property_name = "jumped"
    ACT0001.property_value = CON0002.CURRENT_VALUE
    CON0002.initialize = False
    CON0002.current_value = ACT0003.OUT
    ACT0003.condition = CON0004
    ACT0003.game_object = "NLO:U_O"
    CON0004.condition_a = PAR0029.ON_GROUND
    CON0004.condition_b = CON0005
    CON0005.key_code = bge.events.SPACEKEY
    CON0005.pulse = False
    CON0006.condition_a = CON0011
    CON0006.condition_b = CON0010
    ACT0007.condition = CON0026
    ACT0007.game_object = "NLO:U_O"
    ACT0007.property_name = "running"
    ACT0007.property_value = PAR0009
    PAR0008.game_object = "NLO:U_O"
    PAR0008.property_name = "running"
    PAR0009.value_a = PAR0008
    PAR0009.value_b = PAR0012.VAL
    PAR0009.factor = PAR0014.VAL
    CON0010.key_code = bge.events.DKEY
    CON0010.pulse = True
    CON0011.key_code = bge.events.AKEY
    CON0011.pulse = True
    PAR0012.condition = CON0006
    PAR0012.val_a = PAR0013.VAL
    PAR0012.val_b = 0.0
    PAR0013.condition = CON0011
    PAR0013.val_a = -1.0
    PAR0013.val_b = 1.0
    PAR0014.condition = PAR0029.ON_GROUND
    PAR0014.val_a = PAR0000
    PAR0014.val_b = 0.029999999329447746
    ACT0015.condition = CON0022
    ACT0015.game_object = "NLO:U_O"
    ACT0015.property_name = "falling"
    ACT0015.property_value = 0.0
    ACT0016.condition = CON0023
    ACT0016.game_object = "NLO:U_O"
    ACT0016.property_name = "landed"
    ACT0016.property_value = CON0023.CURRENT_VALUE
    ACT0017.condition = CON0027
    ACT0017.game_object = "NLO:U_O"
    ACT0017.property_name = "start_falling"
    ACT0017.property_value = CON0027.CURRENT_VALUE
    ACT0018.condition = CON0026
    ACT0018.game_object = "NLO:U_O"
    ACT0018.property_name = "grounded"
    ACT0018.property_value = PAR0025
    CON0019.monitored_value = PAR0029.ON_GROUND
    CON0019.trigger_value = True
    PAR0020.game_object = "NLO:U_O"
    PAR0020.property_name = "start_falling"
    PAR0021.game_object = "NLO:U_O"
    PAR0021.property_name = "grounded"
    CON0022.monitored_value = PAR0020
    CON0022.trigger_value = True
    CON0023.initialize = False
    CON0023.current_value = CON0019
    CON0024.monitored_value = PAR0029.ON_GROUND
    CON0024.trigger_value = False
    PAR0025.value_a = PAR0021
    PAR0025.value_b = PAR0028.VAL
    PAR0025.factor = 0.30000001192092896
    CON0027.initialize = False
    CON0027.current_value = CON0024
    PAR0028.condition = PAR0029.ON_GROUND
    PAR0028.val_a = 1.0
    PAR0028.val_b = 0.0
    PAR0029.local = True
    PAR0029.game_object = "NLO:U_O"
    network.add_cell(PAR0000)
    network.add_cell(CON0005)
    network.add_cell(PAR0008)
    network.add_cell(CON0010)
    network.add_cell(PAR0020)
    network.add_cell(CON0022)
    network.add_cell(CON0026)
    network.add_cell(PAR0029)
    network.add_cell(CON0004)
    network.add_cell(CON0011)
    network.add_cell(PAR0013)
    network.add_cell(ACT0015)
    network.add_cell(CON0019)
    network.add_cell(CON0023)
    network.add_cell(PAR0028)
    network.add_cell(ACT0003)
    network.add_cell(PAR0014)
    network.add_cell(PAR0021)
    network.add_cell(PAR0025)
    network.add_cell(CON0002)
    network.add_cell(ACT0016)
    network.add_cell(ACT0018)
    network.add_cell(ACT0001)
    network.add_cell(CON0024)
    network.add_cell(CON0006)
    network.add_cell(PAR0012)
    network.add_cell(CON0027)
    network.add_cell(PAR0009)
    network.add_cell(ACT0007)
    network.add_cell(ACT0017)
    owner["IGNLTree_Player_2D_Properties"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__Player_2D_Properties')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_Player_2D_Properties")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
