from forums.models import Forum, Comment

from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from forums.forms import CommentForm
from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class ForumListView(OwnerListView):
    model = Forum
    template_name = "forums/list.html"


# OwnerDetailView extends DetailView, which basically demands a primary key. There is this primary key value that's
# going to come in and that's going to come in from the DetailView, which is the second parameter which is forum/3.
# So we're going to go grab and load that object. I could've made that a getter 404. I probably actually should've made
# that a getter 404. So that's going to load the forum object, and the forum object is the title and the text and the
# owner of the forum itself. But then what I'm going to do is, I'm going to say, ''Go get me all of the comment objects
# filtered, so that the forum value in the model equals the current forum.'' That is the forum we just loaded. That's
# forum key in the model. So the first one is this forum in models, and the second one is this variable, I could have
# changed this to be, I'm not going to change it, but I could have changed this to be x. I could change this to be x.
# Not going to save it, although it might be end up to save it. Make sure I got all of comment form. Let's just make
# this to be x too because that's the variable. I hope I don't break the code by doing this. I'm trying to show you that
# this is a field in the model, and this is just a variable in this view. So this is going to give us a list of comments
# In a sense, this is like a ListView. If you're dealing with a ListView, you got to write a for loop to go through it
# in the thing. So we got all the comments for this thing, and we're passing in the comment form that's simply
# constructing it. It's constructing this comment form. Then, we're going to basically render the request. So we'll
# close that one. So let's take a look at this detail page. This detail page is what generates this forum. A lot of it's
# pretty much the same. Check to see if you're the owner before you put up the little button, little pencils, that's
# quite nice. Print out the forum title, print out the forum text.
class ForumDetailView(OwnerDetailView):
    model = Forum
    template_name = "forums/detail.html"

    def get(self, request, pk):
        x = Forum.objects.get(id=pk)
        comments = Comment.objects.filter(forum=x).order_by('-updated_at')
        comment_form = CommentForm()
        context = {'forum': x, 'comments': comments, 'comment_form': comment_form}
        return render(request, self.template_name, context)


# CommentCreateView, so CommentCreateView is what's going to happen when I get this post. So the post is going to come
# in, there's going to be a comment field, which is this text field, and there is the primary key of the forum, not the
# comment. So now we are going to make that connection. This is where we're actually making the connection. You'll
# notice that I'm just saying login required view and view because I don't have an automated way to do this. So I'm
# going to do it by hand. So we're in the post. We're going to go grab the forum object by applying primary key. There
# I'm using a get 404 so at least I blow up in the right way. Then what I'm going to do is I am going to, let's go back
# to models, I've got to fill out the TextField, the ForumField, and the OwnerField. The OwnerField are the two foreign
# keys, and we'll come back, in the many-to-many, we have to have those objects available to us. So we're going to build
# a new comment that doesn't store the database. The TextField comes from the request post. The OwnerField is current
# request user, and the ForumField, the foreign key in this middle connector table is this forum object that we just
# loaded. So that fully populates a comment object. It fully populates a comment object in that post method. Then all we
# have to do is we have to say save it. So the comment.save takes that in-memory comment that we created with the two
# foreign keys in the comment and sticks it in the database. Then all we have to do is redirect. Now, what we want to
# redirect back to is we only redirect back to this detail page because we don't want to redirect back to ourselves, and
# we don't want to redirect back to all forums. So when we hit Submit, we want to come back here. So it just looks like
# that thing showed up, but really it was a full request-response cycle where it posted to CommentCreateView, but after
# the post was done, it did a redirect. We're doing post redirect, so it's cool anyways. So this is a slightly different
# version of the reverse. It is the same concept as what we've seen all along where we have like a forum ID inside a
# second parameter to the URL, because the reverse in this URL thing, I wish they'd call this reverse because that's
# what it's doing. The URL is just a wrapper for reverse. Well, this is the two-parameter form. So we have a
# one-parameter form of URL, which is this one which says go URL forums colon all, says give me the URL to the view that
# is named all within forums. Here I'm saying URL forums, forum create forum ID. This is saying this one needs a primary
# key because if you go into urls.py, the forum_create demands a parameter, and so we're feeding it. But you can also
# feed that in, in a reverse, and you do it with this funky format. I wish that was by position. No, it's not. We have
# this args keyword and it's sending in a list of variables, and the variable is the primary key, which is the number
# which is this three. So we're redirecting to forum/forum/3. That's where the three comes from.
class ForumCreateView(OwnerCreateView):
    model = Forum
    fields = ['title', 'text']
    template_name = "forums/form.html"


