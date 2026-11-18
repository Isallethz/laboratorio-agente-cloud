import unittest
from tasks import agregar_tarea, completar_tarea, eliminar_tarea, pendientes


class TestTasks(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertFalse(tarea["completada"])

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])

    def test_agregar_tarea_con_categoria(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación", "Estudio")
        self.assertEqual(tarea["categoria"], "Estudio")

    def test_agregar_tarea_categoria_vacia(self):
        tareas = []
        with self.assertRaises(ValueError):
            agregar_tarea(tareas, "Practicar", "")

    def test_agregar_tarea_categoria_con_espacios(self):
        tareas = []
        with self.assertRaises(ValueError):
            agregar_tarea(tareas, "Practicar", "   ")

    def test_filtrar_pendientes_por_categoria(self):
        tareas = []
        agregar_tarea(tareas, "Estudiar agentes cloud", "Estudio")
        agregar_tarea(tareas, "Comprar café", "Personal")
        agregar_tarea(tareas, "Repasar filtrado", "estudio")
        completar_tarea(tareas, 3)

        resultado = pendientes(tareas, "ESTUDIO")

        self.assertEqual([t["titulo"] for t in resultado], ["Estudiar agentes cloud"])

    def test_pendientes_sin_categoria_devuelve_todas(self):
        tareas = []
        agregar_tarea(tareas, "Estudiar agentes cloud", "Estudio")
        agregar_tarea(tareas, "Comprar café", "Personal")
        completar_tarea(tareas, 2)

        self.assertEqual(len(pendientes(tareas)), 1)

    def test_filtrar_categoria_inexistente_devuelve_lista_vacia(self):
        tareas = []
        agregar_tarea(tareas, "Estudiar agentes cloud", "Estudio")

        self.assertEqual(pendientes(tareas, "NoExiste"), [])

    def test_eliminar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Estudiar agentes cloud", "Estudio")
        agregar_tarea(tareas, "Comprar café", "Personal")

        eliminada = eliminar_tarea(tareas, 1)

        self.assertEqual(eliminada["titulo"], "Estudiar agentes cloud")
        self.assertEqual([t["id"] for t in tareas], [2])

    def test_eliminar_tarea_inexistente(self):
        tareas = []
        agregar_tarea(tareas, "Estudiar agentes cloud", "Estudio")

        with self.assertRaises(ValueError):
            eliminar_tarea(tareas, 99)

    def test_eliminar_tarea_conserva_las_demas(self):
        tareas = []
        agregar_tarea(tareas, "Estudiar agentes cloud", "Estudio")
        agregar_tarea(tareas, "Comprar café", "Personal")
        agregar_tarea(tareas, "Preparar laboratorio", "Universidad")

        eliminar_tarea(tareas, 2)

        self.assertEqual(
            [t["titulo"] for t in tareas],
            ["Estudiar agentes cloud", "Preparar laboratorio"],
        )


if __name__ == "__main__":
    unittest.main()
