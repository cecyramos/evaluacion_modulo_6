# Gestor de Tareas - Django

Aplicación web para gestionar tareas personales. Los usuarios pueden registrarse, iniciar sesión, crear, ver y eliminar tareas.

## Características

- ✅ Autenticación de usuarios (registro, login, logout)
- ✅ Crear, ver y eliminar tareas
- ✅ Tareas almacenadas en memoria (no persisten al reiniciar)
- ✅ Interfaz responsiva con Bootstrap 5
- ✅ Protección de vistas con login_required

## Requisitos Previos

- Python 3.8+
- Django 5.2+
- pip

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/cecyramos/evaluacion_modulo_6.git
cd evaluacion_modulo_6
```

### 2. Crear entorno virtual

**Windows:**
```bash
python -m venv myenv
myenv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario (opcional)
```bash
python manage.py createsuperuser
```

### 6. Ejecutar servidor
```bash
python manage.py runserver
```

Accede a `http://127.0.0.1:8000/`

---

## Uso

1. **Registrarse:** Accede a `/registro/` y crea una cuenta
2. **Iniciar Sesión:** Ingresa con tus credenciales
3. **Crear Tareas:** Haz clic en "Agregar Nueva Tarea"
4. **Ver Detalles:** Haz clic en "Ver Detalles" de una tarea
5. **Eliminar:** Haz clic en "Eliminar" y confirma
6. **Cerrar Sesión:** Haz clic en "Cerrar Sesión"

---

## Estructura del Proyecto
```txt
M6_evaluacion_modulo/
├── gestor_tareas/          # Configuración principal del proyecto
│   ├── settings.py         # Configuración de Django
│   ├── urls.py             # URLs principales
│   └── wsgi.py
│
├── tareas/                 # Aplicación principal
│   ├── migrations/         # Migraciones de BD
│   ├── forms.py            # Formularios personalizados
│   ├── models.py           # Modelos (vacío, no usamos BD)
│   ├── utils.py            # Clase GestorTareas (almacenamiento en memoria)
│   ├── views.py            # Vistas y lógica
│   ├── urls.py             # URLs de tareas
│   └── tests.py            # Pruebas (opcional)
│
├── templates/              # Plantillas HTML
│   ├── base.html           # Plantilla base
│   ├── login.html
│   ├── logout.html
│   ├── registro.html
│   ├── lista_tareas.html
│   ├── agregar_tarea.html
│   ├── detalle_tarea.html
│   └── eliminar_tarea.html
│
├── manage.py               # Gestor de Django
├── requirements.txt        # Dependencias del proyecto
└── README.md              # Este archivo
```
---

## Funcionalidades Principales

### Autenticación
- Registro de nuevos usuarios con validación de contraseña
- Login seguro con contraseña encriptada
- Logout con limpeza de sesión
- Protección de vistas con `@login_required`

### Gestión de Tareas
- Crear tareas con título y descripción
- Listar tareas del usuario autenticado
- Ver detalles completos de una tarea
- Eliminar tareas con confirmación
- Tareas almacenadas en memoria (clase `GestorTareas`)

### Interfaz
- Diseño responsivo con Bootstrap 5
- Navbar con navegación condicional
- Mensajes de éxito/error
- Footer fijo al pie de página

---

## Notas Técnicas

- **Tareas en Memoria:** Las tareas se almacenan en la clase `GestorTareas` (en `utils.py`) y NO persisten cuando se reinicia el servidor
- **Usuario por Defecto:** Usa el modelo `User` de Django sin personalizaciones
- **Sin Base de Datos:** Solo usa SQLite para la autenticación de usuarios
- **DEBUG:** Actualmente en `True` para desarrollo. Cambiar a `False` en producción

---

## Autor

Cecilia Ramos - 2025

---

## Licencia

Este proyecto es de código abierto bajo la licencia MIT.
