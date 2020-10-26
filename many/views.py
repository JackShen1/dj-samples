from django.views import generic
from many.models import Person, Course, Membership


class MembershipListView(generic.ListView):
    model = Membership


class MembershipDetailView(generic.DetailView):
    model = Membership


class PersonListView(generic.ListView):
    model = Person


class PersonDetailView(generic.DetailView):
    model = Person


class CourseListView(generic.ListView):
    model = Course


class CourseDetailView(generic.DetailView):
    model = Course
