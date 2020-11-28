# MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionOr()
    ACT0001 = bgelogic.ActionSetGameObjectGameProperty()
    PAR0002 = bgelogic.ParameterObjectProperty()
    PAR0003 = bgelogic.InterpolateValue()
    CON0004 = bgelogic.ConditionKeyPressed()
    PAR0005 = bgelogic.ValueSwitch()
    PAR0006 = bgelogic.ValueSwitch()
    CON0007 = bgelogic.ConditionKeyPressed()
    PAR0008 = bgelogic.ParameterSimpleValue()
    CON0009 = bgelogic.ConditionKeyPressed()
    CON0010 = bgelogic.ConditionAnd()
    ACT0011 = bgelogic.ActionCharacterJump()
    CON0012 = bgelogic.ConditionValueChanged()
    ACT0013 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0014 = bgelogic.ActionGetCharacterInfo()
    CON0015 = bgelogic.ConditionValueChanged()
    PAR0016 = bgelogic.ValueSwitch()
    CON0017 = bgelogic.ConditionOnUpdate()
    PAR0018 = bgelogic.InterpolateValue()
    ACT0019 = bgelogic.ActionSetGameObjectGameProperty()
    CON0020 = bgelogic.ConditionValueTrigger()
    ACT0021 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0022 = bgelogic.ActionSetGameObjectGameProperty()
    CON0023 = bgelogic.ConditionValueChanged()
    CON0024 = bgelogic.ConditionValueTrigger()
    CON0025 = bgelogic.ConditionValueTrigger()
    ACT0026 = bgelogic.ActionSetGameObjectGameProperty()
    PAR0027 = bgelogic.ParameterObjectProperty()
    PAR0028 = bgelogic.ParameterObjectProperty()
    CON0000.condition_a = CON0007
    CON0000.condition_b = CON0004
    ACT0001.condition = CON0017
    ACT0001.game_object = "NLO:U_O"
    ACT0001.property_name = "running"
    ACT0001.property_value = PAR0003
    PAR0002.game_object = "NLO:U_O"
    PAR0002.property_name = "running"
    PAR0003.value_a = PAR0002
    PAR0003.value_b = PAR0005.VAL
    PAR0003.factor = PAR0008
    CON0004.key_code = bge.events.DKEY
    CON0004.pulse = True
    PAR0005.condition = CON0000
    PAR0005.val_a = 0.0
    PAR0005.val_b = PAR0006.VAL
    PAR0006.condition = CON0007
    PAR0006.val_a = 1.0
    PAR0006.val_b = -1.0
    CON0007.key_code = bge.events.AKEY
    CON0007.pulse = True
    PAR0008.value = 0.10000000149011612
    CON0009.key_code = bge.events.SPACEKEY
    CON0009.pulse = False
    CON0010.condition_a = ACT0014.ON_GROUND
    CON0010.condition_b = CON0009
    ACT0011.condition = CON0010
    ACT0011.game_object = "NLO:U_O"
    CON0012.initialize = False
    CON0012.current_value = ACT0011.OUT
    ACT0013.condition = CON0012
    ACT0013.game_object = "NLO:U_O"
    ACT0013.property_name = "jumped"
    ACT0013.property_value = CON0012.CURRENT_VALUE
    ACT0014.condition = True
    ACT0014.game_object = "NLO:U_O"
    CON0015.initialize = False
    CON0015.current_value = CON0020
    PAR0016.condition = ACT0014.ON_GROUND
    PAR0016.val_a = 0.0
    PAR0016.val_b = 1.0
    PAR0018.value_a = PAR0027
    PAR0018.value_b = PAR0016.VAL
    PAR0018.factor = 0.30000001192092896
    ACT0019.condition = CON0017
    ACT0019.game_object = "NLO:U_O"
    ACT0019.property_name = "grounded"
    ACT0019.property_value = PAR0018
    CON0020.monitored_value = ACT0014.ON_GROUND
    CON0020.trigger_value = False
    ACT0021.condition = CON0023
    ACT0021.game_object = "NLO:U_O"
    ACT0021.property_name = "landed"
    ACT0021.property_value = CON0023.CURRENT_VALUE
    ACT0022.condition = CON0025
    ACT0022.game_object = "NLO:U_O"
    ACT0022.property_name = "falling"
    ACT0022.property_value = 0.0
    CON0023.initialize = False
    CON0023.current_value = CON0024
    CON0024.monitored_value = ACT0014.ON_GROUND
    CON0024.trigger_value = True
    CON0025.monitored_value = PAR0028
    CON0025.trigger_value = True
    ACT0026.condition = CON0015
    ACT0026.game_object = "NLO:U_O"
    ACT0026.property_name = "start_falling"
    ACT0026.property_value = CON0015.CURRENT_VALUE
    PAR0027.game_object = "NLO:U_O"
    PAR0027.property_name = "grounded"
    PAR0028.game_object = "NLO:U_O"
    PAR0028.property_name = "start_falling"
    network.add_cell(PAR0002)
    network.add_cell(CON0004)
    network.add_cell(CON0007)
    network.add_cell(CON0009)
    network.add_cell(ACT0014)
    network.add_cell(PAR0016)
    network.add_cell(CON0020)
    network.add_cell(CON0024)
    network.add_cell(PAR0027)
    network.add_cell(CON0000)
    network.add_cell(PAR0006)
    network.add_cell(CON0010)
    network.add_cell(CON0015)
    network.add_cell(PAR0018)
    network.add_cell(CON0023)
    network.add_cell(ACT0026)
    network.add_cell(PAR0005)
    network.add_cell(ACT0011)
    network.add_cell(CON0017)
    network.add_cell(ACT0021)
    network.add_cell(PAR0028)
    network.add_cell(PAR0008)
    network.add_cell(ACT0019)
    network.add_cell(CON0025)
    network.add_cell(PAR0003)
    network.add_cell(ACT0022)
    network.add_cell(ACT0001)
    network.add_cell(CON0012)
    network.add_cell(ACT0013)
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
