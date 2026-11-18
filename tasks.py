CATEGORIA_POR_DEFECTO = "General"


def _normalizar_categoria(categoria):
    """Valida y normaliza una categoría: no se aceptan valores vacíos."""
    if categoria is None:
        raise ValueError("La categoría es obligatoria")
    categoria = str(categoria).strip()
    if not categoria:
        raise ValueError("La categoría es obligatoria")
    return categoria


def _siguiente_id(tareas):
    """Devuelve el siguiente id libre, sin reutilizar ids de tareas eliminadas."""
    return max((t["id"] for t in tareas), default=0) + 1


def agregar_tarea(tareas, titulo, categoria=CATEGORIA_POR_DEFECTO):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("El título es obligatorio")
    categoria = _normalizar_categoria(categoria)
    tarea = {
        "id": _siguiente_id(tareas),
        "titulo": titulo,
        "categoria": categoria,
        "completada": False,
    }
    tareas.append(tarea)
    return tarea


def completar_tarea(tareas, tarea_id):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea["completada"] = True
            return tarea
    raise ValueError("Tarea no encontrada")


def eliminar_tarea(tareas, tarea_id):
    for indice, tarea in enumerate(tareas):
        if tarea["id"] == tarea_id:
            return tareas.pop(indice)
    raise ValueError("Tarea no encontrada")


def pendientes(tareas, categoria=None):
    tareas_pendientes = [t for t in tareas if not t["completada"]]
    if categoria is None:
        return tareas_pendientes
    categoria = _normalizar_categoria(categoria)
    return [
        t
        for t in tareas_pendientes
        if t["categoria"].casefold() == categoria.casefold()
    ]
