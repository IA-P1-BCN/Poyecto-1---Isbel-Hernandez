from enum import Enum
from time import monotonic
from decimal import Decimal


class VehicleState(Enum):
    STOPPED = "stopped"
    MOVING = "moving"


class Trip:
    def __init__(
        self,
        clock=monotonic,
        stopped_rate=Decimal("0.02"),
        moving_rate=Decimal("0.05"),
    ):
        self.clock = clock
        self.stopped_rate = stopped_rate
        self.moving_rate = moving_rate
        self.is_active = False
        self.state = None
        self.total_fare = Decimal("0")
        self.last_updated = None
        self.started_at = None
        self.duration = 0

    def start(self):
        self.is_active = True
        self.state = VehicleState.STOPPED
        self.total_fare = Decimal("0")
        self.last_updated = self.clock()
        self.started_at = self.last_updated

    def _current_rate(self):
        if self.state == VehicleState.STOPPED:
            return self.stopped_rate
        return self.moving_rate

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
        self.duration = self.clock() - self.started_at
        self.is_active = False
        return self.total_fare