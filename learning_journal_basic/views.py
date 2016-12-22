"""Views page for learning_journal_basics."""
from pyramid.view import view_config
import os
import io

THIS_DIR = os.path.dirname(__file__)

ENTRIES = [
    {"title": "First Entry", "creation_date": "Dec 18, 2016", "id": 0, "body": "blah."},
    {"title": "LJ - Day 11", "creation_date": "Dec 19, 2016", "id": 1, "body": "blah."},
    {"title": "LJ - Day 12", "creation_date": "Dec 20, 2016", "id": 2, "body": "blah"},

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