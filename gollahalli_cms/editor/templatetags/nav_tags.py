from django import template

register = template.Library()


@register.filter()
def has_string_in_path(path, has):
    """
    Checks if the path has the given string.

    Parameters
    ----------
    path: str
        Forward slash separated string.
    has: str
        String to check in path.

    Returns
    -------
    bool: bool
        True or False.
    """
    return bool(set(has.split(',')).intersection(path.split('/')))
