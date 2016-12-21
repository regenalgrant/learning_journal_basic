import os
import io

from pyramid.response import Response

THIS_DIR =os.path.dirname(__file__)

def list_view(request):
    file_path = os.path.join(THIS_DIR, "templates", "index.html")
    file_data = io.open(file_path).read()
    return Response(file_data)


def detail_view(request):
    file_path = os.path.join(THIS_DIR, "data", "lj11.html")
    file_data = io.open(file_path).read()
    return Response(file_data)


def create_view(request):
    file_path = os.path.join(THIS_DIR, "templates", "create.html")
    file_data = io.open(file_path).read()
    return Response(file_data)


def update_view(request):
    file_path = os.path.join(THIS_DIR, "templates", "output.html")
    file_data = io.open(file_path).read()
    return Response(file_data)

def includeme(config):
    config.add_view(list_view,route_name="list")
    config.add_view(detail_view,route_name="detail")
    config.add_view(create_view,route_name="create")
    config.add_view(update_view,route_name="update")