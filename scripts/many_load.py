import csv
from many.models import Person, Course, Membership


# Here's the code that we've got, and we'll see in a second that you can't just run this in Python, you got to run this
# after the whole Django extensions says, load up all the Django stuff and then run my code, as compared to just run my
# code. If you just run your code, that import of many dot models person course membership, it's just going to blow up
# because it hasn't run the settings.py first, you can't do that, but python3 manage.py does do the settings and loads
# all these things and makes it so that this import works, because that's how you access the data models. There's other
# things like it's made the connection to the database, the db sqlite, and figured all that stuff out, you don't write a
# single line of that, and that's all magically done before you start and all you have to do in the script file is make
# a method called run, takes no parameters, and when the script starts it's going to call your run method, so your first
# line and code is right there. What we're going to do is, we're going to open the CSV file. We're going to use the CSV
# library, CSV reader fhand, and we're going to get our CSV reader. This is just a iterable thing that you can go read
# your way through this. It parses the CSV and gives you a nice array out of the CSV, and if there's quotes in there,
# it knows about that and escape characters, and CSV files are complex. The one I showed you is super simple, but you
# may quickly run into a CSV that's got UTF-8 characters in it or who knows what's in it, and you want to use this CSV
# reader rather than just doing a split on commas. The one I gave you, split on commas work but you don't really want
# account on that, you really want to use CSV. Again, it's all built into Python, so Python is awesome, so away we go.
# Now the first thing we do before we get going is we take the Person class,.objects is like a thing we say after the
# class,.objects.all that's like a filter, and then.delete. That is like a delete from person table. Then we're going to
# delete all from the course table and we're going to delete from the membership table. If you go to the person table,
# the membership table, and the course table, if you recall, there was a on delete cascade for both of the foreign key
# relationships coming out of the membership table.
def run():
    fhand = open('many/load.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Person.objects.all().delete()
    Course.objects.all().delete()
    Membership.objects.all().delete()  # redundant if we delete Person and Course, cause CASCADE delete

    for row in reader:
        print(row)

        # Then we're going call person.objects, and this is really cool. A method called get or create. This is either
        # going to retrieve a row that matches the e-mail of the e-mail address because the e-mail address is the 0th
        # element because it's the first element. If it's not there, it will create it and then retrieve it. This is
        # like Python's. This is very much like get in dictionaries, where, if you use get the right way you can
        # basically increment or create something. In this case, we're loading it if it exists, and if it doesn't exist,
        # we're making it and then we're loading it. Part of what we did is we declared this e-mail as unique, and so
        # it's going to load it up. We do that for both the course and the person. We actually here returned a tuple,
        # the p and the c are the objects that we're going to get back for person and create it as a Boolean that tells
        # you whether or not the get or create did it get or it did create. If created is false that means that there
        # was one and we loaded it. If created is true, that means there wasn't one and we created one. Now on our
        # situation, we really don't care whether it was created or not. When these two lines are done, we know that we
        # have a person associate with e-mail, the first parameter, and then then a course associated with the course
        # title, which is the last parameter. If you look back at the CSV, you see there's redundancy or a replication,
        # Python, Python, Python; Django, Django; SQL, SQL; Jane, Jane; ed, ed, ed; sue. So we're only going to insert
        # Python once, and then we're going to use the same Python over and over. Because even though there's vertical
        # replication in this data file, we're not going to have vertical replication in our person membership or course
        # tables. There's no vertical replication allowed. The world is full of vertical replication, good data models
        # are not. That's pretty to found actually.

        p, created = Person.objects.get_or_create(email=row[0])
        c, created = Course.objects.get_or_create(title=row[2])

        r = Membership.LEARNER
        if row[1] == 'I' : r = Membership.INSTRUCTOR
        m = Membership(role=r, person=p, course=c)
        m.save()