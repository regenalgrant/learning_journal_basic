
"""All the routes for the configuration to find."""


def includeme(config):
    """All the routes for the configuration to find."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route("index", "/")
    config.add_route("detail", "/journal/{id:\d+}")
    config.add_route("form", "/journal/new-entry")
    config.add_route("edit-form", "/journal/{id:\d+}/edit-entry")