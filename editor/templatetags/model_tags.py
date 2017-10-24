from django import template
from ..models import ContentModel

register = template.Library()


@register.filter()
def check_model_exists():
    """
    Checks if any data available in ContentModel.

    Returns
    -------
    bool: bool
        True or False.
    """

    try:
        ContentModel.objects.get(ref_id=1)
        return True
    except ContentModel.DoesNotExist:
        return False
