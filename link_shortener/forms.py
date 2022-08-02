from django.forms import ModelForm
from link_shortener.models import ClippedLinks


class UrlUserForm(ModelForm):
    class Meta:
        model = ClippedLinks
        fields = ( 
            'original_link',
        )
