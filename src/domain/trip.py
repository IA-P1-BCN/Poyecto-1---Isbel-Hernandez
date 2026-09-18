from enum import Enum
from time import monotonic



class VehicleState(Enum):
    STOPPED = "stopped"
    MOVING = "moving"

class Trip:
    def __init__(self):
        self.is_active = False
        self.state = None
        self.total_fare = 0
        self.last_update = None

    def start(self):
        self.is_active = True
        self.state = VehicleState.STOPPED
        self.total_fare = 0
        self.last_updated = monotonic()        

    