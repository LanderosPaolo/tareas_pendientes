# Importación de módulos y clases necesarios de Django
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Tarea

# Definición de una clase basada en LoginView para gestionar el inicio de sesión
class Logueo(LoginView):
    template_name = 'base/login.html'  # Plantilla para la página de inicio de sesión
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tareas')  # Redirección después de un inicio de sesión exitoso

# Definición de una clase basada en FormView para la página de registro de usuario
class PaginaRegistro(FormView):
    template_name = 'base/registro.html'  # Plantilla para la página de registro
    form_class = UserCreationForm  # Formulario de creación de usuario predeterminado de Django
    redirect_authenticated_user = True
    success_url = reverse_lazy('tareas')  # Redirección después de un registro exitoso

    # Método que se ejecuta cuando el formulario es válido
    def form_valid(self, form):
        usuario = form.save()  # Guarda el nuevo usuario
        if usuario is not None:
            login(self.request, usuario)  # Inicia sesión automáticamente después del registro
        return super(PaginaRegistro, self).form_valid(form)

    # Método que se ejecuta en una solicitud GET a la vista
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tareas')  # Redirige al usuario autenticado a la lista de tareas
        return super(PaginaRegistro, self).get(*args, **kwargs)

# Definición de una clase basada en ListView para mostrar la lista de tareas pendientes
class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = 'tareas'  # Nombre del objeto en el contexto de la plantilla

    # Método para agregar datos adicionales al contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = context['tareas'].filter(usuario=self.request.user)
        context['count'] = context['tareas'].filter(completo=False).count()

        # Filtrar tareas por un valor de búsqueda proporcionado en la URL
        valor_buscado = self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            context['tareas'] =  context['tareas'].filter(titulo__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado
        return context

# Definición de una clase basada en DetailView para mostrar detalles de una tarea específica
class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'  # Nombre del objeto en el contexto de la plantilla
    template_name = 'base/tarea.html'  # Plantilla para la página de detalles de la tarea

# Definición de una clase basada en CreateView para la creación de una nueva tarea
class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']  # Campos permitidos en el formulario
    success_url = reverse_lazy('tareas')  # Redirección después de la creación exitosa

    # Método que se ejecuta cuando el formulario es válido
    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Asigna el usuario actual a la tarea
        return super(CrearTarea, self).form_valid(form)

# Definición de una clase basada en UpdateView para la edición de una tarea existente
class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']  # Campos permitidos en el formulario
    success_url = reverse_lazy('tareas')  # Redirección después de la edición exitosa

# Definición de una clase basada en DeleteView para eliminar una tarea existente
class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tareas'  # Nombre del objeto en el contexto de la plantilla
    success_url = reverse_lazy('tareas')  # Redirección después de la eliminación exitosa
