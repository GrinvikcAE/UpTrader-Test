from django.shortcuts import render
from .models import Menu


def index(request):
    return render(request, 'tree_menu/index.html', {'menus': Menu.objects.all()})


def draw_menu(request, path):
    split_path = path.split('/')
    return render(
        request, 'tree_menu/index.html', {'menu_name': split_path[0], 'menu_item': split_path[-1]})
