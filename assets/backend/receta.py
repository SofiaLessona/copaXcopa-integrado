class Receta:

    def __init__(self, **kwargs):
        self.nombre:str = kwargs['nombre']
        self.url:str = kwargs['url']
        self.descripcion:str = kwargs['descripcion']
        self.ingredientes:str = kwargs['ingredientes']
        self.preparacion:str = kwargs['preparacion']

    def __str__(self):
        return f"""
                {self.nombre}
                {self.url}
                Descripción:
                {self.descripcion}
                Ingredientes:
                {self.ingredientes}
                Preparación:
                {self.preparacion}
            """