from tasks import agregar_tarea, completar_tarea, pendientes

tareas = []
agregar_tarea(tareas, "Estudiar agentes cloud", "Estudio")
agregar_tarea(tareas, "Preparar laboratorio", "Universidad")
completar_tarea(tareas, 1)

for tarea in pendientes(tareas):
    print(f'- {tarea["id"]}: {tarea["titulo"]} [{tarea["categoria"]}]')

print("\nPendientes de la categoría 'estudio':")
for tarea in pendientes(tareas, "estudio"):
    print(f'- {tarea["id"]}: {tarea["titulo"]} [{tarea["categoria"]}]')
