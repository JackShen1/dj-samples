from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.http import JsonResponse, HttpResponse
from chat.models import Message
from datetime import datetime, timedelta
import time


class HomeView(View):
    def get(self, request):
        return render(request, 'chat/main.html')


def jsonfun(request):
    time.sleep(2)
    stuff = {
        'first': 'first thing',
        'second': 'second thing'
    }
    return JsonResponse(stuff)


class TalkMain(LoginRequiredMixin, View):
    # For my online system, all it's doing is it's throwing away chat messages that are more than 60 minutes old.
    # You could put code in there like this but it really doesn't implement it, it just is something because of
    # samples that's online. Don't worry about that. What it's really doing here is just rendering chat/talk.html.
    # So that's what the GET request is. So that means if we just hit "Enter" here, I'll come here, hit "Enter" here
    # that's what happens. Then a few seconds later, I get the messages show up. But you should also notice that
    # when I just hit "Enter" and I do a GET request to that page, for a little while I see a spinning GET. So that
    # all happens here in chat/talk.html. But before we leave the view, it's pretty straightforward, when we hit the
    # "Chat" button here, it's going to send a post data and then the name of this form, and inspect element, that's
    # what I wanted. The name of this thing is a name message. So I'm going to say request post message, and I'm
    # going to set the owner field. This is just a message model, and I'm going to store it and I'm going to
    # redirect back to the GET request. So that's how I do cool new message, and that's what happens when I press
    # this button. Now we're going to find out how in this other tab, cool new message shows up two seconds ago. I
    # did nothing in here other than navigate the tab.
    def get(self, request):
        time_threshold = datetime.now() - timedelta(minutes=60)
        Message.objects.filter(created_at__lt=time_threshold)

        return render(request, 'chat/talk.html')

    def post(self, request):
        message = Message(text=request.POST['message'], owner=request.user)
        message.save()
        return redirect(reverse('chat:talk'))


class TalkMessages(LoginRequiredMixin, View):
    def get(self, request):
        messages = Message.objects.all().order_by('-created_at')[:10]
        results = []
        for message in messages:
            result = [message.text, naturaltime(message.created_at)]
            results.append(result)
        return JsonResponse(results, safe=False)

# References

# https://simpleisbetterthancomplex.com/tutorial/2016/07/27/how-to-return-json-encoded-response.html
