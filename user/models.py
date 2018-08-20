from django.db import models
from django.contrib.auth.models import User
from base.models import Location
from django.utils.translation import ugettext_lazy as _
from base.models import AcademicLevel

# Create your models here.

class Profile(models.Model):
    """!
    Clase que contiene los datos del perfil de un usuario del sistema

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 03-08-2018
    """

    ## Nivel académico
    academic_level = models.ForeignKey(AcademicLevel, on_delete=models.CASCADE, verbose_name='nivel académico')

    ## Establece la relación entre la ubicación geográfica y el perfil
    location = models.OneToOneField(Location, on_delete=models.CASCADE, verbose_name='ubicación')

    ## Establece la relación entre el usuario del sistema con el perfil
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='usuario')

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author William Páez (wpaez at cenditel.gob.ve)
        @date 03-08-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Una cadena de caracteres con el nombre y apellido del usuario
        """

        return '%s %s' % (self.user.first_name, self.user.last_name)

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @date 03-08-2018
        """

        verbose_name = _('Perfil')
        verbose_name_plural = _('Perfiles')