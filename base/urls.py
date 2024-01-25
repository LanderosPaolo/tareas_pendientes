# Importación de módulos y clases necesarios de Django
from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Logueo, PaginaRegistro
from django.contrib.auth.views import LogoutView

# Definición de las URL para la aplicación
urlpatterns = [
    path('', ListaPendientes.as_view(), name='tareas'),  # Página principal que muestra la lista de tareas pendientes
    path('login/', Logueo.as_view(), name='login'),  # Página de inicio de sesión
    path('registro/', PaginaRegistro.as_view(), name='registro'),  # Página de registro de usuario
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),  # Página de cierre de sesión
    path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),  # Página de detalles de una tarea específica
    path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),  # Página para crear una nueva tarea
    path('editar-tarea/<int:pk>/', EditarTarea.as_view(), name='editar-tarea'),  # Página para editar una tarea existente
    path('eliminar-tarea/<int:pk>/', EliminarTarea.as_view(), name='eliminar-tarea'),  # Página para eliminar una tarea existente
]
