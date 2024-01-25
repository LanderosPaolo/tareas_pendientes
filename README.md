# Tarea App

Esta es una aplicación simple de lista de tareas desarrollada en Django. Permite a los usuarios gestionar sus tareas, incluyendo la creación, edición y eliminación de tareas, así como la visualización de detalles.

## Contenido

1. [Vistas y Modelos](#vistas-y-modelos)
2. [URLs](#urls)
3. [Plantillas HTML](#plantillas-html)

## Vistas y Modelos

### Logueo (`Logueo`)

La vista `Logueo` maneja el inicio de sesión de los usuarios utilizando `LoginView` de Django. Después del inicio de sesión exitoso, redirige a la página de lista de tareas.

### PaginaRegistro (`PaginaRegistro`)

La vista `PaginaRegistro` permite a los usuarios registrarse en la aplicación utilizando `UserCreationForm` de Django. Después del registro exitoso, inicia sesión automáticamente y redirige a la página de lista de tareas.

### ListaPendientes (`ListaPendientes`)

Esta vista muestra la lista de tareas pendientes del usuario autenticado. Utiliza `ListView` y filtra las tareas según el usuario actual. También proporciona funcionalidad de búsqueda por título de tarea.

### DetalleTarea (`DetalleTarea`)

Muestra los detalles de una tarea específica utilizando `DetailView`.

### CrearTarea (`CrearTarea`)

Permite a los usuarios crear nuevas tareas utilizando `CreateView`. Asigna automáticamente el usuario actual a la tarea.

### EditarTarea (`EditarTarea`)

Permite a los usuarios editar tareas existentes utilizando `UpdateView`.

### EliminarTarea (`EliminarTarea`)

Permite a los usuarios eliminar tareas existentes utilizando `DeleteView`.

## URLs

Las URLs de la aplicación están definidas en el archivo `urls.py`.

- `/`: Lista de tareas pendientes.
- `/login/`: Página de inicio de sesión.
- `/registro/`: Página de registro de usuario.
- `/logout/`: Página de cierre de sesión.
- `/tarea/<int:pk>`: Detalles de una tarea específica.
- `/crear-tarea/`: Página para crear una nueva tarea.
- `/editar-tarea/<int:pk>/`: Página para editar una tarea existente.
- `/eliminar-tarea/<int:pk>/`: Página para eliminar una tarea existente.

## Plantillas HTML

### `base/index.html`

Esta es la plantilla base que se utiliza para las demás páginas. Define el diseño general y estilos CSS comunes.

### `base/tarea.html`

Plantilla para la página de detalles de una tarea específica.

### `base/crear_tarea.html`

Plantilla para la página de creación de una nueva tarea.

### `base/eliminar_tarea.html`

Plantilla para la página de confirmación de eliminación de una tarea.

### `base/registro.html`

Plantilla para la página de registro de usuario.

### `base/login.html`

Plantilla para la página de inicio de sesión.

Espero que encuentres útil esta documentación. ¡Disfruta utilizando la aplicación de lista de tareas!
