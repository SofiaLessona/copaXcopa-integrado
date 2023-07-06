from receta import Receta

class RecetasManager:
    db_recetas = []

    def __init__(self, **kwargs):
        self.path:str = kwargs['path']
        self.trago:str = kwargs['trago']

    def create_receta(self, receta:Receta):
        self.db_recetas.append(receta)
        print(f"La receta de {receta.nombre} ha sido agregada")

    def read_receta(self):
        for receta in self.db_recetas:
            print(receta)

    # def update_receta(self):


    # def delete_receta(self):
