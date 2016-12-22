"""Views page for learning_journal_basics."""
from pyramid.view import view_config
import os
import io

THIS_DIR = os.path.dirname(__file__)

ENTRIES = [
    {"title": "First Entry", "creation_date": "Dec 18, 2016", "id": 0, "body": "This is a fake learning journal thay I did not write but I wanted to have at least three examples in the entries list.."},
    {"title": "LJ - Day 11", "creation_date": "Dec 19, 2016", "id": 1, "body": "Today is class we started learning about pyramid and how to build an app using this framework. We are also continuing on in our data structures assignment and I have changed to be partners with Marc K. This was interesting in working on our deque for the day since we started with his data-structure repo so I had to learn a bit about how they named and formated their doubly linked list. There is also a difference in how we approach the testing. This should be a good learning experience as we continue to work together."},
    {"title": "LJ - Day 12", "creation_date": "Dec 20, 2016", "id": 2, "body": "Well there was a ton of stuff covered in class today and none of it is crazy but Im definitly not retaining all of it.  Still way too much of a workload in this class and I am starting to get way to pissed off at anything and everything.  I left early after struggling through the binary heap with Marc.  I stressed my way all the way to the bus and even yelled at a lady for blatantly littering on the ground.  I went to my parents place where I was able to see my nephew who is two years old and lives in South Carolina.  He is so close to spitting out full on sentances and it was amazing to get to feel joy for the first time in a few weeks.  I also got to see my younger brother and his wife which was amazing and I truely miss them since they live on the other side of the country.  After spending a little while with my family I returned to the misery that is this worhtless pile of assignments that is apparently not actually meant to be accomplished each day.  This place is just a game and seems like a waste of my time more often than not now.  So all in all today I learned that my family will always be more important than some class and I also learned that I can still feel terrible for screwing over my partner and leaving early "},

]


@view_config(route_name='list', renderer='templates/list.jinja2')
def list_view(request):
    """List_view view to supply entries before database."""
    return {"entries": ENTRIES}


@view_config(route_name="detail", renderer="templates/detail.jinja2")
def detail_view(request):
    """View for individual post."""
    entry = int(request.matchdict['id'])
    return {"entry": ENTRIES[entry]}


@view_config(route_name="create", renderer="string")
def create_view(request):
    """View for creating a new post."""
    file_path = os.path.join(THIS_DIR, "templates", "newpost.html")
    file_data = io.open(file_path).read()
    return file_data


@view_config(route_name="update", renderer="string")
def update_view(request):
    """View for updating a existing post."""
    file_path = os.path.join(THIS_DIR, "templates", "editpost.html")
    file_data = io.open(file_path).read()
    return file_data