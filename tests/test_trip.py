from decimal import Decimal
from src.domain.trip import Trip, VehicleState


def test_start_activates_trip():
    trip = Trip()

    trip.start()

    assert trip.is_active is True
    assert trip.state == VehicleState.STOPPED

class FakeClock:
    def __init__(self):
        self.now = 0

    def __call__(self):
        return self.now

    def advance(self, seconds):
        self.now += seconds

def test_trip_accumulates_fare_over_time():
    clock = FakeClock()
    trip = Trip(clock=clock)

    trip.start()
    clock.advance(10)

    trip.finish()

    assert trip.total_fare == Decimal("0.20")        

def test_trip_uses_moving_rate_after_state_change():
    clock = FakeClock()
    trip = Trip(clock=clock)

    trip.start()
    clock.advance(10)

    trip.change_state(VehicleState.MOVING)
    clock.advance(10)

    trip.finish()

    assert trip.total_fare == Decimal("0.70")      

def test_trip_accumulates_fare_across_state_changes():
    clock = FakeClock()
    trip = Trip(clock=clock)

    trip.start()
    clock.advance(10)

    trip.change_state(VehicleState.MOVING)
    clock.advance(20)

    trip.change_state(VehicleState.STOPPED)
    clock.advance(10)

    trip.finish()

    assert trip.total_fare == Decimal("1.40")          

def test_finish_deactivates_trip_and_returns_fare():
    clock = FakeClock()
    trip = Trip(clock=clock)

    trip.start()
    clock.advance(10)

    total = trip.finish()

    assert trip.is_active is False
    assert total == Decimal("0.20")    