class ForumUpdateView(OwnerUpdateView):
    model = Forum
    fields = ['title', 'text']
    template_name = "forums/form.html"


# So the only thing to look at next is what happens when I hit the Delete button. So let's take a look at the detail
# page. So remember that we cannot delete in a get, but we have to delete in a post. So in here, this is the trash can.
# The trash can is not going do the deleting, the trash can is going to link to forums comment delete with comment ID.
# So there's this number 3, but each of these comments has a comment ID. So let's just inspect. You can see in the
# bottom, it's comment 7. This one is comment 4, and so that is the comment ID. Because we're looping in this code, we
# are looping through four comment in comments. So each comment as the primary key. So with all that, I am just going to
# click on it, and of course, we're going to have a verification page that turns the get into a post in a sense. I mean,
# it's just a page. So we've gone to comment delete views. So forums, comment, 7, delete. If you look at the urls.py;
# forums, comment, 7, delete. We give it a name and we're going to route through to CommentDeleteView. So if we take a
# look at our comment delete view, well, what's pretty cool is that we can mostly use OwnerDeleteView because by now we
# know it, the object, we know that we're in the comment model, template we're going to work with, is comment delete,
# which is pretty straight forward. So it's going to go find, and so you'll notice we don't have a get in here, we don't
# have a post in here, and that's because we're inheriting all that from OwnerDeleteView.
# Now, the only thing we're overriding is the get of the success URL. Because the success URL, when we're all done, we
# want to go back to the forum, not 7, but 3. See how we're going to go back to form 3, and it looks like that just went
# away. So the success URL is actually needs to be computed based on the current forum. So we are overriding the
# get_success_url, which is part, not exactly of OwnerDeleteView, but the models, the GenericDeleteView. We are
# returning a string, and if you go and you read self.object points to the current comment. So if this is, we're in the
# middle of comment for delete while we're running in this view, self.object is the comment. That's number 4, comment
# number 4. But comment number 4.forum is the primary key of the forum that this object belonged to. By the time we're
# here getting the success URL, it's actually been deleted, but we still have in-memory copy of it, so we're going to go
# to the forums. Oh, no, I do not intend otherwise. I was dragging it by mistake, trying to highlight it. So it's been
# deleted, but we'd have it sitting here in the memory, and so we can get its former primary key.
# Object doesn't exist in the database anymore, but the memory copy does, and so we know what that number is. So then we
# go to this fancy reverse again with a parameter, and so that's how we get back. Let's see what happens in the cancel.
# So the cancel does this.The cancel generates the URL forum detail with a comment, which is the current object, and
# then a foreign key into forum and the primary key of the forum, so comment forum ID is what generates this URL. There
# is that URL, it goes back to the forum detail page. So if I go "Cancel", it goes back to the right page. That's
# because comment, you're walking the foreign key in this particular situation. I think that we pretty much have covered
# everything, just check the views, we've covered pretty much everything that's unique in this particular bit of code.
# Again, the new part here is to have a connector model and then have a many-to-many field.
class ForumDeleteView(OwnerDeleteView):
    model = Forum
    template_name = "forums/delete.html"


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        f = get_object_or_404(Forum, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, forum=f)
        comment.save()
        return redirect(reverse('forums:forum_detail', args=[pk]))


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "forums/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        forum = self.object.forum
        return reverse('forums:forum_detail', args=[forum.id])
