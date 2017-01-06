import pytest
from pyramid import testing


@pytest.fixture(scope="session")
def configuration(request):
   settings = {
        'sqlalchemy.url': 'sqlite:///:memory:'}  # points to an in-memory database.
    config = testing.setUp(settings=settings)
    config.include('.models')

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture
def req():
    """Dummy request."""
    the_request = testing.DummyRequest()
    return the_request


@pytest.fixture
def testapp():
    """Test app fixture."""
    from webtest import TestApp
    from learning_journal_basic import main
    app = main({})
    return TestApp(app)


def test_home_page_renders_home_page_stuff(req):
    """My home page view returns some data."""
    from .views import list_view
    response = list_view(req)
    assert "Most Recent Posts" in response

# not removed cause i know i need this
# def test_home_page_has_thing(testapp):
#     response = testapp.get("/", status=200)
#     html = response.html


def test_details_page_renders_details_page_stuff(req):
    """My home page view returns some data."""
    from .views import detail_view
    response = detail_view(req)
    assert "An individual Post" in response

    # ======== TESTING WITH SECURITY ==========


def test_create_route_is_forbidden(testapp):
    """Any old user shouldn't be able to access the create view."""
    response = testapp.get("/new-expense", status=403)
    assert response.status_code == 403


def test_auth_app_can_see_create_route(set_auth_credentials, testapp):
    """A logged-in user should be able to access the create view."""
    response = testapp.post("/login", params={
        "username": "testme",
        "password": "foobar"
    })
    response = testapp.get("/new-entry")
    assert response.status_code == 200
