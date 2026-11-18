# Issue #1 — Agregar categorías y filtrado de tareas

**En GitHub:** <https://github.com/Isallethz/laboratorio-agente-cloud/issues/1>
**Estado:** cerrado (resuelto en el Pull Request #2)
**Etiquetas:** `enhancement`, `delegable`

## Objetivo

Agregar una categoría a cada tarea y permitir filtrar las tareas pendientes por categoría.

## Alcance

- `tasks.py`
- `app.py`
- `tests/test_tasks.py`

## Restricciones

- No agregar dependencias externas.
- No eliminar funciones existentes.
- Mantener compatibilidad con las pruebas actuales.

## Criterios de aceptación

- `agregar_tarea` debe recibir una categoría no vacía.
- `pendientes` debe aceptar opcionalmente una categoría.
- El filtrado no debe distinguir mayúsculas/minúsculas.
- Deben existir pruebas para categoría válida, categoría vacía y filtrado.

## Validación

Ejecutar:

```bash
python -m unittest discover -s tests
```

---

## Revisión del issue antes de delegar (paso 9)

**Pregunta:** ¿otro desarrollador podría implementar esta tarea sin preguntarme qué significa
"terminado"?

**Respuesta:** sí, con una precisión añadida. El criterio "mantener compatibilidad con las pruebas
actuales" convive con "agregar_tarea debe recibir una categoría no vacía"; las pruebas actuales
invocan `agregar_tarea(tareas, "Leer documentación")` con dos argumentos. La única forma de cumplir
ambos criterios sin tocar las pruebas existentes es que el parámetro `categoria` tenga un valor por
defecto. Se deja explícito en el PR para que la decisión quede registrada y sea revisable:

> Si `categoria` se omite, se usa `"General"`. Si se envía, debe ser una cadena no vacía después de
> aplicar `strip()`; en caso contrario se lanza `ValueError`.

Con esa aclaración el issue es delegable: un tercero sabe exactamente qué significa "terminado".
