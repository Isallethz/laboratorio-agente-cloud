# Trazabilidad del laboratorio (pasos 1 a 24)

| Paso | Actividad | Dónde queda registrado |
|------|-----------|-------------------------|
| 1 | Cuenta de GitHub y acceso a agente cloud | `docs/sesion-agente-cloud.md` (agente no habilitado: 403) |
| 2 | Crear repositorio con README | `README.md`, commit `42f9482` |
| 3 | Crear `tasks.py` | `tasks.py`, commit `42f9482` |
| 4 | Crear `app.py` | `app.py`, commit `42f9482` |
| 5 | Crear `tests/test_tasks.py` | `tests/test_tasks.py`, commit `42f9482` |
| 6 | Comprobar línea base | `evidencias/01_app_linea_base.txt`, `evidencias/02_pruebas_linea_base.txt` (2 pruebas OK) |
| 7 | Crear issue «Agregar categorías y filtrado de tareas» | `docs/issue-01-categorias.md` |
| 8 | Cuerpo del issue con objetivo, alcance, restricciones, criterios y validación | `docs/issue-01-categorias.md` |
| 9 | Revisar el issue antes de delegarlo | Sección final de `docs/issue-01-categorias.md` |
| 10 | Delegar el issue al agente cloud | `docs/sesion-agente-cloud.md` (captura pendiente) |
| 11 | Observar el trabajo remoto sin tocar archivos | `docs/sesion-agente-cloud.md` |
| 12 | Esperar rama o Pull Request | Rama `copilot/agregar-categorias`, `docs/pr-01-descripcion.md` |
| 13 | Leer la explicación del agente | `docs/pr-01-descripcion.md` |
| 14 | Revisar el PR archivo por archivo | `docs/revision-pr-01.md` (paso 14), `evidencias/04_diff_pr1_iteracion1.txt` |
| 15 | Revisar checks y pruebas | `evidencias/03_pruebas_iteracion1.txt` (Actions bloqueado por facturación) |
| 16 | Buscar un caso no cubierto | `docs/revision-pr-01.md` (paso 16) |
| 17 | Solicitar una iteración por comentario | `docs/revision-pr-01.md` (paso 17) |
| 18 | Comprobar la actualización del mismo PR | Commit `977653c`, `evidencias/05_diff_iteracion2.txt` |
| 19 | Validar localmente el resultado final | `evidencias/08_app_final.txt`, `evidencias/09_pruebas_finales.txt` |
| 20 | Decidir aprobar, pedir cambios o rechazar | `docs/revision-pr-01.md` (paso 20) |
| 21 | Hacer merge si la revisión es satisfactoria | PR #2 (merge `ff99df4`), PR #4 (merge `c984072`) |
| 22 | Revisar la trazabilidad del trabajo | `evidencias/14_historial_git.txt`, este documento |
| 23 | Reto final con una segunda tarea | `docs/issue-02-eliminar-tarea.md`, `docs/revision-pr-02.md` |
| 24 | Preparar la entrega | `DSaIA-Lab12-Entrega.docx` |

## Trazabilidad: agente cloud vs. chat web

| Elemento auditable | Agente cloud (este repositorio) | Chat web tradicional |
|--------------------|--------------------------------|----------------------|
| Enunciado del trabajo | Issue versionado y enlazado al PR | Prompt en una conversación privada |
| Cambios | Diff en una rama, revisable línea por línea | Texto pegado en el chat, sin diff |
| Pruebas | Logs de ejecución y checks del PR | Afirmaciones del modelo |
| Discusión | Comentarios de revisión sobre el código | Conversación sin contexto del repositorio |
| Decisión | Aprobación humana y merge registrado | Copiar y pegar sin registro |
| Reversión | `git revert` sobre un commit identificable | Rehacer manualmente |

## Entregables del laboratorio

| # | Entregable | Estado | Archivo |
|---|------------|--------|---------|
| 1 | URL o captura del repositorio | Listo | <https://github.com/Isallethz/laboratorio-agente-cloud> |
| 2 | Issue original completo | Listo | issue #1 y `docs/issue-01-categorias.md` |
| 3 | Evidencia de la sesión o asignación | Agente no habilitado (403); se documenta el intento | `docs/sesion-agente-cloud.md` |
| 4 | Pull Request generado | Listo | PR #2 y PR #4 |
| 5 | Captura o fragmento del diff revisado | Listo | `evidencias/04_diff_pr1_iteracion1.txt` |
| 6 | Evidencia de pruebas o checks | Listo (ejecución local, Actions bloqueado) | `evidencias/03_*`, `evidencias/06_*`, `evidencias/09_*` |
| 7 | Comentario de corrección y segunda iteración | Listo | comentarios en PR #2 y PR #4, `docs/revision-pr-01.md` |
| 8 | Validación local final | Listo | `evidencias/08_app_final.txt`, `evidencias/09_pruebas_finales.txt` |
| 9 | Segundo issue del reto final | Listo | issue #3 y `docs/issue-02-eliminar-tarea.md` |
| 10 | Reflexiones | Listo | `DSaIA-Lab12-Entrega.docx` |
