# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionKeyPressed()
    CON0001 = bgelogic.ConditionAnd()
    ACT0002 = bgelogic.ActionCharacterJump()
    CON0003 = bgelogic.ConditionValueChanged()
    ACT0004 = bgelogic.ActionSetGameObjectGameProperty()
    CON0005 = bgelogic.ConditionValueChanged()
    PAR0006 = bgelogic.ValueSwitch()
    CON0007 = bgelogic.ConditionOnUpdate()
    PAR0008 = bgelogic.InterpolateValue()
    ACT0009 = bgelogic.ActionSetGameObjectGameProperty()
    CON0010 = bgelogic.ConditionValueTrigger()
    ACT0011 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0012 = bgelogic.ActionSetGameObjectGameProperty()
    CON0013 = bgelogic.ConditionValueChanged()
    CON0014 = bgelogic.ConditionValueTrigger()
    ACT0015 = bgelogic.ActionSetGameObjectGameProperty()
    PAR0016 = bgelogic.ParameterObjectProperty()
    PAR0017 = bgelogic.ParameterObjectProperty()
    CON0018 = bgelogic.ConditionOr()
    ACT0019 = bgelogic.ActionSetGameObjectGameProperty()
    PAR0020 = bgelogic.ParameterObjectProperty()
    PAR0021 = bgelogic.InterpolateValue()
    CON0022 = bgelogic.ConditionKeyPressed()
    PAR0023 = bgelogic.ValueSwitch()
    PAR0024 = bgelogic.ValueSwitch()
    CON0025 = bgelogic.ConditionKeyPressed()
    ACT0026 = bgelogic.ActionGetCharacterInfo()
    CON0027 = bgelogic.ConditionValueTrigger()
    PAR0028 = bgelogic.ParameterSimpleValue()
    PAR0029 = bgelogic.ValueSwitch()
    CON0000.key_code = bge.events.SPACEKEY
    CON0000.pulse = False
    CON0001.condition_a = ACT0026.ON_GROUND
    CON0001.condition_b = CON0000
    ACT0002.condition = CON0001
    ACT0002.game_object = "NLO:U_O"
    CON0003.initialize = False
    CON0003.current_value = ACT0002.OUT
    ACT0004.condition = CON0003
    ACT0004.game_object = "NLO:U_O"
    ACT0004.property_name = "jumped"
    ACT0004.property_value = CON0003.CURRENT_VALUE
    CON0005.initialize = False
    CON0005.current_value = CON0010
    PAR0006.condition = ACT0026.ON_GROUND
    PAR0006.val_a = 0.0
    PAR0006.val_b = 1.0
    PAR0008.value_a = PAR0016
    PAR0008.value_b = PAR0006.VAL
    PAR0008.factor = 0.30000001192092896
    ACT0009.condition = CON0007
    ACT0009.game_object = "NLO:U_O"
    ACT0009.property_name = "grounded"
    ACT0009.property_value = PAR0008
    CON0010.monitored_value = ACT0026.ON_GROUND
    CON0010.trigger_value = False
    ACT0011.condition = CON0013
    ACT0011.game_object = "NLO:U_O"
    ACT0011.property_name = "landed"
    ACT0011.property_value = CON0013.CURRENT_VALUE
    ACT0012.condition = CON0014
    ACT0012.game_object = "NLO:U_O"
    ACT0012.property_name = "falling"
    ACT0012.property_value = 0.0
    CON0013.initialize = False
    CON0013.current_value = CON0027
    CON0014.monitored_value = PAR0017
    CON0014.trigger_value = True
    ACT0015.condition = CON0005
    ACT0015.game_object = "NLO:U_O"
    ACT0015.property_name = "start_falling"
    ACT0015.property_value = CON0005.CURRENT_VALUE
    PAR0016.game_object = "NLO:U_O"
    PAR0016.property_name = "grounded"
    PAR0017.game_object = "NLO:U_O"
    PAR0017.property_name = "start_falling"
    CON0018.condition_a = CON0025
    CON0018.condition_b = CON0022
    ACT0019.condition = CON0007
    ACT0019.game_object = "NLO:U_O"
    ACT0019.property_name = "running"
    ACT0019.property_value = PAR0021
    PAR0020.game_object = "NLO:U_O"
    PAR0020.property_name = "running"
    PAR0021.value_a = PAR0020
    PAR0021.value_b = PAR0023.VAL
    PAR0021.factor = PAR0029.VAL
    CON0022.key_code = bge.events.DKEY
    CON0022.pulse = True
    PAR0023.condition = CON0018
    PAR0023.val_a = 0.0
    PAR0023.val_b = PAR0024.VAL
    PAR0024.condition = CON0025
    PAR0024.val_a = 1.0
    PAR0024.val_b = -1.0
    CON0025.key_code = bge.events.AKEY
    CON0025.pulse = True
    ACT0026.condition = True
    ACT0026.game_object = "NLO:U_O"
    CON0027.monitored_value = ACT0026.ON_GROUND
    CON0027.trigger_value = True
    PAR0028.value = 0.10000000149011612
    PAR0029.condition = ACT0026.ON_GROUND
    PAR0029.val_a = 0.029999999329447746
    PAR0029.val_b = PAR0028
    network.add_cell(CON0000)
    network.add_cell(CON0007)
    network.add_cell(PAR0016)
    network.add_cell(PAR0020)
    network.add_cell(CON0022)
    network.add_cell(CON0025)
    network.add_cell(PAR0028)
    network.add_cell(PAR0017)
    network.add_cell(PAR0024)
    network.add_cell(CON0014)
    network.add_cell(CON0018)
    network.add_cell(PAR0023)
    network.add_cell(ACT0012)
    network.add_cell(ACT0026)
    network.add_cell(PAR0029)
    network.add_cell(CON0001)
    network.add_cell(PAR0006)
    network.add_cell(CON0010)
    network.add_cell(PAR0021)
    network.add_cell(ACT0002)
    network.add_cell(CON0005)
    network.add_cell(ACT0015)
    network.add_cell(CON0027)
    network.add_cell(CON0003)
    network.add_cell(PAR0008)
    network.add_cell(CON0013)
    network.add_cell(ACT0004)
    network.add_cell(ACT0011)
    network.add_cell(ACT0009)
    network.add_cell(ACT0019)
    owner["Player_2D_Properties"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__Player_2D_Properties')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("Player_2D_Properties")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
