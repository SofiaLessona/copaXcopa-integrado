from django.db import models

# Create your models here.

class Receta(models.Model):
    class Meta:
        db_table = "Recetas"

    nombre        = models.CharField(max_length=200)
    url_video     = models.CharField(max_length=200)
    ingredientes  = models.CharField(max_length=800)
    preparacion   = models.CharField(max_length=1000)

    def __str__(self):
        return f"Receta de {self.nombre}"

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]