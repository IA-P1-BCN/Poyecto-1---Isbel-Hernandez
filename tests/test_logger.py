from src.infrastructure.logger import setup_logger


def test_logger_writes_to_file(tmp_path, monkeypatch):
    log_file = tmp_path / "taximetro.log"

    monkeypatch.setattr(
        "src.infrastructure.logger.LOG_PATH",
        log_file
    )

    logger = setup_logger()

    logger.info("Carrera iniciada")
    logger.info("Vehículo en movimiento")
    logger.error("Comando no válido: abc")
    logger.info("Carrera finalizada")

    content = log_file.read_text()

    assert "Carrera iniciada" in content
    assert "Vehículo en movimiento" in content
    assert "Comando no válido: abc" in content
    assert "Carrera finalizada" in content 