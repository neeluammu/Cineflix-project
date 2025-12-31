from django import template

register = template.Library()

@register.simple_tag
def allowed_roles(request, roles):
    if not request.user.is_authenticated:
        return False

    import json
    roles = json.loads(roles)

    return request.user.role in roles
