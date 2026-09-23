from src.domain.trip import Trip, VehicleState
from src.infrastructure.history import load_history, save_trip
from datetime import datetime
from src.infrastructure.logger import setup_logger


def main():
    logger = setup_logger()
    logger.info("Sistema iniciado")

    print("Taxímetro")
    print("Comandos: start, moving, stopped, finish, exit")

    while True:
        command = input("> ").strip().lower()

        if command == "history":
            history = load_history()

            for trip in history:
             print(trip)

            continue

        if command == "exit":
            return

        if command == "start":
            trip = Trip()
            trip.start()
            logger.info("Carrera iniciada")

            print("Carrera iniciada")

            while trip.is_active:
                command = input("> ").strip().lower()

                if command == "moving":
                    trip.change_state(VehicleState.MOVING)
                    print("Vehículo en movimiento")
                    logger.info("Vehículo en movimiento")

                elif command == "stopped":
                    trip.change_state(VehicleState.STOPPED)
                    print("Vehículo parado")
                    logger.info("Vehículo parado")

                elif command == "finish":
                    total = trip.finish()
                    logger.info("Carrera finalizada")

                    trip_data = {
                        "date" : datetime.now().isoformat(),
                        "duration" : trip.duration,
                        "amount" : str(total)
                     }

                    save_trip (trip_data)

                    print(f"Total: {total:.2f} €")

                else:
                    print("Comando no válido")
                    logger.error(f"Comando no válido: {command}")

        else:
            print("Comando no válido")


if __name__ == "__main__":
    main()