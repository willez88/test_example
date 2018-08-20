from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    """!
    Clase que agrega perfil al panel administrativo

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 19-08-2018
    """

    ## Mostrar los campos de la clase
    list_display = ('academic_level','location')

    ## Seleccionar campo para ordenar
    ordering = ('academic_level',)

admin.site.register(Profile, ProfileAdmin)