import os
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow, Everyone, Authenticated

class NewRoot(object):
    def __init__(self, request):
        self.request = request

    __acl__ = [
        (Allow, Everyone, "add")
    ]

def check_credentials(username, password):
    """return true if correct username and password, else false."""
    if username and password:
        #check credentials
        if username == os.environ["AUTH_USERNAME"]:
            if password  == os.environ["AUTH_PASSWORD"]:
                return True
        return False

def includeme(config):
    """"pyramid security configutation."""
    auth_secret = os.environ.get("AUTH_SECRET", "snake")
    authn_policy = AuthTktAuthenticationPolicy(
        secret=auth_secret,
        hashalg="sha512"
    )
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authentication_policy(authz_policy)
    # config.set_default_permission("view")
    config.set_root_factory(NewRoot)
