from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from autos.models import Auto, Make
from autos.forms import MakeForm


# So the fun starts to happen when we're in the views.py. So login mixin, if you remember from the author of z
# walk-through, you just add this to a view and it just basically says you cannot get to this view unless you're
# logged in and if you aren't logged in, it will bumps to the login.html file and then bounce back after you're done.
# So LoginRequiredMixin is all we need to do. If you go to the author z sample, you'll see like I did that by hand.
# You don't wanna do it by hand, you just call login mixin. Now, so this Main view is a list view, and so let's go take
# a look at what this is going to look like. This is the List view. So we're going to take however many audits we have,
# we're going to loop through that list, we're going to retrieve all the audits from the database. Then we're going to
# have an add the auto link, then a view that make's link with a count of how many makes there are and add a make.
# So let me also then go into autos templates, autos again, and auto list. So this is the template that makes that.
# So there's a few things that we get, we get an auto list. Now the names of these are not forced upon you, but there's
# conventions that turn out in a moment, we're going to look really useful. So we're going to get an auto list. If we go
# back into our views, we see that we say, get all of the objects from the auto table, all the auto class objects
# retrieve them all, past them in to the context as auto_list. Now we also want to be able to show that little count,
# this is number two, so we're going to ask, go ahead to the make objects all but don't give me a list of them, count
# them and give me a number. So make count is stuck in there and you'll see if may count is greater than zero.
# We can show the ad and auto button, and it also somewhere shows the make count, view all the makes, add a make, and
# the make count comes out here. So that's another thing we put in. The auto list we're going to go through and that
# iteration variable of auto is going to go through each of the separate things, and nickname, make, etc, that's right
# straight out of the models.py file. There's the four things that every auto has, and we're just printing all this
# stuff out. You also get the primary key, and so we're going to make a update URL, and that URL is to autos:
# auto_update. So if you look in urls.py, we see this auto update looks up, this gives us a path to the view, but that
# particular path needs one parameter which is a primary key, and so that means that this URL template tag, autos has to
# have the auto.id. But because we're looping through the models, you got one, and you do an auto_create, that's pretty
# straight forward. But one of the rules is, is you have to have at least one make before you can do an auto, because if
# you recall, add an auto has to have this dropdown list populatable and that's being pulled from the make table, and so
# that's basically the way around this. That's the main view.

# Create your views here.

class MainView(LoginRequiredMixin, View) :
    def get(self, request):
        mc = Make.objects.all().count()
        al = Auto.objects.all()

        ctx = { 'make_count': mc, 'auto_list': al };
        return render(request, 'autos/auto_list.html', ctx)


# That's the autos view, and then if we do the make view, we're doing the same thing. If we go and look at the make list
# we're doing the same basic thing, view all the makes, and now we got update and delete. This way you don't need to
# count. We just want to grab all of the objects, we want to put it in a context under make list, and then we do make
# list on the HTML, and this is even simpler. It's just going through the make list, it comes in through the context.
# If there's none, we don't print this out, and then we put out the name of it, and then we have an update and a delete
# button that goes to the update and delete, and of course, if you look in urls.py, those also the update and delete
# have primary key requirements, and so you have a primary key that you've got to pass in here to make that URL the
# proper URL, and then just some links to go back to the various things so that we can get back to autos, view makes,
# add a new make. Now, cancel all that stuff. So that is the views.py for listing the autos and the makes. Now, we want
# to make the make create view. So if we take a look at the make create view, that is add a make. That's going to create
# this form. I can make this bigger here. It can create this form, where we're going to put in a thing called Chevy.

class MakeView(LoginRequiredMixin,View) :
    def get(self, request):
        ml = Make.objects.all()
        ctx = { 'make_list': ml }
        return render(request, 'autos/make_list.html', ctx)

