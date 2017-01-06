"""Default views for learning journal web app."""

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from sqlalchemy.exc import DBAPIError
from pyramid.view import notfound_view_config

from ..models import Entry
import datetime
from learnal_journal_basic.security import check_credentials
from pyramid.security import remember, forget

@view_config(route_name='list', renderer='templates/list.jinja2')
def list_view(request):
    """List_view view to supply entries before database."""
    try:
        entries = request.dbsession.query(Entry).order_by(Entry.creation_date.desc()).all()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {"entries": entries}


@view_config(route_name="detail", renderer="../templates/detail.jinja2")
def detail_view(request):
    """View for individual post."""
    query = request.dbsession.query(Entry)
    the_entry = query.filter(Entry.id == request.matchdict['id']).first()
    return {"entry": the_entry}


@view_config(route_name='create', renderer='../templates/create.jinja2')
def create_view(request):
    """View for creating a new post."""
    if request.method == "POST":
        new_title = request.POST["title"]
        new_body = request.POST["body"]
        new_date = datetime.datetime.now().date()
        new_category = request.POST["category"].title().replace(" ", "")
        new_tags = request.POST["tags"]
        new_entry = Entry(title=new_title, body=new_body, creation_date=new_date, category=new_category, tags=new_tags)

        request.dbsession.add(new_entry)

        return HTTPFound(location='/')
    return {}


@view_config(route_name="category", renderer="../templates/category.jinja2")
def category_view(request):
    """View for post of different categories."""
    query = request.dbsession.query(Entry)
    entries = query.filter(Entry.category == request.matchdict['category']).order_by(Entry.creation_date.desc()).all()
    return {"entries": entries}


@view_config(route_name="about", renderer="../templates/about.jinja2")
def about_view(request):
    """View for about me."""
    return {}

@view_config(route_name="login",
             renderer="../templates/login.jinja2",
             require_csrf=False)
def login_view(request):
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        if check_credentials(username, password):
            auth_head = remember(request, username)
            return HTTPFound(
                request.route_url("list"),
                headers=auth_head
            )

@view_config(route_name="logout")
def logout_view(request):
    auth_head = forget(request)
    return HTTPFound(request.route_url("list"), headers=auth_head)
    return {}

@forbidden_view_config(renderer="../templates/forbidden.jinja2")
def not_allowed_view(request):
    """Some special stuff for the forbidden view."""
    return {}


@view_config(route_name="delete", permission="delete")
def delete_view(request):
    """To delete individual items."""
    expense = request.dbsession.query(Expense).get(request.matchdict["id"])
    request.dbsession.delete(expense)
    return HTTPFound(request.route_url("list"))


@view_config(route_name="api_list", renderer="string")
def api_list_view(request):
    expenses = request.dbsession.query(Expense).all()
    output = [item.to_json() for item in expenses]
    return output

db_err_msg = """\
