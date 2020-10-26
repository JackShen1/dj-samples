from myarts.models import Article
from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class ArticleListView(OwnerListView):
    model = Article
    # By convention:
    # template_name = "myarts/article_list.html"


class ArticleDetailView(OwnerDetailView):
    model = Article


# Now, the one thing that's different about the create and update is there are two things. There's a form which tells
# what shows up on the screen, and then there is the model back here that shows up what's ends up in a database. So the
# article model is what's in the database, the form is what we show on the screen. So the model is which model is in the
# database and fields are which model fields are to be put on the screen. We're not going to show all of the fields on
# the screen. In particular, we're not putting the owner field in, because we're not letting the user say this is owned
# by number 12. If it's owner 12, great. That number 12 is the current logged in user, it's not something we let the
# user see. So we don't put owner in here, we put the title and the text. We don't put updated at or created at, all the
# things from the model. We have to tell that we want this to put in the form and that to put in the form, this is going
# to be handled internally, and all these three are going to be handled internally. Owner created at and updated, at are
# handled internally, text and title are to be shown to the user.
class ArticleCreateView(OwnerCreateView):
    model = Article
    fields = ['title', 'text']


class ArticleUpdateView(OwnerUpdateView):
    model = Article
    fields = ['title', 'text']


class ArticleDeleteView(OwnerDeleteView):
    model = Article
