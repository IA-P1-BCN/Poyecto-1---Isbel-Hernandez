from src.interfaces.cli import main

def test_cli_starts_trip(monkeypatch, capsys):
    commands = iter(["test123","start", "finish", "exit"])

    monkeypatch.setattr("builtins.input", lambda _: next(commands))

    main()

    output = capsys.readouterr().out

    assert "Carrera iniciada" in output
    assert "Total:" in output

def test_cli_changes_vehicle_state(monkeypatch, capsys):
    commands = iter(["test123","start", "moving", "stopped", "finish", "exit"])

    monkeypatch.setattr("builtins.input", lambda _: next(commands))

    main()

    output = capsys.readouterr().out

    assert "Vehículo en movimiento" in output
    assert "Vehículo parado" in output

def test_cli_allows_multiple_trips(monkeypatch, capsys):
    commands = iter(["test123","start", "finish", "start", "finish", "exit"])

    monkeypatch.setattr("builtins.input", lambda _: next(commands))

    main()

    output = capsys.readouterr().out

    assert output.count("Carrera iniciada") == 2
    assert output.count("Total:") == 2        