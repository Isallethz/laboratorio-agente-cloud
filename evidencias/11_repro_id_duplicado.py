"""Reproducción del caso no cubierto detectado durante la revisión del PR #2.

Escenario: se elimina la última tarea de la lista y luego se agrega una nueva.
Con el cálculo `id = len(tareas) + 1` el id nuevo colisiona con uno existente.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tasks import agregar_tarea, eliminar_tarea

tareas = []
agregar_tarea(tareas, "Estudiar agentes cloud", "Estudio")
agregar_tarea(tareas, "Preparar laboratorio", "Universidad")

eliminar_tarea(tareas, 1)
nueva = agregar_tarea(tareas, "Comprar café", "Personal")

ids = [t["id"] for t in tareas]
print("IDs despues de eliminar la tarea 1:", ids)
print("ID asignado a la tarea nueva:", nueva["id"])

assert len(ids) == len(set(ids)), f"IDs duplicados: {ids}"
