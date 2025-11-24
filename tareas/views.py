from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FormularioTarea, RegistroForm
from .utils import GestorTareas


# ==================== AUTENTICACIÓN ====================

def registro_view(request):
    """Vista de registro de usuarios"""
    if request.user.is_authenticated:
        return redirect('lista_tareas')
    
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'¡Bienvenid@ {user.username}!')
            return redirect('lista_tareas')
        else:
            for errors in form.errors.values():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = RegistroForm()
    
    return render(request, 'registro.html', {'form': form})


def login_view(request):
    """Vista de inicio de sesión"""
    if request.user.is_authenticated:
        return redirect('lista_tareas')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Hola {user.username}!')
            return redirect('lista_tareas')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'login.html')


def logout_view(request):
    """Vista de cierre de sesión"""
    logout(request)
    messages.success(request, 'Sesión cerrada correctamente')
    return redirect('login')


# ==================== TAREAS ====================

@login_required(login_url='login')
def lista_tareas(request):
    """Muestra todas las tareas del usuario autenticado"""
    tareas = GestorTareas.obtener_tareas(request.user.id)
    return render(request, 'lista_tareas.html', {
        'tareas': tareas,
        'total_tareas': len(tareas)
    })


@login_required(login_url='login')
def agregar_tarea(request):
    """Permite agregar una nueva tarea"""
    if request.method == 'POST':
        form = FormularioTarea(request.POST)
        if form.is_valid():
            GestorTareas.crear_tarea(
                usuario_id=request.user.id,
                titulo=form.cleaned_data['titulo'],
                descripcion=form.cleaned_data['descripcion']
            )
            messages.success(request, 'Tarea creada exitosamente')
            return redirect('lista_tareas')
    else:
        form = FormularioTarea()
    
    return render(request, 'agregar_tarea.html', {'form': form})


@login_required(login_url='login')
def detalle_tarea(request, tid):
    """Muestra los detalles de una tarea específica"""
    tarea = GestorTareas.obtener_tarea_por_id(request.user.id, tid)
    
    if tarea is None:
        messages.error(request, 'Tarea no encontrada')
        return redirect('lista_tareas')
    
    return render(request, 'detalle_tarea.html', {'tarea': tarea})


@login_required(login_url='login')
def eliminar_tarea(request, tid):
    """Permite eliminar una tarea con confirmación"""
    tarea = GestorTareas.obtener_tarea_por_id(request.user.id, tid)
    
    if tarea is None:
        messages.error(request, 'Tarea no encontrada')
        return redirect('lista_tareas')
    
    if request.method == 'POST':
        GestorTareas.eliminar_tarea(request.user.id, tid)
        messages.success(request, 'Tarea eliminada exitosamente')
        return redirect('lista_tareas')
    
    return render(request, 'eliminar_tarea.html', {'tarea': tarea})