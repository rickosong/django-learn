from perpustakaan.models import Buku
from django import forms
from django.forms import ModelForm

class FormBuku(ModelForm):
    class Meta:
      model = Buku
      fields = ['judul','penulis', 'jumlah', 'penerbit' ,'kelompok_id']

      widgets = {
        'judul' : forms.TextInput({'class':'form-control'}),
        'penulis' : forms.TextInput({'class':'form-control'}),
        'penerbit' : forms.TextInput({'class':'form-control'}),
        'jumlah' : forms.NumberInput({'class':'form-control'}),
        'kelompok_id' : forms.Select({'class':'form-control'}),
      }