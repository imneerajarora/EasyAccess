from django import forms
from .models import documentation , AITool , DataFeedback , category

class DocumentationForm(forms.ModelForm):
    class Meta:
        model = documentation
        fields = ['icon','title','description','link']


class AIToolForm(forms.ModelForm):
    class Meta:
        model = AITool
        fields = ['icon','title','description','link']


class FeedForm(forms.ModelForm):
    class Meta:
        model = DataFeedback
        fields = ['user_name','user_email','feedback_text']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100,label='search' ,required=False)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ['name']
    
    
