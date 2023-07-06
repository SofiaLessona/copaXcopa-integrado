from recetasManager import RecetasManager
from receta import Receta

russianSpringPunch = Receta(
    nombre = "Russian Spring Punch",
    url = "https://www.youtube.com/watch?v=I-Xd6Nlq2J0&ab_channel=QUIEROFLAIRAnthonySerra",
    descripcion = "BlaBlaBla",
    ingredientes = "Hielo, 1⅓ Partes de Absolut Vodka, ⅓ Parte de Licor De Grosella Negra, 1 Parte de Zumo De Limón, ⅔ Parte de Almíbar, Champán",
    preparacion = "Llenar una coctelera boston con hielo. Añadir Absolut Vodka, licor de grosella negra, zumo de limón y almíbar. Agitar y colar en una copa de vino refrigerada lleno con hielo picado. Rellénalo con champán."
)

recetas_manager = RecetasManager(
    path = "/nose/path/etc",
    trago = "vodka"
)

recetas_manager.create_receta(russianSpringPunch)
print(recetas_manager.db_recetas)