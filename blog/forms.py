from django import forms

from blog.models import BlogModel


class BlogForm(forms.ModelForm):
    """
    Model form for BlogModel.
    """

    tags = forms.CharField(required=False)
    meta_title = forms.CharField(required=False)
    meta_body = forms.CharField(widget=forms.Textarea(), required=False)
    code_injection_header = forms.CharField(widget=forms.Textarea(), required=False)
    code_injection_footer = forms.CharField(widget=forms.Textarea(), required=False)
    twitter_card_title = forms.CharField(required=False)
    twitter_card_body = forms.CharField(widget=forms.Textarea(), required=False)
    facebook_card_title = forms.CharField(required=False)
    facebook_card_body = forms.CharField(widget=forms.Textarea(), required=False)

    class Meta:
        model = BlogModel
        fields = '__all__'
