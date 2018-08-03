from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Country, State, City

class LocationForm(forms.Form):
    """!
    Clase que muestra el formulario de ubicación geográfica

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 03-08-2018
    """

    ## Estado o Entidad en donde se encuentra ubicado el municipio
    country = forms.ModelChoiceField(
        label=_("País:"), queryset=Country.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip',
            'title': _("Seleccione el país donde se encuentra ubicado"),
            'onchange': "combo_update(this.value,'base','State','country','pk','name','id_state')"
        })
    )

    ## Estado o Entidad en donde se encuentra ubicado el municipio
    state = forms.ModelChoiceField(
        label=_("Estado:"), queryset=State.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'disabled': 'true',
            'title': _("Seleccione el estado donde se encuentra ubicado"),
            'onchange': "combo_update(this.value,'base','City','state','pk','name','id_city')"
        })
    )

    ## Ciudad en donde se encuentra ubicada la dirección suministrada
    city = forms.ModelChoiceField(
        label=_("Ciudad:"), queryset=City.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'disabled': 'true',
            'title': _("Seleccione la ciudad donde se encuentra ubicado")
        })
    )

    ## Dirección exacta del usuario
    address = forms.CharField(
        label=_("Dirección:"),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _("Indique la dirección exacta en donde se encuentra ubicado"),
            }
        )
    )
