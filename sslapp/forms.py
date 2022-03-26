from .models import sslSiteModel
from bootstrap_modal_forms.forms import BSModalModelForm

class SslCheckModelForm(BSModalModelForm):
    class Meta:
        model = sslSiteModel
        fields =['ssl_title','ssl_site','ssl_desc','ssl_author'] 