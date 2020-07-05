from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
import random

from .forms import TweetForm
from .models import Tweet

# Create your views here.

def home_view(request, *args, **kwargs):
   return render(request,"pages/home.html", context={}, status=200)

def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = TweetForm()
    return render (request, 'components/form.html', context={"form": form})

   
def tweet_list(request, *args, **kwargs):
    obj = Tweet.objects.all()
    tweet_list = [{"id": x.id, "content": x.content, "likes": random.randint(0,100)} for x in obj]
    data = {
        "response" : tweet_list
    }
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):

    data = {
        "id" : tweet_id,
    }
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
        status = 200
    except:
        data['message'] = "Content not found"
        status = 404

    return JsonResponse(data, status = status)