from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from twitmaker.models import Tweet
from twitmaker.forms import TweetForm
import json
import datetime, dateutil


def index(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    context = {'tweets': tweets, 'form': TweetForm()}
    return render(request, 'index.html', context)


def create_tweet(request):
    form = TweetForm(request.POST)
    tweet = form.instance
    if form.is_valid():
        form.save()
        return JsonResponse({'message': tweet.message, 'created_at': tweet.created_at})
    else:
        context = {'tweets': Tweet.objects.all(), 'form': form}
        return render(request, 'index.html', context)
