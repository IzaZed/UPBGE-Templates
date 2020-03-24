#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.ParameterPythonModuleFunction()
    PAR0001 = bgelogic.ParamOwnerObject()
    ACT0002 = bgelogic.ActionSetGameObjectGameProperty()
    CON0003 = bgelogic.ConditionOnInit()
    ACT0004 = bgelogic.InitEmptyDict()
    ACT0005 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0006 = bgelogic.ActivateActuatorByName()
    ACT0000.condition = CON0003
    ACT0000.module_name = "vehi"
    ACT0000.module_func = "create"
    ACT0000.use_arg = True
    ACT0000.arg = PAR0001
    ACT0002.condition = ACT0000.OUT
    ACT0002.game_object = PAR0001
    ACT0002.property_name = "_car_wrapper"
    ACT0002.property_value = ACT0000.VAL
    ACT0004.condition = CON0003
    ACT0005.condition = ACT0004.OUT
    ACT0005.game_object = None
    ACT0005.property_name = "_args"
    ACT0005.property_value = ACT0004.DICT
    ACT0006.condition = ACT0002.OUT
    ACT0006.actuator = "FXAA"
    network.add_cell(PAR0001)
    network.add_cell(CON0003)
    network.add_cell(ACT0000)
    network.add_cell(ACT0004)
    network.add_cell(ACT0002)
    network.add_cell(ACT0006)
    network.add_cell(ACT0005)
    owner["vehicule_part"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__vehicule_part')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("vehicule_part")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
