# Pull Request #2 — Agregar función para eliminar una tarea por ID

**Rama del agente:** `copilot/eliminar-tarea` → `main`
**Issue:** #3 (reto final, redactado por el estudiante)
**Pull Request:** #4 (<https://github.com/Isallethz/laboratorio-agente-cloud/pull/4>)
**Estado:** revisado → iteración solicitada → aprobado → merged (`c984072`)

## Descripción enviada por el agente (primera versión)

Resumen: agregué `eliminar_tarea(tareas, tarea_id)` en `tasks.py`, que recorre la lista, elimina la
tarea con el `id` indicado mediante `pop()` y la devuelve; si no la encuentra lanza
`ValueError("Tarea no encontrada")`. Agregué tres pruebas: eliminación exitosa, `id` inexistente y
conservación del resto de las tareas. No modifiqué `app.py` ni agregué dependencias.

Archivos: `tasks.py`, `tests/test_tasks.py`.
Pruebas: `python -m unittest discover -s tests -v` → **11 pruebas, OK**.

## Revisión humana

### Explicación vs. diff

| Afirmación | Verificación | Resultado |
|------------|--------------|-----------|
| Solo dos archivos | `git diff main --stat` | Confirmado |
| No tocó `app.py` | Sin cambios en `app.py` | Confirmado |
| No agregó dependencias | Sin `import` nuevos | Confirmado |
| 11 pruebas OK | `evidencias/10_pruebas_pr2_iteracion1.txt` | Confirmado |
| `pop()` modifica en el lugar | El código usa `tareas.pop(indice)` | Confirmado |

### Revisión archivo por archivo

- `tasks.py`: función corta, coherente con `completar_tarea` (mismo mensaje de error).
- `tests/test_tasks.py`: las 8 pruebas anteriores se conservan; se agregan 3.
- Sin renombres, sin archivos no relacionados, sin cambios de estilo.

### Caso no cubierto encontrado (paso 16)

Se escribió un caso deliberado: eliminar una tarea y luego agregar otra.

```text
IDs despues de eliminar la tarea 1: [2, 2]
ID asignado a la tarea nueva: 2
AssertionError: IDs duplicados: [2, 2]
```

**Hallazgo real:** `agregar_tarea` calcula `id = len(tareas) + 1`. Al eliminar una tarea, el
siguiente `id` se reutiliza y quedan dos tareas con el mismo `id`. A partir de ese momento
`completar_tarea` y `eliminar_tarea` actúan sobre la primera coincidencia, lo que produce resultados
incorrectos. El issue #2 no lo cubría porque el cálculo del `id` está en `agregar_tarea`, fuera del
alcance declarado; se amplía el alcance de forma explícita en la revisión.

Script de reproducción: `evidencias/11_repro_id_duplicado.py`
Salida: `evidencias/11_repro_id_duplicado.txt`

### Comentario de revisión enviado (paso 17)

> El PR cumple los criterios del issue, pero encontré un problema de integridad de datos.
> Al eliminar la última tarea y agregar una nueva, `agregar_tarea` reutiliza un `id` existente
> porque usa `len(tareas) + 1` (ver `evidencias/11_repro_id_duplicado.txt`).
> Antes de integrar, cambia el cálculo para usar el siguiente `id` libre (`max(id) + 1`) y agrega una
> prueba de regresión que elimine una tarea, agregue otra y verifique que no hay `id` duplicados.
> Mantén la compatibilidad: con inserciones consecutivas los `id` deben seguir siendo 1, 2, 3...
> No cambies la API pública ni agregues dependencias. Actualiza el mismo Pull Request.

### Segunda iteración verificada (paso 18)

- Nuevo commit `19d245d` en la misma rama.
- Se agregó el auxiliar `_siguiente_id()` y se reemplazó `len(tareas) + 1` por `max(id) + 1`.
- Se agregó `test_id_no_se_reutiliza_despues_de_eliminar`.
- El diff incremental no toca `app.py`, no cambia firmas públicas y no agrega dependencias.
- El script de reproducción ahora imprime `[2, 3]` sin duplicados
  (`evidencias/12_repro_id_corregido.txt`).
- Resultado: **12 pruebas, OK**.

### Decisión (pasos 20 y 21)

**Aprobado y mergeado.** El cambio solicitado resuelve un defecto real, está cubierto por una prueba
de regresión y conserva la compatibilidad (las pruebas originales siguen pasando sin modificarse).
El alcance ampliado quedó justificado y registrado en el comentario de revisión, no fue un cambio
silencioso del agente.
