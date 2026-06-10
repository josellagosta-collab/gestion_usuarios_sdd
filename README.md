# Aplicación de Gestión de Usuarios

Proyecto sencillo en Python para gestionar usuarios desde la consola. Implementa
operaciones CRUD (crear, listar, modificar, eliminar) y persiste los datos en
un archivo JSON de forma atómica. Las contraseñas se almacenan como hashes
seguros con sal (no en texto plano).

## Funcionalidades

- Crear usuarios
- Listar usuarios
- Modificar usuarios
- Eliminar usuarios
- Guardar datos en JSON con persistencia atómica
- Almacenar contraseñas como hashes seguros con sal

## Estructura del proyecto

```text
Gestión de usuarios SDD/
├── PRD.md
├── README.md
├── pyproject.toml
├── requirements-dev.txt
├── main.py              # CLI y modo interactivo
├── usuario.py           # Modelo de dominio
├── gestor_usuarios.py   # Lógica de negocio
├── repositorio_usuarios.py # Persistencia (JSON, atómica)
├── usuarios.json        # Datos de ejemplo
├── test_*.py            # Pruebas unitarias
```

## Requisitos

- Python 3.10 o superior

## Instalación

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

## Uso

### Modo interactivo

```bash
python main.py interactivo
```

### Uso como CLI (no interactivo)

Crear usuario:

```bash
python main.py crear --nombre "Jose" --apellidos "Lopez" --email jose@test.com --password 12345678
```

Listar usuarios:

```bash
python main.py listar
```

Modificar usuario:

```bash
python main.py modificar --id 1 --nombre "Jose" --apellidos "Perez" --email jose@nuevo.com
```

Eliminar usuario:

```bash
python main.py eliminar --id 1
```

## Ejecutar pruebas

```bash
pytest
```

## Calidad y formateo

Usa `ruff` y `black` para comprobar estilo y formateo:

```bash
python -m ruff check .
python -m black .
```

## Integración continua

El proyecto incluye un flujo de GitHub Actions que ejecuta las pruebas y la
comprobación de estilo en cada push y pull request (`.github/workflows/python-ci.yml`).

## Contribuir

Si quieres contribuir:

- Abre un issue describiendo la propuesta.
- Crea un branch y un PR usando el flujo habitual.
- Asegúrate de que `pytest`, `ruff` y `black` pasan antes de enviar el PR.

## Notas

- Las contraseñas se almacenan como hashes seguros con sal y no en texto plano.
- La persistencia de usuarios usa una escritura atómica para reducir el riesgo de
  corrupción de datos.
- El proyecto está diseñado para ser extensible a otras interfaces (API, web)
  sin modificar la lógica de negocio.

## Licencia

Por defecto este repositorio no incluye una licencia; añade una `LICENSE` si
quieres compartir el código públicamente.
