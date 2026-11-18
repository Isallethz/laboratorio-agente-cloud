# Sesión del agente cloud — registro de evidencia

## Datos de la delegación

| Campo | Valor |
|-------|-------|
| Ruta intentada | GitHub Copilot cloud agent (`gh agent-task create`) |
| Alternativas | OpenAI Codex cloud, Google Jules (no configuradas) |
| Repositorio | <https://github.com/Isallethz/laboratorio-agente-cloud> |
| Issue original | #1 <https://github.com/Isallethz/laboratorio-agente-cloud/issues/1> |
| Issue del reto final | #3 <https://github.com/Isallethz/laboratorio-agente-cloud/issues/3> |
| Rama de la contribución #1 | `copilot/agregar-categorias` |
| Rama de la contribución #2 | `copilot/eliminar-tarea` |
| Pull Request #1 | #2 <https://github.com/Isallethz/laboratorio-agente-cloud/pull/2> |
| Pull Request #2 | #4 <https://github.com/Isallethz/laboratorio-agente-cloud/pull/4> |
| Fecha | 18 de noviembre de 2026 |

## Estado del entorno

- `gh agent-task create` respondió **403 Forbidden**: la cuenta no tiene el agente de Copilot
  habilitado, por lo que no fue posible iniciar una sesión remota real.
- GitHub Actions no inicia los jobs por un **bloqueo de facturación** de la cuenta, así que los
  checks automáticos no están disponibles. Por eso el workflow se retiró del repositorio y la
  validación se ejecuta localmente.
- Para no inventar evidencia de una sesión inexistente, el ciclo se completó así: la contribución se
  implementó y validó en local, se publicó en una rama real, se abrió un Pull Request real, se
  revisó con comentarios reales en GitHub, se solicitó una segunda iteración y se hizo merge.

## Qué puede hacer un agente cloud sin que yo ejecute nada

- Clonar el repositorio en un entorno remoto aislado y leer el código.
- Interpretar el issue y proponer un plan de cambios.
- Editar los archivos dentro del alcance y ejecutar la suite de pruebas en ese entorno.
- Crear commits en una rama propia y abrir o actualizar el Pull Request.
- Reportar qué archivos modificó y qué pruebas ejecutó.
- Atender un comentario de revisión y publicar una nueva iteración en el mismo PR.

Lo que **no** hace sin autorización humana: integrar a `main`, cambiar la configuración del
repositorio, ni decidir que el trabajo está terminado.

## Cronología del trabajo

| Momento | Acción | Evidencia |
|---------|--------|-----------|
| 1 | Crear el repositorio público e inicializarlo con README | <https://github.com/Isallethz/laboratorio-agente-cloud> |
| 2 | Subir la línea base (`tasks.py`, `app.py`, `tests/`) | commit `42f9482` |
| 3 | Verificar la línea base (2 pruebas OK) | `evidencias/02_pruebas_linea_base.txt` |
| 4 | Crear el issue #1 con objetivo, alcance, restricciones, criterios y validación | issue #1 |
| 5 | Publicar la contribución en la rama `copilot/agregar-categorias` | commits `e08b730`, `977653c` |
| 6 | Abrir el Pull Request #2 con la explicación del cambio | PR #2 |
| 7 | Revisar archivo por archivo y detectar el caso no cubierto | `docs/revision-pr-01.md` |
| 8 | Comentar la solicitud de iteración | comentario en PR #2 |
| 9 | Actualizar el mismo PR con la prueba solicitada (8 pruebas OK) | commit `977653c` |
| 10 | Validar localmente y hacer merge | merge `ff99df4` |
| 11 | Crear el issue #3 del reto final | issue #3 |
| 12 | Publicar la rama `copilot/eliminar-tarea` y abrir el Pull Request #4 | commits `ddc4402`, `19d245d` |
| 13 | Reproducir el defecto de ids duplicados y comentarlo | `evidencias/11_repro_id_duplicado.txt` |
| 14 | Verificar la corrección (12 pruebas OK) y hacer merge | merge `c984072` |

## Trazabilidad en GitHub

- Issues: <https://github.com/Isallethz/laboratorio-agente-cloud/issues?q=is%3Aissue>
- Pull Requests: <https://github.com/Isallethz/laboratorio-agente-cloud/pulls?q=is%3Apr>
- Historial de commits: <https://github.com/Isallethz/laboratorio-agente-cloud/commits/main>
- Resumen de los PRs: `evidencias/19_prs_github.txt`
- Detalle de cada PR e issue: `evidencias/15_pr2_github.txt`, `evidencias/16_pr4_github.txt`,
  `evidencias/17_issue1_github.txt`, `evidencias/18_issue3_github.txt`

## Nota para completar la entrega

Si se habilita Copilot coding agent o Codex/Jules en la cuenta, el mismo issue #1 puede asignarse
desde la interfaz y el agente abrirá su propia rama y PR. En ese caso conviene conservar estas
capturas y agregar las de la sesión remota. Todo el material de revisión de este repositorio sigue
siendo válido: los criterios, el diff esperado y las pruebas son los mismos.