# We're going to make it a login required, we're not going to let folks do this. We're going to have some variables that
# are class wide, like what template we want to use, and success_url is after we have done this right. Now, if you just
# submit it and it complains, it doesn't do it. But once you've done it right, where do you want to go afterwards?
# So Chevy, where do you want to go afterwards? This is controller function. I want to go back to the auto list, and so
# the success_url is go to autos:all which in urls.py is this main view. That's the name of the main view, and so if we
# go here, which template to use and which success_url. If we do a get request, we're going to build a form for the make
# that comes from make form, but really it comes from the make model, which is just one string field. As simple as that.
# We're reusing this. We're just saying, let's make a form that pulls from here. We have to pass a form in, because
# models can't be used to create this screen. That screen comes from a form. Okay. If we take a look at the template,
# if we look at the make create template or make form. So that's the template we're going to use to make form.
# We're going to need form_as_table. So that's from how we did forms. Put the CSRF token, you make a table, that could
# be as paragraphs or as tables. But whatever, you need this form object. So you need to pass the form object in.
# So here we are, we're going to make a form and then we're going to the form object in, and then we're going to render
# to self.template autos.makeform html. Then we're going to return that for the get. Then when we hit the button the
# submit button, Add a make, we hit the submit button, it's coming into the post because we made a form post, comes in.
# Don't do that. That's terrible. I hate it when vi does that. But here we go, we're back. Yeah. So post comes in,
# request.POST has all the key value pairs which are these key-value pairs as defined by the form. So we say let's make
# a make form with the initial data coming in from request post. Given that the form generated it, it knows what the
# names of these fields are, and this is something that hides behind how forms work. But it also checks to see if the
# form data is valid and that means we're all these validator rules followed. If the validator rules are not followed,
# if not form is valid, we're just going to send it back. So this code here, this form is not valid code. If I put in a
# single letter A and hit "Submit", it's going to come back and re-render the form and all that errors stuff, all that
# stuff is all handled by this form code, this Django form code figures out what is wrong. Right over just a little bit
# so I can get back to it faster. There we go. It figures out what's wrong with it, makes an error message, the error
# message came from models.py right here. No, right here. Then went through forms.py because it is a form ultimately
# that we inherited from model form. Get it? So that's cool. So that's the error condition, and otherwise we do
# form.save. Now the thing here that's really super cool is because this form is a model form and the field names are
# the same as the field names in the model, and so it actually does a save on the model itself. So in a way the form
# contains the model data that came from the post request and then it saves it. That saves the form. It puts it in, and
# then we just re-redirect back to the request URL. This is pretty succinct me. We pull in the old post data, we check
# to see if it's bad, if it's bad, we send the form back to the exact same template we did and then we save it if it's
# good, and then we pop to the success URL. That is a beautiful thing. But just like in Django all the time, this is a
# far wordier thing to do even though this is super succinct. If you did this in almost any other language, you'd be
# like 75 lines of code, and here we have like 15 lines of code. But it turns out in Django there's almost always a more
# succinct way to do it. We have a generic create view. You can take a look at the documentation for this generic create
# view, django.views.generic.edit. Let's just go and Google this stuff. I always just put a dot here and this usually
# gets me right to because that's the actual package and the class inside the package. Oh, no. Sorry. You thought that
# that was a domain name, so the searching didn't work. But now I'll just say Django, something so at least it's going
# to do with a search for me, generic editing views jump to the CreateView. So you can read through all this stuff,
# generic CreateView actually. Do I have a reference to this?

# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

# o now, I want to show you the hard way of doing an Update. So what's an Update? Let's take a look at the code. So
# let's take a look at view makes. Update is the thing that happens when we go here and that's going to go to MakeUpdate
# So here's MakeUpdate, here's urls.py. It's this one. I mean, look up primary key update, which then if you look under
# here, it's going to be autos lookup one Update. So I'm going to Update the Chevy one. It has to read the old data, has
# to show it to you, and then let us update it and then submit it checking, of course, for any validation errors. Then
# redirecting us back to a success_url. So if we look at the views, we're going to again, foreshadowing, there's a much
# easier way to do this. So we set these variables or the success_url, which template we want, and the model. Then we
# have a get request. Because in the urls.py there's this int:pk, were passed in this pk value. Now, this
# get_object_or_404 is really cool. This get_object_or_404(self.model pk=pk). That's this parameter that we're passing
# pk equals and it's common that they are same name, but this is a parameter to get_object_or_404. This second one is
# the parameter that was called to our get. Self.model, of course, is make. Get_object_or_404 basically checks to see if
# I'll do this update, let's go to makes, let's do an update. What it's doing is it's taking this number, this three
# here, autos/lookup/3/update, and it's retrieving the old data. Now, what happens if I inadvertently have a number that
# doesn't exist in the database, like 9,999, and I do a get request to that one? I get "Page not found 404." So what's
# happening here is somehow you say, "Hey, load this object and give it to me and the variable, make, or just blow up
# and send out a 404 error." So this is telling you what's going on, which view you just, "No Make matches the given
# query." Now, generally you're not supposed to hand type these. Three it works, and so it doesn't blow up.
# So get_object_or_404 is a way of loading the old data and then protecting using that data, or just blowing up.
# So don't go any further at that point. Now, then we're going to make a form and we're going to fill it with the
# old data. So instance, what the instance is make. So that's the object. Make a MakeForm. Here's a MakeForm.
# All the fields from the model inherit from the model Make. Then pass it in to the template make_form.html, which we
# just looked at. This form comes in, that's all we need. This is very generic looking. It really doesn't care too much.
# It's all pretty much encoded in this form, which is derived from the model. Then of course, we type a bunch of stuff
# in and we hit "Submit". It does exactly the same thing as the Create, and that it does well. First it has to do a
# get or 404 because we post to the thing with the primary key. We load it up to make sure we have an object to update.
# Then we create a new make form from that database and then change it. So this is like the starting data, but then it
# alters it to the data. So in this particular case, Chevrolet is the old value in the database. If I say Bowtie,
# request post lab Bowtie, this will start a Chevrolet but in this form object then it will be Bowtie. Of course,
# if it's not valid, we're going to return an error message right back here. If it is valid, we're going to save it and
# so this new Bowtie is going to be saved in there. So if we view our makes, we see that it's now Bowtie, and we're
# going to redirect to success URL. Now, at this point, I would hope you could predict about what's going to happen next

# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

# So there you go. Take a look at that. Now, this just like some of the other views that we've inherited, have a ton of
# functionality in them. So if I want to do an AutoCreate, this is all it takes. Now, AutoCreate and MakeCreate for all
# intents and purposes, do the exact same thing. So what happens in AutoCreate because we're extending CreateView, we
# have three bits of metadata, we tell it which model we want to use, which fields from that model we want, and where
# the success URL to go is. Then this generates all this code. We inherited all that code. You'll notice that there's
# nothing hardcoded in here except the MakeForm. Now, we don't even have to make a form for the Auto because this code
# right here builds the form. Not only that, but it uses this name Auto to pick the template. So if I do auto_form,
# I have to use this. I use this, that's my base bootstrap. Don't worry too much about that. So it knows the name of the
# template that it's going to use. I only have to tell it which template to use in here, because it derives the template
# auto_form.html is the template. Pretty cool. Pretty awesome and cool. So it automatically finds that and the
# success_url. So this is all that's needed. As a matter of fact, in this MakeCreate, I could have deleted all this code
# from here to here, but instead just do a CreateView by extending CreateView. So I'm just showing you this because I
# want you to see what's really going on. But this is not how you write your code. This is how you write your code.


# Take the easy way out on the main table
# These views do not need a form because CreateView, etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes
class AutoCreate(LoginRequiredMixin,CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

# AutoUpdate, extends update view, the generic editing view. It says which model it is, which fields you want, and
# where to go when it's successful. Literally, I could go and say the exact same words for make delete, which is what
# happens when you go in here and you delete and then you have a cancel, there is a confirm delete. The name of this
# template is not randomly chosen, it's got to be called the confirm.delete, the model confirm.delete. There you go.
# You've got to CSRF token. You're handed the make as an object in this. So that produces this output. There's no form
# in this one. There's just the make that gets loaded by object or 404 and then it passes make in and renders it. Then
# when the post happens, it retrieves it. If it's there, a 404 again checking for bad data and deleting it, and then
# hopping off to the success URL. It doesn't take much to guess what I'm going to do next, and that is, if you extend
# delete view, you get all that code for free. You just tell which model fields and where to go for success. So the key
# thing is, as your doing your homework, I'm sure some of you are just going to copy and paste all this stuff. That's
# wrong. The MakeCreate, MakeUpdate, and MakeDelete should be as short as AutoCreate, AutoUpdate, and AutoDelete.
# Because you're going to do these generic editing views a lot and we're going to do CRUD over and over and over again,
# and you really do not want to write 15 lines of code. That's unnecessary repetition, unnecessary cutting and pasting
# and changing code if you can keep it really simple. So I can basically build a full set of CRUD forms and CRUD
# functionality with validation for a model with this code and then I don't even have to have a forms.py, I just have a
# models.py. So if you're doing your Autos, you would think I made a mistake if I'm making a forms.py. Because if I just
# use this views.py this way, instead of making all of them look like MakeUpdate, then you're going to save yourself a
# lot of time and energy and we have to modify these things. It's a lot easier to find all the changes and then modify
# them. So that is a walk-through of the sample code for Autos. You're going to do an assignment on this, but don't just
# copy everything. I've set this up so that the time you spend understanding what's going on, particularly in the views.
# URL is your pride just copy, models you just copy, the URLs you'll just copy, but the views don't just copy it, figure
# out what's really going on and come up with the easier and more succinct way to do all this stuff. Django is starting
# to look really beautiful at this point. So I hope you found this helpful.

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

# We use reverse_lazy rather than reverse in the class attributes
# because views.py is loaded by urls.py and in urls.py as_view() causes
# the constructor for the view class to run before urls.py has been
# completely loaded and urlpatterns has been processed.

# References

# https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/#createview

