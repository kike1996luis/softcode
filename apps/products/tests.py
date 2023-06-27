from django.test import TestCase
from apps.products.models import Producto

class TestProductCase(TestCase):

    def setUp(self):
        Producto.objects.create(nombre="Producto 1", descripcion="Esta es una descripcion",precio="123.45",activo=True)
        Producto.objects.create(nombre="Producto 2", descripcion="Esta es otra descripcion",precio="453.21",activo=False)

    # Prueba unitaria para verificar si los datos fueron agregados correctamente
    def products_ut(self):
        product = Producto.objects.get(nombre="Producto 1")
        self.assertEqual(product.nombre, "Producto 1", "Verifica si el producto 1 fue registrado")
        product = Producto.objects.get(nombre="Producto 2")
        self.assertEqual(product.nombre, "Producto 2", "Verifica si el producto 2 fue registrado")
        self.assertEqual(Producto.objects.all().count(), 2, "Verifica si hay elementos en la base de datos")
