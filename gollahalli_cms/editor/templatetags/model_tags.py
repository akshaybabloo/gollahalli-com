from django import template
from django.template import NodeList

from gollahalli_cms.editor.models import ContentModel

register = template.Library()


@register.tag(name='contentmodelexist')
def check_model_exists(parser, token):
    """
    Checks if any data available in ContentModel.

    ... {% contentmodelexist ContentModel %}
    ...     .....
    ... {% endcontentmodelexist %}

    Returns
    -------
    bool: bool
        True or False.
    """

    nodelist = parser.parse(('endcontentmodelexist',))
    full_node = [(token.split_contents()[1], nodelist)]
    parser.delete_first_token()

    return ModelDataExistNode(full_node)


class ModelDataExistNode(template.Node):
    """
    Check if the ``ContentModel`` has data, if ``True`` the context is rendered else empty string is returned.
    """

    def __init__(self, nodelist):
        self.list_nodelist = nodelist

    def __iter__(self):
        for _, nodelist in self.nodelist:
            yield from nodelist

    @property
    def nodelist(self):
        return NodeList(node for _, nodelist in self.list_nodelist for node in nodelist)

    def render(self, context):
        output = ''
        for content, nodelist in self.list_nodelist:
            if content is not None and content == 'ContentModel':
                try:
                    ContentModel.objects.get(ref_id=1)
                    output = self.nodelist.render(context)
                except ContentModel.DoesNotExist:
                    output = ''
            else:
                output = ''

        return output
