from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core import serializers
from twitmaker.models import Tweet
from twitmaker.forms import TweetForm
import ipdb


def index(request):
    tweets = Tweet.objects.all()
    context = {'tweets': tweets, 'form': TweetForm()}
    response = render(request, 'index.html', context)
    return HttpResponse(response)


def create_tweet(request):
    form = TweetForm(request.POST)
    tweet = form.instance
    if form.is_valid():
        form.save()
        if request.is_ajax():
            tweet_json = serializers.serialize("json", [tweet], fields=('message', 'created_at'))[1:-1]
            data = { 'tweet': tweet_json }
            return JsonResponse(data)
        else:
            return HttpResponseRedirect('/')
    else:
        context = {'tweets': Tweet.objects.all(), 'form': form}
        return render(request, 'index.html', context)
