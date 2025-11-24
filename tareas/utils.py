from datetime import datetime

class GestorTareas:
    """Gestor de tareas en memoria por usuario"""
    _tareas = {}  # Estructura: {usuario_id: [tarea1, tarea2, ...]}
    _contador = {}  # Estructura: {usuario_id: siguiente_id}
    
    @classmethod
    def obtener_tareas(cls, usuario_id):
        """Obtiene todas las tareas de un usuario"""
        return cls._tareas.get(usuario_id, [])
    
    @classmethod
    def obtener_tarea_por_id(cls, usuario_id, tarea_id):
        """Obtiene una tarea específica por ID"""
        tareas = cls._tareas.get(usuario_id, [])
        for tarea in tareas:
            if tarea['id'] == tarea_id:
                return tarea
        return None
    
    @classmethod
    def crear_tarea(cls, usuario_id, titulo, descripcion):
        """Crea una nueva tarea para un usuario"""
        if usuario_id not in cls._tareas:
            cls._tareas[usuario_id] = []
            cls._contador[usuario_id] = 1
        
        tarea_id = cls._contador[usuario_id]
        cls._contador[usuario_id] += 1
        
        nueva_tarea = {
            'id': tarea_id,
            'titulo': titulo,
            'descripcion': descripcion,
            'fecha_creacion': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'completada': False
        }
        
        cls._tareas[usuario_id].append(nueva_tarea)
        return nueva_tarea
    
    @classmethod
    def eliminar_tarea(cls, usuario_id, tarea_id):
        """Elimina una tarea de un usuario"""
        if usuario_id in cls._tareas:
            cls._tareas[usuario_id] = [
                t for t in cls._tareas[usuario_id] 
                if t['id'] != tarea_id
            ]
            return True
        return False
    
    @classmethod
    def actualizar_tarea(cls, usuario_id, tarea_id, titulo, descripcion):
        """Actualiza una tarea existente"""
        tarea = cls.obtener_tarea_por_id(usuario_id, tarea_id)
        if tarea:
            tarea['titulo'] = titulo
            tarea['descripcion'] = descripcion
            return tarea
        return None