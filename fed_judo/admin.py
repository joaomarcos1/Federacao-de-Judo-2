from django.contrib import admin
from .models import Usuario, Evento, FaleConosco, Academia, Noticia, TipoUsuario
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Evento)
admin.site.register(FaleConosco)
admin.site.register(Academia)
admin.site.register(Noticia)
admin.site.register(TipoUsuario)
