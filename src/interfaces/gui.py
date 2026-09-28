import tkinter as tk
from src.application.taxi_service import TaxiService
from src.domain.trip import VehicleState


def main():
    window = tk.Tk()
    service = TaxiService()
    window.title("Taxímetro")
    window.geometry("400x600")
    title = tk.Label(window, text="TAXÍMETRO", font=("Arial", 24))
    title.pack(pady=30)

    fare = tk.Label(window, text="0,00 €", font=("Arial", 40))
    fare.pack(pady=20)
    start_button = tk.Button(
    window,
    text="INICIAR CARRERA",
    command=lambda: (
    service.start_trip(),
    state.config(text="CARRERA INICIADA")
)
)
    start_button.pack(pady=10)

    moving_button = tk.Button(
    window,
    text="EN MOVIMIENTO",
    command=lambda: (
        service.change_state(VehicleState.MOVING),
        state.config(text="EN MOVIMIENTO")
    )
)
    moving_button.pack(pady=10)

    stopped_button = tk.Button(
    window,
    text="PARADO",
    command=lambda: (
        service.change_state(VehicleState.STOPPED),
        state.config(text="VEHÍCULO PARADO")
    )
)
    stopped_button.pack(pady=10)

    def finish_trip():
       total = service.finish_trip()
       fare.config(text=f"{total:.2f} €")
       state.config(text="CARRERA FINALIZADA")
    
    finish_button = tk.Button(
    window,
    text="FINALIZAR",
    command=finish_trip
)
    finish_button.pack(pady=10)

    state = tk.Label(window, text="VEHÍCULO PARADO", font=("Arial", 18))
    state.pack(pady=20)


    window.mainloop()


if __name__ == "__main__":
    main()