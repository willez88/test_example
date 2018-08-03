from django.db import models

# Create your models here.

class Country(models.Model):
    """!
    Clase que contiene los paises

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 03-08-2018
    """

    ## Nombre del pais
    name = models.CharField(max_length=80)

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author William Páez (paez.william8 at gmail.com)
        @date 03-08-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return string <b>{object}</b> Objeto con el nombre del país
        """

        return self.name

class State(models.Model):
    """!
    Clase que contiene los estados

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 03-08-2018
    """

    ## Nombre del Estado
    name = models.CharField(max_length=50)

    ## Pais en donde esta ubicado el Estado
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author William Páez (paez.william8 at gmail.com)
        @date 03-08-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return string <b>{object}</b> Objeto con el nombre del estado
        """

        return self.name

class City(models.Model):
    """!
    Clase que contiene las ciudades

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 03-08-2018
    """

    ## Nombre de la Ciudad
    name = models.CharField(max_length=50)

    ## Estado en donde se encuentra ubicada la Ciudad
    state = models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author William Páez (paez.william8 at gmail.com)
        @date 03-08-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return string <b>{object}</b> Objeto con el nombre de la ciudad
        """

        return self.name

class Location(models.Model):
    """!
    Clase que contiene los datos de una ubicación geográfica

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 03-08-2018
    """

    ## Establece la dirección exacta
    address = models.CharField(max_length=500)

    ## Establece la relación entre la parroquia y la ubicación
    city = models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author William Páez (paez.william8 at gmail.com)
        @date 03-08-2018
        """

        return self.address

class AcademicLevel(models.Model):
    """!
    Clase que contiene los datos de nivel académico

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 03-08-2018
    """

    ## Establece la dirección exacta
    name = models.CharField(max_length=50)

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author William Páez (paez.william8 at gmail.com)
        @date 03-08-2018
        """

        return self.name