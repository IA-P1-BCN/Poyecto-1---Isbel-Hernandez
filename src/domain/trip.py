from enum import Enum
from time import monotonic
from decimal import Decimal



class VehicleState(Enum):
    STOPPED = "stopped"
    MOVING = "moving"

STOPPED_RATE = Decimal("0.02")
MOVING_RATE = Decimal("0.05")   

class Trip:
    def __init__(self, clock=monotonic):
        self.clock = clock
        self.is_active = False
        self.state = None
        self.total_fare = Decimal("0")
        self.last_update = None

    def start(self):
        self.is_active = True
        self.state = VehicleState.STOPPED
        self.total_fare = Decimal("0")
        self.last_updated = self.clock()     

    def _current_rate(self):
        if self.state == VehicleState.STOPPED:
            return STOPPED_RATE
        return MOVING_RATE         

    def _update_fare(self):
        now = self.clock()
        elapsed_seconds = Decimal(str(now - self.last_updated))
        self.total_fare += elapsed_seconds * self._current_rate()
        self.last_updated = now

    def change_state(self, new_state):
        self._update_fare()
        self.state = new_state

    def finish(self):
        self._update_fare()
        self.is_active = False
        return self.total_fare    
    