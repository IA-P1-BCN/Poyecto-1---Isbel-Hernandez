from datetime import datetime

from src.domain.trip import Trip, VehicleState
from src.infrastructure.history import save_trip
from src.infrastructure.logger import setup_logger
from src.infrastructure.config import load_tariffs


class TaxiService:
    def __init__(self):
        self.logger = setup_logger()
        self.trip = None

    def start_trip(self):
        tariffs = load_tariffs()
        self.trip = Trip(
            stopped_rate=tariffs["stopped_rate"],
            moving_rate=tariffs["moving_rate"],
        )
        self.trip.start()
        self.logger.info("Carrera iniciada")

    def change_state(self, state):
        self.trip.change_state(state)

        if state == VehicleState.MOVING:
            self.logger.info("Vehículo en movimiento")
        else:
            self.logger.info("Vehículo parado")

    def finish_trip(self):
        total = self.trip.finish()

        self.logger.info("Carrera finalizada")

        trip_data = {
            "date": datetime.now().isoformat(),
            "duration": self.trip.duration,
            "amount": str(total),
        }

        save_trip(trip_data)

        return total

    def get_history(self):
        from src.infrastructure.history import load_history
        return load_history()

    def log_error(self, message):
        self.logger.error(message)