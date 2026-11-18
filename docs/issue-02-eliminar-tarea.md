# Issue #2 — Agregar función para eliminar una tarea por ID

**En GitHub:** <https://github.com/Isallethz/laboratorio-agente-cloud/issues/3>
**Estado:** cerrado (resuelto en el Pull Request #4)
**Etiquetas:** `enhancement`, `delegable`, `reto-final`

## Objetivo

Permitir eliminar una tarea de la lista a partir de su `id`, informando un error claro cuando el
`id` no existe.

## Alcance

- `tasks.py`
- `tests/test_tasks.py`

## Restricciones

- No agregar dependencias externas.
- No modificar `app.py` en este issue.
- No cambiar la firma de `eliminar_tarea` una vez acordada: `eliminar_tarea(tareas, tarea_id)`.
- Mantener el estilo de manejo de errores del proyecto (`ValueError`).

## Criterios de aceptación

- `eliminar_tarea(tareas, tarea_id)` elimina la tarea cuyo `id` coincide y la devuelve.
- Si el `id` no existe, lanza `ValueError("Tarea no encontrada")`.
- El resto de las tareas conserva su contenido y su orden.
- Deben existir pruebas para: eliminación exitosa, `id` inexistente y conservación de las demás
  tareas.
- La lista original se modifica en el lugar (no se devuelve una lista nueva).

## Validación

Ejecutar:

```bash
python -m unittest discover -s tests
```

---

## Revisión del issue antes de delegar

**Pregunta:** ¿otro desarrollador podría implementar esta tarea sin preguntarme qué significa
"terminado"?

**Respuesta:** sí. El contrato es explícito: misma convención de errores que `completar_tarea`,
devolución de la tarea eliminada, modificación en el lugar y alcance limitado a `tasks.py` y sus
pruebas. El único punto que queda abierto a propósito es qué ocurre con los `id` después de una
eliminación; se deja para la revisión del PR porque afecta a `agregar_tarea`, que está fuera del
alcance declarado.
