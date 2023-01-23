from django import forms
from .models import *



class AddNewPost(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Kategorya tanlang'

    class Meta:
        model = New
        fields = ['cat', 'title', 'slug', 'content', 'photo', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }





















    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Kategoriya")
    # title = forms.CharField(max_length=225, label="Sarlavha", widget=forms.TextInput(attrs={'class': 'form-input'}))
    # slug = forms.SlugField(max_length=225, label="URL")
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 15}))
    # photo = forms.ImageField(label="Rasm")
    # is_published = forms.BooleanField(label='Nashr etilgan', required=False, initial=True)