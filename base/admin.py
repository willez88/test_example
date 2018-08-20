from django.contrib import admin
from .models import Country, State, City, Location, AcademicLevel

# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    """!
    Clase que agrega país al panel administrativo

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 19-08-2018
    """

    ## Mostrar los campos de la clase
    list_display = ('name',)

    ## Seleccionar campo para ordenar
    ordering = ('name',)

admin.site.register(Country, CountryAdmin)

class StateAdmin(admin.ModelAdmin):
    """!
    Clase que agrega estado al panel administrativo

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 19-08-2018
    """

    ## Mostrar los campos de la clase
    list_display = ('name','country')

    ## Seleccionar campo para ordenar
    ordering = ('name',)

admin.site.register(State, StateAdmin)

class CityAdmin(admin.ModelAdmin):
    """!
    Clase que agrega país al panel administrativo

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 19-08-2018
    """

    ## Mostrar los campos de la clase
    list_display = ('name','state')

    ## Seleccionar campo para ordenar
    ordering = ('name','state')

admin.site.register(City, CityAdmin)

class LocationAdmin(admin.ModelAdmin):
    """!
    Clase que agrega la ubicación al panel administrativo

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 19-08-2018
    """

    ## Mostrar los campos de la clase
    list_display = ('address','city')

    ## Seleccionar campo para ordenar
    ordering = ('address',)

admin.site.register(Location, LocationAdmin)

class AcademicLevelAdmin(admin.ModelAdmin):
    """!
    Clase que agrega país al panel administrativo

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 19-08-2018
    """

    ## Mostrar los campos de la clase
    list_display = ('name',)

    ## Seleccionar campo para ordenar
    ordering = ('name',)

admin.site.register(AcademicLevel, AcademicLevelAdmin)