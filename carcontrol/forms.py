from django	import forms
from .models import Viagens

class SearchForm(forms.Modelform):
	"""docstring for PostForm"""
	class Meta:
		model = Viagens
		fields = ('viagens_destino')
		