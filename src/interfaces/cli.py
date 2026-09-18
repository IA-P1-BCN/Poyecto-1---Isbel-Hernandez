from src.domain.trip import Trip, VehicleState


def main():
    print("Taxímetro")
    print("Comandos: start, moving, stopped, finish, exit")

    while True:
        command = input("> ").strip().lower()

        if command == "exit":
            return

        if command == "start":
            trip = Trip()
            trip.start()

            print("Carrera iniciada")

            while trip.is_active:
                command = input("> ").strip().lower()

                if command == "moving":
                    trip.change_state(VehicleState.MOVING)
                    print("Vehículo en movimiento")

                elif command == "stopped":
                    trip.change_state(VehicleState.STOPPED)
                    print("Vehículo parado")

                elif command == "finish":
                    total = trip.finish()
                    print(f"Total: {total:.2f} €")

                else:
                    print("Comando no válido")

        else:
            print("Comando no válido")


if __name__ == "__main__":
    main()