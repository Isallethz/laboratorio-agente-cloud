# laboratorio-agente-cloud

Repositorio de práctica del **Laboratorio 12 – Agente cloud** de Tópicos Especiales II.

El objetivo del laboratorio no es solo el código final, sino demostrar el ciclo completo de
delegación asíncrona a un agente que trabaja en un entorno remoto:

```
issue bien delimitado  ->  agente cloud (rama/PR)  ->  revisión humana  ->  validación local  ->  merge
```

## Estructura del proyecto

```
laboratorio_agente_cloud/
├── app.py                  # Demo ejecutable
├── tasks.py                # Lógica de tareas
├── tests/
│   └── test_tasks.py       # Pruebas unitarias (unittest)
├── docs/
│   ├── issue-01-categorias.md
│   ├── issue-02-eliminar-tarea.md
│   ├── pr-01-descripcion.md
│   ├── revision-pr-01.md
│   ├── sesion-agente-cloud.md
│   └── trazabilidad.md
├── evidencias/             # Salidas reales de comandos y diffs revisados
└── README.md
```

Repositorio en GitHub: <https://github.com/Isallethz/laboratorio-agente-cloud>

- Issue #1: <https://github.com/Isallethz/laboratorio-agente-cloud/issues/1>
- Pull Request #2: <https://github.com/Isallethz/laboratorio-agente-cloud/pull/2>
- Issue #3: <https://github.com/Isallethz/laboratorio-agente-cloud/issues/3>
- Pull Request #4: <https://github.com/Isallethz/laboratorio-agente-cloud/pull/4>

## Cómo ejecutar

Requiere Python 3 (sin dependencias externas).

```bash
python app.py
python -m unittest discover -s tests
```

## Historial de trabajo

| Rama | Contenido |
|------|-----------|
| `main` | Línea base + contribuciones revisadas y aprobadas |
| `copilot/agregar-categorias` | Contribución del issue #1 |
| `copilot/eliminar-tarea` | Contribución del issue #3 (reto final) |

Cada contribución se revisó archivo por archivo antes de integrarse. Las observaciones y la
segunda iteración solicitada al agente están documentadas en `docs/revision-pr-01.md`.
