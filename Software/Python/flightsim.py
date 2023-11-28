from MSFSPythonSimConnectMobiFlightExtension.src.simconnect_mobiflight import SimConnectMobiFlight
from MSFSPythonSimConnectMobiFlightExtension.src.mobiflight_variable_requests import MobiFlightVariableRequests
from SimConnect import  AircraftEvents

class FlightSim:
    def __init__(self):
        self.simConnect = SimConnectMobiFlight()
        self.events = AircraftEvents(self.simConnect)
        self.requests = MobiFlightVariableRequests(self.simConnect)
        self._events_memo = {}
        self.requests.clear_sim_variables()
    
    # list of events:
    # https://docs.flightsimulator.com/html/Programming_Tools/Event_IDs/Event_IDs.htm
    def event(self, name, value=None):
        if name not in self._events_memo:
            self._events_memo[name] = self.events.find(name)
        func = self._events_memo[name]
        if value is None:
            func()
        else:
            func(value)
    
    # list of variables:
    # https://docs.flightsimulator.com/html/Programming_Tools/SimVars/Simulation_Variables.htm
    def get(self, name):
        return self.requests.get(name)
    
    # list of A32NX LVars:
    # https://github.com/flybywiresim/aircraft/blob/master/fbw-a32nx/docs/a320-simvars.md
    def get_lvar(self, name):
        return self.get(f"(L:{name})")