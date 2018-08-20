from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Country(models.Model):
    """!
    Clase que contiene los paises

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 03-08-2018
    """

    ## Nombre del pais
    name = models.CharField('nombre', max_length=80)

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author William Páez (paez.william8 at gmail.com)
        @date 03-08-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return string <b>{object}</b> Objeto con el nombre del país
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @date 19-08-2018
        """

        verbose_name = _('País')
        verbose_name_plural = _('Paises')

class State(models.Model):
    """!
    Clase que contiene los estados

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 03-08-2018
    """

    ## Nombre del Estado
    name = models.CharField('nombre', max_length=50)

    ## Pais en donde esta ubicado el Estado
    country = models.ForeignKey(Country,on_delete=models.CASCADE, verbose_name='país')

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author William Páez (paez.william8 at gmail.com)
        @date 03-08-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return string <b>{object}</b> Objeto con el nombre del estado
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @date 19-08-2018
        """

        verbose_name = _('Estado')
        verbose_name_plural = _('Estados')

class City(models.Model):
    """!
    Clase que contiene las ciudades

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 03-08-2018
    """

    ## Nombre de la Ciudad
    name = models.CharField('nombre', max_length=50)

    ## Estado en donde se encuentra ubicada la Ciudad
    state = models.ForeignKey(State,on_delete=models.CASCADE, verbose_name='estado')

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author William Páez (paez.william8 at gmail.com)
        @date 03-08-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return string <b>{object}</b> Objeto con el nombre de la ciudad
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @date 19-08-2018
        """

        verbose_name = _('Ciudad')
        verbose_name_plural = _('Ciudades')

class Location(models.Model):
    """!
    Clase que contiene los datos de una ubicación geográfica

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 03-08-2018
    """

    ## Establece la dirección exacta
    address = models.CharField('dirección', max_length=500)

    ## Establece la relación entre la parroquia y la ubicación
    city = models.ForeignKey(City,on_delete=models.CASCADE, verbose_name='ciudad')

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author William Páez (paez.william8 at gmail.com)
        @date 03-08-2018
        """

        return self.address

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @date 19-08-2018
        """

        verbose_name = _('Ubicación')
        verbose_name_plural = _('Ubicaciones')

class AcademicLevel(models.Model):
    """!
    Clase que contiene los datos de nivel académico

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 03-08-2018
    """

    ## Establece la dirección exacta
    name = models.CharField('nombre', max_length=50)

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author William Páez (paez.william8 at gmail.com)
        @date 03-08-2018
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @date 19-08-2018
        """

        verbose_name = _('Nivel Académico')
        verbose_name_plural = _('Niveles Académicos')