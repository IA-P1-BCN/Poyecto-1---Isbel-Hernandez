from src.application.taxi_service import TaxiService
from src.domain.trip import VehicleState


def main():
    service = TaxiService()

    password = input("Contraseña: ")

    if not service.authenticate(password):
       print("Contraseña incorrecta")
       return

    print("Taxímetro")
    print("Comandos: start, moving, stopped, finish, history, exit")

    while True:
        command = input("> ").strip().lower()

        if command == "history":
            history = service.get_history()

            for trip in history:
                print(trip)

            continue

        if command == "exit":
            return

        if command == "start":
            service.start_trip()
            print("Carrera iniciada")

            while service.trip.is_active:
                command = input("> ").strip().lower()

                if command == "moving":
                    service.change_state(VehicleState.MOVING)
                    print("Vehículo en movimiento")

                elif command == "stopped":
                    service.change_state(VehicleState.STOPPED)
                    print("Vehículo parado")

                elif command == "finish":
                    total = service.finish_trip()
                    print(f"Total: {total:.2f} €")

                else:
                    print("Comando no válido")
                    service.log_error(f"Comando no válido: {command}")
                    

        else:
            print("Comando no válido")


if __name__ == "__main__":
    main()