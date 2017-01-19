def includeme(config):
    """All of the routes for the config to find."""
    config.add_static_view('static', 'learning_journal:static', cache_max_age=3600),
    config.add_route('list', '/')
    config.add_route('about', '/about')
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('create', '/journal/new-entry')
    config.add_route('update', '/journal/{id:\d+}/edit-entry')
    config.add_route('category', '/journal/category/{category:\w+}')
    config.add_route('notfound', '/journal/notfound')
    config.add_static_view('static', 'expense_tracker:static')
    config.add_route('edit', '/journal/{id:\d+}/edit')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('delete', '/delete/{id:\d+}') # <-- NEW ROUTE
    config.add_route('api_list', '/api/journal')