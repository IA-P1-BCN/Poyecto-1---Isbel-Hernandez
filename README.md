# Taxímetro TaxiTech Solutions

Aplicación de taxímetro desarrollada para **TaxiTech Solutions** como proyecto académico.

El sistema permite gestionar carreras, calcular tarifas según el estado del vehículo, almacenar el historial de carreras, registrar operaciones y autenticar al usuario.

## Tecnologías

- Python 3
- Tkinter
- Pytest
- Git / GitHub
- JSON
- JSONL

## Funcionalidades

- Inicio y finalización de carreras.
- Cambio entre vehículo parado y en movimiento.
- Cálculo de tarifa según el tiempo y el estado del vehículo.
- Tarifas configurables mediante un archivo JSON.
- Persistencia del historial de carreras.
- Consulta del historial del día.
- Registro de operaciones mediante logging.
- Autenticación mediante contraseña.
- Interfaz de línea de comandos (CLI).
- Interfaz gráfica (GUI) con Tkinter.
- Actualización del importe en tiempo real durante una carrera.

## Estructura del proyecto

```text
Poyecto-1---Isbel-Hernandez/
│
├── config/
│   ├── tariffs.json
│   └── auth.json
│
├── data/
│   ├── history.jsonl
│   └── taximetro.log
│
├── src/
│   ├── application/
│   │   └── taxi_service.py
│   │
│   ├── domain/
│   │   └── trip.py
│   │
│   ├── infrastructure/
│   │   ├── auth.py
│   │   ├── config.py
│   │   ├── history.py
│   │   └── logger.py
│   │
│   └── interfaces/
│       ├── cli.py
│       └── gui.py
│
└── tests/
    ├── test_auth.py
    ├── test_cli.py
    ├── test_config.py
    ├── test_history.py
    ├── test_logger.py
    └── test_trip.py
```

## Arquitectura

El proyecto está organizado en diferentes capas:

### Domain

Contiene la lógica principal del taxímetro.

`Trip` gestiona el estado de la carrera, el tiempo transcurrido y el cálculo de la tarifa.

### Application

`TaxiService` coordina las operaciones de la aplicación y conecta la lógica de negocio con la infraestructura.

### Infrastructure

Gestiona elementos externos a la lógica de negocio:

- Configuración de tarifas.
- Persistencia del historial.
- Logging.
- Autenticación.

### Interfaces

Contiene las interfaces desde las que se puede utilizar la aplicación:

- CLI.
- GUI con Tkinter.

## Tarifas

Las tarifas se encuentran en:

```text
config/tariffs.json
```

Actualmente:

```json
{
  "stopped_rate": "0.02",
  "moving_rate": "0.05"
}
```

Los valores representan el precio por segundo según el estado del vehículo.

## Ejecución

Activar el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

### CLI

Ejecutar:

```powershell
python -m src.interfaces.cli
```

La aplicación solicita una contraseña antes de acceder al taxímetro.

### GUI

Ejecutar:

```powershell
python -m src.interfaces.gui
```

Se abrirá la interfaz gráfica del taxímetro.

## Tests

Para ejecutar todos los tests:

```powershell
python -m pytest
```

El proyecto cuenta actualmente con **13 tests**.

## Seguridad

La contraseña no se almacena en texto plano.

El sistema utiliza:

- Salt aleatorio.
- PBKDF2-HMAC-SHA256.
- Comparación segura mediante `compare_digest`.

El archivo `config/auth.json` está incluido en `.gitignore` para evitar subir las credenciales almacenadas al repositorio.

## Historial

Las carreras finalizadas se almacenan en:

```text
data/history.jsonl
```

Cada carrera registra información como:

- Fecha.
- Duración.
- Importe final.

El sistema permite consultar las carreras correspondientes al día actual.

## Logging

Las operaciones del sistema se registran en:

```text
data/taximetro.log
```

El archivo de logs está excluido del repositorio mediante `.gitignore`.

## Estado del proyecto

### Fase 1 — CLI

- [x] Gestión de carreras.
- [x] Estados parado/en movimiento.
- [x] Cálculo de tarifas.
- [x] Tests.

### Fase 2 — Observabilidad y persistencia

- [x] Tarifas externas.
- [x] Persistencia del historial.
- [x] Consulta del historial.
- [x] Logging.
- [x] Servicio de aplicación.

### Fase 3 — Seguridad e interfaz

- [x] Autenticación mediante contraseña.
- [x] Hash seguro de contraseña.
- [x] Interfaz gráfica con Tkinter.
- [x] Actualización de tarifa en tiempo real.

### Fase 4 — Versión de producción

Pendiente de implementación:

- [ ] Migración del historial a una base de datos relacional.
- [ ] API REST.
- [ ] Panel web.
- [ ] Despliegue mediante Docker.
- [ ] Persistencia de datos mediante volúmenes.
