# Aplicación de Gestión de Usuarios

Proyecto desarrollado siguiendo una metodología SDD, donde primero se ha creado una especificación funcional en `PRD.md` y después se ha generado el código.

## Funcionalidades

- Crear usuarios
- Listar usuarios
- Modificar usuarios
- Eliminar usuarios
- Guardar datos en JSON

## Estructura del proyecto

```text
gestion_usuarios_sdd/
│
├── PRD.md
├── README.md
├── main.py
├── usuario.py
├── gestor_usuarios.py
├── usuarios.json
└── test_gestor_usuarios.py
```

## Ejecutar la aplicación

```bash
python main.py
```

o en Linux:

```bash
python3 main.py
```

## Ejecutar pruebas

```bash
pytest
```

## Metodología utilizada

El proyecto sigue el flujo SDD:

```text
Especificación → IA → Código → Pruebas → Git → Documentación
```