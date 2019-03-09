from django.forms import ModelForm, Textarea
from twitmaker.models import Tweet

class TweetForm(ModelForm):
    message = Textarea()

    class Meta:
        model = Tweet
        fields = ['message']
