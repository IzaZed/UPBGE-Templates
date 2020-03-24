#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionOr()
    PAR0001 = bgelogic.ParameterMathFun()
    PAR0002 = bgelogic.ParameterGetGlobalValue()
    PAR0003 = bgelogic.ParameterGetGlobalValue()
    PAR0004 = bgelogic.ParamOwnerObject()
    ACT0005 = bgelogic.ActionSetObjectAttribute()
    ACT0006 = bgelogic.ActionSetGlobalValue()
    ACT0007 = bgelogic.ActionSetGlobalValue()
    ACT0008 = bgelogic.ActionSetGlobalValue()
    CON0009 = bgelogic.ConditionOr()
    ACT0010 = bgelogic.InvertBool()
    ACT0011 = bgelogic.InvertBool()
    ACT0012 = bgelogic.ActionSetGlobalValue()
    CON0013 = bgelogic.ConditionKeyPressed()
    CON0014 = bgelogic.ConditionKeyPressed()
    CON0015 = bgelogic.ConditionKeyPressed()
    CON0016 = bgelogic.ConditionKeyPressed()
    ACT0017 = bgelogic.ActionSetGlobalValue()
    ACT0018 = bgelogic.ActionSetGlobalValue()
    ACT0019 = bgelogic.ActionApplyLocation()
    CON0020 = bgelogic.ConditionOnInit()
    ACT0021 = bgelogic.ActionSetGlobalValue()
    CON0022 = bgelogic.ConditionOr()
    PAR0023 = bgelogic.ParameterVector3Simple()
    CON0000.condition_a = ACT0006.OUT
    CON0000.condition_b = ACT0007.OUT
    PAR0001.formula = "atan2(a,b)"
    PAR0001.a = PAR0003
    PAR0001.b = PAR0002
    PAR0002.data_id = "movement"
    PAR0002.key = "y"
    PAR0003.data_id = "movement"
    PAR0003.key = "x"
    ACT0005.condition = CON0022
    ACT0005.game_object = PAR0004
    ACT0005.attribute_value = PAR0023.OUTV
    ACT0005.value_type = 'worldOrientation'
    ACT0006.condition = CON0014
    ACT0006.data_id = "movement"
    ACT0006.persistent = False
    ACT0006.key = "y"
    ACT0006.value = -1
    ACT0007.condition = CON0013
    ACT0007.data_id = "movement"
    ACT0007.persistent = False
    ACT0007.key = "y"
    ACT0007.value = 1
    ACT0008.condition = CON0016
    ACT0008.data_id = "movement"
    ACT0008.persistent = False
    ACT0008.key = "x"
    ACT0008.value = 1
    CON0009.condition_a = ACT0008.OUT
    CON0009.condition_b = ACT0012.OUT
    ACT0010.value = CON0000
    ACT0011.value = CON0009
    ACT0012.condition = CON0015
    ACT0012.data_id = "movement"
    ACT0012.persistent = False
    ACT0012.key = "x"
    ACT0012.value = -1
    CON0013.key_code = bge.events.DKEY
    CON0013.pulse = True
    CON0014.key_code = bge.events.AKEY
    CON0014.pulse = True
    CON0015.key_code = bge.events.SKEY
    CON0015.pulse = True
    CON0016.key_code = bge.events.WKEY
    CON0016.pulse = True
    ACT0017.condition = ACT0011.OUT
    ACT0017.data_id = "movement"
    ACT0017.persistent = False
    ACT0017.key = "x"
    ACT0017.value = 0
    ACT0018.condition = ACT0010.OUT
    ACT0018.data_id = "movement"
    ACT0018.persistent = False
    ACT0018.key = "y"
    ACT0018.value = 0
    ACT0019.local = True
    ACT0019.condition = ACT0005.OUT
    ACT0019.game_object = PAR0004
    ACT0019.movement = mathutils.Vector((0.0, -0.11999999731779099, 0.0))
    ACT0021.condition = CON0020
    ACT0021.data_id = "movement"
    ACT0021.persistent = False
    ACT0021.key = "aim"
    ACT0021.value = 0.0
    CON0022.condition_a = CON0009
    CON0022.condition_b = CON0000
    PAR0023.input_x = 0.0
    PAR0023.input_y = 0.0
    PAR0023.input_z = PAR0001
    network.add_cell(PAR0002)
    network.add_cell(PAR0004)
    network.add_cell(CON0013)
    network.add_cell(CON0015)
    network.add_cell(CON0020)
    network.add_cell(PAR0003)
    network.add_cell(ACT0007)
    network.add_cell(ACT0012)
    network.add_cell(CON0016)
    network.add_cell(ACT0021)
    network.add_cell(PAR0001)
    network.add_cell(ACT0008)
    network.add_cell(CON0014)
    network.add_cell(PAR0023)
    network.add_cell(ACT0006)
    network.add_cell(CON0000)
    network.add_cell(CON0009)
    network.add_cell(ACT0011)
    network.add_cell(CON0022)
    network.add_cell(ACT0005)
    network.add_cell(ACT0017)
    network.add_cell(ACT0019)
    network.add_cell(ACT0010)
    network.add_cell(ACT0018)
    owner["TOP_DOWN"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__TOP_DOWN')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("TOP_DOWN")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
