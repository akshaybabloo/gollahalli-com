from django import forms

from gollahalli_cms.blog.models import PostModel


class PostForm(forms.ModelForm):
    """
    Model form for BlogModel.
    """

    meta_title = forms.CharField(required=False)
    meta_body = forms.CharField(widget=forms.Textarea(), required=False)
    code_injection_header = forms.CharField(widget=forms.Textarea(), required=False)
    code_injection_footer = forms.CharField(widget=forms.Textarea(), required=False)
    twitter_card_title = forms.CharField(required=False)
    twitter_card_body = forms.CharField(widget=forms.Textarea(), required=False)
    facebook_card_title = forms.CharField(required=False)
    facebook_card_body = forms.CharField(widget=forms.Textarea(), required=False)

    class Meta:
        model = PostModel
        fields = '__all__'
