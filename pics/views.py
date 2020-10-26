from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from myarts.owner import OwnerListView, OwnerDetailView, OwnerDeleteView

from pics.models import Pic
from pics.forms import CreateForm


class PicListView(OwnerListView):
    model = Pic
    template_name = "pics/list.html"


class PicDetailView(OwnerDetailView):
    model = Pic
    template_name = "pics/detail.html"


class PicCreateView(LoginRequiredMixin, View):
    template_name = 'pics/form.html'
    success_url = reverse_lazy('pics:all')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    # So this one's nice, less than two, and I'm going to hit "The post.'' So I'm going to I hit the 'Submit.' Now, the
    # post is going to come through and it's going to run this code right here. This is probably the trickiest part of
    # this code. So if you recall, we can construct a CreateForm and get it back, and we pull the data, request.POST.
    # Now, it turns out that these little attached files like apple-iphone-sakai.jpg comes in request.FILES, and/or none
    # is just in case it's not there. So what happens is this is where we're going to do some of our work. We're going
    # actually pull data from this request.FILES. So we're going to jack into the clean. So as a side effect of clean,
    # you're saying, is the form valid? If there was an error from this or if there was an error like my title was too
    # short, then it would come back and say title is greater than two characters. "Oh, we love crispy forms, a couple
    # of pretty errors are in crispy forms." That is running this little bit of code right here. If the form is not
    # valid, and it could've been and in that particular case, the super got upset because this min length validator
    # triggered, and so the super got upset, and set form was not valid. Now, mine looked good, but now the picture is
    # gone. So I can make a slightly longer title here and browse completely.
    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        #  So here's what's happening. So you've got the form, the form has took all that data including the file, and
        #  cleaned it all up, and I'm going to call form.save commit equals false, and then I'm going to set the owner
        #  field because I'm not extending owner view here. So I got to set that owner view because I'm going to
        #  ultimately override both this post and the get, and I wasn't going to get much help out of owner at that
        #  point, and then I'm going to save the model. So form.save gives me back a model. If I don't say commit equals
        #  false, it actually does the pic.save also. So if you save the form without commit equals false, commit equals
        #  false means don't store in the database. So let's take a look at what's going on here in form.save. So I have
        #  also overridden form.save, and I'm just behaving, commit equals true is the default. But when I say commit
        #  equals false, then commit will be false, and so I have got to call the super. Actually, this is really not
        #  right. No matter what the commit is, this is the end user's wish for commit. I'm going to do a super, and I'm
        #  going to run a save with commit false. No matter what this person wants if they will give commit true or not,
        #  I'm going to run commit false, then what I got to do is I got to grab the picture, the picture from the form,
        #  I'm in a form, and I check to see if this is an in-memory uploaded file. There's all cool magic that's
        #  happening right here, it's got this all, it's in memory, it's got this thing, it's an object, it's really
        #  nice, and then what I say is give me all the data, the byte array, which reads all of the pixels of the file,
        #  and then f.content_type is that image/PNG. I then need to put that in the instance, which is the model, I've
        #  got to add to it the byte array of the text, and the content type. I've got to store both of those things,
        #  and now I'm talking to the database, the picture and the content type are being set as part of the save.
        #  Then what I do is, if commit is true, now I'm trying to mimic the save behavior. Now I'm only using this one
        #  way with commit equals false, but someone might leave this out and call my form. I'm supposed to actually
        #  save the model if commit is true, but in this case, commit will be false, so I'm just going to return that
        #  instance. At this point, I have an object model, and in that object model all these two fields are exactly
        #  the way they want to be, and the only thing I've got to do is set the owner field, which I'm doing right
        #  there, and then I'm storing it in the database, and then I redirect, and that's how it works.

        # Add owner to the model before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)


# So I'll just go through the update view because it's not that different than the create view. So it looks the same on
# the get. We're going to go grab the old copy out of the database, and then we're going to make a form and inherit all
# the old data. Now in this one, it's not going to put the picture out there, it'll just put out a new one. So I'll just
# go through the update view because it's not that different than the create view. So it looks the same on the get.
# We're going to go grab the old copy out of the database, and then we're going to make a form and inherit all the old
# data. Now in this one, it's not going to put the picture out there, it'll just put out a new one.
class PicUpdateView(LoginRequiredMixin, View):
    template_name = 'pics/form.html'
    success_url = reverse_lazy('pics:all')

    def get(self, request, pk):
        pic = get_object_or_404(Pic, id=pk, owner=self.request.user)
        form = CreateForm(instance=pic)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        pic = get_object_or_404(Pic, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.save()

        return redirect(self.success_url)


class PicDeleteView(OwnerDeleteView):
    model = Pic
    template_name = "pics/delete.html"


# If we go back to URLs now, that's this one, and it goes into views.stream_file and it passes in an integer number as
# the variable pk, so let's go take a look at that. So that's this one. You'll notice that this is not a class-based one
# it's an old-school one mostly because hey, I'm just going to do get. In class-based one, we can do def get and def
# post, but this one I'm just going to do an old-school thing. Passes in the request in the first parameter, which of
# course is that number 3, that's the primary key of the image that we're trying to see. So I'm going to do a
# get_object_or_404 and of type pic and I'm going to look it up by its primary key, which is that three, and now I have
# it. So I'm going to send an HTTP response but this is not a text response nor it's an HTML response. This is where
# that content_type. Going back to the model, remember this is the MIMEType, that image/png \
# Now, if I hit refresh, you're going to see that it's coming back and the response content-type is in image.png. So to
# set that, to set this, and that's essential so that when the browser is seeing the pixels, it knows that this is a PNG
# and not a JPEG, or a GIF, or MPG, or a PDF or whatever. So this content-type is something that we stored. We got it
# when we are doing the post and we pulled it in, we took all that stuff and if you look at forums.py, that was grabbing
# it here in the save method and we got it from the form and then we stored it in the database and now we've got it back
# from the database. So we're just saying the content-type which is a header is pic.content_type, that's a string, and
# then we also have to tell how long it is but pic.picture is the actual pixels that are in the picture, and you have to
# tell how long it is, so if you look at content-length right there, 470,152. Yeah, 470,452. So that's Content-Length.
# We knew that from the database. Then we actually write the pixels. The place you see this is when you click on
# response. Now, it's basically showing you, that's a picture. But if you really looked at it just bits and bytes and
# incomplete jibberish. So that's what it takes to send that stream out. So that's what makes it so that when I have an
# image tag, when I have this image tag, I can source, but I'm actually feeding that picture.
def stream_file(request, pk):
    pic = get_object_or_404(Pic, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response
