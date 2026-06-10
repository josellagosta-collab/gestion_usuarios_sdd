# PRD - Aplicación de Gestión de Usuarios

## Objetivo

Crear una aplicación de consola en Python para gestionar usuarios.

## Funcionalidades

La aplicación debe permitir:

1. Crear usuarios.
2. Listar usuarios.
3. Modificar usuarios.
4. Eliminar usuarios.
5. Guardar los datos en un archivo JSON.

## Datos de cada usuario

Cada usuario tendrá:

- id
- nombre
- apellidos
- email
- contraseña

## Reglas de negocio

- El email es obligatorio.
- El nombre es obligatorio.
- El email debe ser único.
- La contraseña debe tener al menos 8 caracteres.
- No se puede modificar un usuario que no exista.
- No se puede eliminar un usuario que no exista.

## Archivo de datos

Los usuarios se guardarán en:

```text
usuarios.json
```

## Criterios de aceptación

### Alta correcta

Dado un usuario con datos válidos, cuando se registra, entonces aparece en la lista de usuarios.

### Email duplicado

Dado un email ya existente, cuando se intenta registrar otro usuario con ese email, entonces el sistema muestra un error.

### Contraseña corta

Dada una contraseña de menos de 8 caracteres, cuando se intenta registrar el usuario, entonces el sistema muestra un error.

### Eliminación

Dado un usuario existente, cuando se elimina, entonces desaparece del listado.