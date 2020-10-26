from django.db import models


class Person(models.Model):
    email = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128, null=True)
    courses = models.ManyToManyField('Course', through='Membership')

    def __str__(self):
        return self.email


class Course(models.Model):
    title = models.CharField(max_length=128, unique=True)
    members = models.ManyToManyField('Person', through='Membership')
    # members = models.ManyToManyField(Person, through='Membership', related_name='courses') and delete courses fieldy =

    def __str__(self):
        return self.title


# The other thing we're going to do is have the role. Now, the example that you use in local library, they make this
# role, I think a string, which makes me feel bad because I don't like vertical replication of string, even if they're
# sort of from a fixed vocabulary. So what we're going to do here is we're going to do something where we are going to
# create a set of integers and associate those integers with meaning and use them in the admin interface, etcetera. So
# what I'm going to do here is these learner, IA, GSI, Instructor and Admin are just integer numbers, and then I'm going
# to say, I'm gonna make this little tuple of tuples, or a list of tuples as it were, and the learner integer maps to
# the string learners,so we can show that in the user interface. This here is a lot of UI stuff. So in the Admin UI,
# this whole member choices thing affects the Admin UI. When this is all said and done, we basically say the role is an
# integer field, and I like that because it's short and I love integers. How many times have you heard me say I love
# integers? Integers are short and efficient, and instead of it just being any number, it really is, the choices are
# pulled from this thing, which is these possible numbers, which is one, 1,000, 2,000, 5,000 or 10,000, and the default
# value is learner, which means it's a one. So this is a nice, this is basically not it. You could make an integer field
# and we could code in our Python code these numbers and these strings, but there's a lot of value in using the
# administrator interface now, and, having these values known inside the data model, rather than just coding them
# throughout all the Python code that we write. So when this is all said and done, what we have is a two foreign keys,
# two outbound foreign keys, like you would expect, a created_at and updated_at, that's totally maintained by Django for
# us, and then modeled at the connection a role, like are you teacher, are you a student? Okay? That's a little more
# sophisticated, kind of many-to-many model
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    LEARNER = 1
    IA = 1000
    GSI = 200
    INSTRUCTOR = 5000
    ADMIN = 10000

    MEMBER_CHOICES = (
        (LEARNER, 'Learner'),
        (IA, 'Instructional Assistant'),
        (GSI, 'Grad Student Instructor'),
        (INSTRUCTOR, 'Instructor'),
        (ADMIN, 'Administrator')
    )

    role = models.IntegerField(
        choices=MEMBER_CHOICES,
        default=LEARNER
    )

    def __str__(self):
        return 'Person ' + str(self.person.id) + ' <-> Course ' + str(self.course.id)
