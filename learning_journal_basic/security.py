import os
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

def includeme(config):
    """"pyramid security configutation."""
    auth_secret = os.environ.get("AUTH_SECRET", "snake")
    authn_policy = AuthTktAuthenticationPolicy(
        secret=auth_secret,
        hashalg="sha512"
    )
    authz_policy =ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authentication_policy(authz_policy)
