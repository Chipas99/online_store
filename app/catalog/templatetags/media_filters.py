from django import template

register = template.Library()


@register.simple_tag
def mediapath(obj):
    return obj.preview.url if obj.preview else '/default/path/to/image.jpg'
