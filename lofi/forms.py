from django import forms

class RequestMusicForm(forms.Form):
    article_url = forms.URLField(max_length=100, required=False, label="Article URL")

    text = forms.CharField(required=False, max_length=280, label="Text", widget=forms.Textarea(attrs={
                                                                                'placeholder': 'Insert your own text'}))
    freq_num = forms.IntegerField(required=False)
    rand_video = forms.CheckboxInput()