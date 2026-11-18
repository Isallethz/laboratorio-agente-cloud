# Revisión humana del Pull Request #1

## Paso 13 — Leer primero la explicación del agente

Afirmaciones del PR que deben comprobarse contra el diff:

| Afirmación del agente | Verificación | Resultado |
|-----------------------|--------------|-----------|
| No agregó dependencias | `git diff` no toca ningún archivo de dependencias y no hay `import` nuevos | Confirmado |
| No eliminó funciones | `agregar_tarea`, `completar_tarea` y `pendientes` siguen existiendo | Confirmado |
| Mantiene compatibilidad | Las 2 pruebas originales siguen pasando sin cambios | Confirmado |
| 7 pruebas en verde | Ejecución local registrada en `evidencias/03_pruebas_iteracion1.txt` | Confirmado |
| Modificó solo 3 archivos | `git diff main --stat` muestra `app.py`, `tasks.py`, `tests/test_tasks.py` | Confirmado |

## Paso 14 — Revisión archivo por archivo

- **`tasks.py`**: el cambio funcional es claro; `_normalizar_categoria` evita duplicar validación.
  No hay renombres innecesarios ni cambios de estilo ajenos.
- **`app.py`**: el cambio se limita a mostrar la categoría y a un ejemplo de filtrado. Está dentro
  del alcance del issue.
- **`tests/test_tasks.py`**: se conservan las 2 pruebas originales y se agregan 5. No se borró
  cobertura previa.
- Sin archivos no relacionados, sin dependencias nuevas, sin reformateos masivos.

## Paso 15 — Checks y resultados de pruebas

- GitHub Actions no está disponible en la cuenta (el job no inicia por un bloqueo de facturación),
  así que la validación se ejecuta localmente y se registra en `evidencias/`.
- Evidencia local: 7 pruebas OK antes de la revisión.
- Nota de revisión: una prueba en verde demuestra que esos casos pasaron, no que el cambio sea
  correcto en todos los escenarios. Por eso se hizo el paso 16.

## Paso 16 — Caso no cubierto encontrado

Se probaron manualmente dos escenarios que el issue no especifica y que el PR no cubre con pruebas:

1. **Filtrar por una categoría inexistente.** El código devuelve `[]`, que es el comportamiento
   esperado, pero no existe una prueba que lo garantice frente a una regresión futura.
2. **Filtrar con una categoría vacía (`"   "`).** `pendientes` lanza `ValueError` por la validación
   centralizada. Es coherente con `agregar_tarea`, pero tampoco está probado ni especificado.

El escenario 1 es el más importante: es una consulta legítima del usuario y su resultado vacío no
debe confundirse con un error.

## Paso 17 — Solicitud de iteración enviada al agente

Comentario publicado en el PR:

> Antes de integrar este PR, agrega una prueba que compruebe que filtrar por una categoría
> inexistente devuelve una lista vacía. No cambies la API pública ni agregues dependencias.
> Actualiza el mismo Pull Request.

## Paso 18 — Verificación de la segunda iteración

- Nuevo commit en la misma rama `copilot/agregar-categorias` (no se abrió un PR nuevo).
- El diff incremental solo agrega `test_filtrar_categoria_inexistente_devuelve_lista_vacia` en
  `tests/test_tasks.py`.
- No se modificó la API pública, no se agregaron dependencias y no aparecieron cambios ajenos.
- Resultado: **8 pruebas, OK**.

## Paso 19 — Validación local independiente

```bash
python app.py
python -m unittest discover -s tests
```

Evidencia: `evidencias/08_app_final.txt` y `evidencias/09_pruebas_finales.txt`.
La ejecución local es la segunda fuente de evidencia, independiente de lo que reportó el agente.

## Paso 20 — Decisión

**Aprobado.** Criterios aplicados:

| Criterio | Evaluación |
|----------|------------|
| Corrección funcional | Cumple los 4 criterios de aceptación |
| Alcance | Solo los 3 archivos del issue |
| Claridad | Nombres y validación explícitos; sin código muerto |
| Pruebas | 8 pruebas; incluye caso vacío, filtrado y categoría inexistente |
| Seguridad | Sin dependencias nuevas ni entradas ejecutables; validación de entrada presente |
| Mantenibilidad | Validación centralizada en una función auxiliar privada |

Riesgo aceptado y documentado: los IDs se siguen calculando con `len(tareas) + 1`, fuera del
alcance de este issue. Se atenderá en el issue #2 (`eliminar_tarea`), donde el riesgo de reutilización
de IDs se vuelve relevante.

## Paso 21 — Integración

El Pull Request #2 (<https://github.com/Isallethz/laboratorio-agente-cloud/pull/2>) se integró con
merge commit `ff99df4`, conservando el historial de la contribución y el registro de la revisión. La
rama `copilot/agregar-categorias` se conserva como referencia.
