from tree_menu.models import Menu
from django import template
from django.db.models import Q

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html')
def draw_menu(menu_name: str = None, menu_item: str = None):

    items = Menu.objects.filter(Q(name=menu_name) | Q(parent__name=menu_item))
    if menu_name == menu_item:
        return {'menu': items}
    else:

        return {'menu': items}
        