from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class OwnerListView(ListView):
    """
    Sub-class the ListView to pass the request to the form.
    """


class OwnerDetailView(DetailView):
    """
    Sub-class the DetailView to pass the request to the form.
    """


# So the next thing we're going to look at is how we actually store the data, and the storing of the data is in form
# valid. We're going to override form valid. Remember, when the post data comes in we're going to first calls form valid
# that checks to see if the things are the right length, if it's a date, it's the right format, who knows what it does.
# But we're also going to override it and stick our own code in form valid. So in the CreateView, it sends out a blank
# form and then incomes the data but we never showed owner. Let's go back a little bit. So if we're going CreateView,
# the form that we're going to send out is title and text. There is no owner field. Now this owner is required, and so
# we have to get the owner in. So what we do here, it's really quite simple. So again, there's a form object which is
# like the UI side of things, and then there's a model object. So form.save commit equals false says, "Just copy the
# data into an object as if we were going to store it, but don't actually store it, commit equals false is make it but
# don't store it." Then we're going to add the owner field, which is there to be self request user. Now self request
# user remember is 16. At some number, it's the primary key of the user, and so that's going to copy 16 in here and then
# we're going to save it. But then we're also going to do the validation and call the super to do form validation for us
# So we're calling the CreateView form validation as well to make sure everything else is done properly.

# So OwnerCreateView, LoginRequiredMixin. And I do this because I don't want to trust the user who's writing this view
# to put the LoginRequiredMixin here. Because I am writing code right here that depends on the fact that this person is
# logged in. So this is like a guardian pattern, I'm putting this in here, so I don't end up with trace backs inside my
# code. If I didn't put LoginRequiredMixin in order to CreateView then and they forgot to user.py, they forgot to put it
# in an article CreateView. Then this code would blow up, it would trace back at when I tried to set object owner to
# self.request.user. It would just blow up. So I'm extending CreateView, which is inheriting all the functionality and
# I'm only going to override one method, this object orientation.
class OwnerCreateView(LoginRequiredMixin, CreateView):
    """
    Sub-class of the CreateView to automatically pass the Request to the Form
    and add the owner to the saved object.
    """

    # Saves the form instance, sets the current object for the view, and redirects to get_success_url().
    def form_valid(self, form):
        print('form_valid called')
        my_object = form.save(commit=False)
        my_object.owner = self.request.user
        my_object.save()
        return super(OwnerCreateView, self).form_valid(form)


# When we first do a get request, if we go look at the documentation, it says, I want to show you the old data in a form
# and I'm going to call a function called get query set in generic update view. If I can't get anything, if I don't get
# anything, I'll give you an error. So this is like to a URL like slash edit slash two. If the two is not in the
# database, then you're going to get a 404. So we call get_queryset. So let's just take a look at get_queryset. So the
# way we're going to do this is because we're in the middle of an update, the user is intending to modify it, which
# means we're not going to let them modify it unless they're the actual owner. So what we're going to do is we're going
# to override the queryset. I just put a print statement in for yucks. So the first thing we're going to do is get the
# default query set. This is going to pick the model that we're going to query and it's probably going to say something
# like, the primary key is whatever that number was, two or 14, and so we're going to actually get a query set back. So
# that says, "Super go into update view and go run its query set and then give me back that query set." Then what I'm
# going to do after I get that query set is add a end clause to filter it that says, "Okay whatever that primary key was
# fine," and the owner column of this model must match the current logged in user. So it's like I'm adding a where
# clause in the end of the where clause. The other thing that you'll notice here is login required mixin. I could have
# put login required mxin in the views.py, but I need to have this variable self request user properly defined, which
# means any owner update view, you really can't use it unless you're logged in. So it's like I'm going to put the login
# required mixin here that's like a marker interface that says, "Look, if you're not logged in send them to login and
# then they come back here, and if they can't log in, I'm never going to let them run this code." Because if you let a
# non logged in user run this code, it would blow up right there. So in a sense, this is like a guardian pattern that
# say, "Don't even bother coming in here if you're not properly logged in and you don't have a user object properly
# passed in as request.user." So that's why I put login required mixin there. So the key here is we're going to do a
# where clause that is where id equals seven and owner equals 14, whatever the current logged in user is. So that means
# that when you come in here, if you're trying to edit a thing, you're going to get a 404. If it doesn't exist, you're
# going to get a 404, or if you don't own it, you're going to get a 404, 404 is not found and it's legit to say it might
# be there, but you didn't find it because you were trying to read it for updating. So by changing get query set, in a
# sense to return zero records when you don't own the record because this is an UpdateView.

# So queryset was called when it's loading ID number four,so it's going to do a load. So queryset is not the actual load
# but it is the query to the database that we're going to do. So what I'm going to do is I'm going to tweak the queryset
# and this queryset is probably going to say show me Where ID equals 4, all right, it's going to say something like,
# select from articles where ID equals 4. And if I just did the normal query set, it would work, but I'm going to change
# the query set. I'm going to change the query set. So what I'm going to do is I'm going to call the default
# get _queryset and the super class, which is the delete view class. And that's going to say query where the primary key
# equals 4. In this particular case, but then what I'm going to do is I'm going to add another filter. This is like and,
# and owner equals the current logged in user. So so number 4 is owns by user 2 but a logged in user is one. So this is
# going to be and logged in as user 1 so when it does the query says give me the thing that side equals 4 and user ID
# equals 1. It's going to get no records. And so as the delete code for the update my looking at delete update and
# delete all the same here. Before it does an update. It has to load the old data and I have made it, so that if you're
# not loading data on something that you own and it's going to give you a 404. So it's like that wasn't found now for
# does exist. It just doesn't exist for the current logged in user, but five does and it does belong to me, right. Now,
# the other thing is, is when it's going to call get_quertset again, new stuff, x y z 1 2 3, so when you submit it, it
# actually is going to call get-queryset one more time.
class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    """
    Sub-class the UpdateView to pass the request to the form and limit the
    queryset to the requesting user.
    """

    def get_queryset(self):
        print('update get_queryset called')
        """ Limit a User to only modifyng their own data. """
        qs = super(OwnerUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user)


# It actually does it runs this code again and it reads the thing and if it can't read it, then it won't let you update
# it. And so that protects you from people breaking in and attacking there and the owner delete view is the same thing.
# So if you go into delete it does a get_queryset and I add this filter to say and it has to belong to the right person.
# So if I try to delete article 4 boom, it says I can't load article 4 but if I come over here and I'll get a log back
# in and so this one I think was seaside.
class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    """
    Sub-class the DeleteView to restrict a User from deleting other
    user's data.
    """

    def get_queryset(self):
        print('delete get_queryset called')
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)

# References

# https://docs.djangoproject.com/en/3.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.form_valid

# https://stackoverflow.com/questions/862522/django-populate-user-id-when-saving-a-model

# https://stackoverflow.com/a/15540149

# https://stackoverflow.com/questions/5531258/example-of-django-class-based-deleteview
