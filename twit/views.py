from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from .models import Tweet
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    latest_tweets = Tweet.objects.order_by('-pub_date')[:10]
    template = loader.get_template('twit/index.html')
    context = {'latest_tweets': latest_tweets}
    return render(request, 'twit/index.html', context)

def tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    user = tweet.user
    context = {'user': user, 'tweet': tweet}
    return render(request, 'twit/tweet.html', context)
