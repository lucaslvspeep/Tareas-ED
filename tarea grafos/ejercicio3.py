class CasaComercial:
    def __init__(self, nombre):
        self.nombre = nombre
        self.categorias = {}
        
    def agregar_categoria(self, categoria, productos):
        self.categorias[categoria] = productos
        
    def mostrar_casa(self):
        print(f"Casa Comercial: {self.nombre}")
        for categoria, productos in self.categorias.items():
            print(f"Categoría: {categoria}")
            for producto in productos:
                print(f"- {producto}")

supermercado = CasaComercial('Supermercado')
supermercado.agregar_categoria('Alimentos', ['Pan', 'Leche', 'Huevos'])
supermercado.agregar_categoria('Utiles', ['Libretas', 'Lapices', 'Borradores'])
supermercado.agregar_categoria('Limpieza', ['Jabón', 'Legía', 'Desinfectante'])
supermercado.mostrar_casa()