from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class RecetasView(TemplateView):
    template_name = "recetas.html"

class CosteoView(TemplateView):
    template_name = "costeo.html"

class ContactoView(TemplateView):
    template_name = "contacto.html"
