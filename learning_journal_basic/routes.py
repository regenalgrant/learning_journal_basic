
"""Routes for learning_journal_basic."""


def includeme(config):
    """All of the routes for the config to find."""
    config.add_static_view('static', 'learning_journal_basic:static', cache_max_age=3600),
    config.add_route('list', '/')
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('create', '/journal/new-entry')
    config.add_route('update', '/journal/{id:\d+}/edit-entry')