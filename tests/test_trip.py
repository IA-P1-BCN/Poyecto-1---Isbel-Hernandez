import unittest

from src.domain.trip import Trip, VehicleState

class TripTests(unittest.TestCase):
    def test_start_activates_trip(self):
        trip = Trip()
        trip.start()

        self.assertTrue(trip.is_active)
        self.assertEqual(trip.state, VehicleState.STOPPED)