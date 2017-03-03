import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.debug import DjangoDebug


from .models import ContentModel


class ContentSchema(DjangoObjectType):
    class Meta:
        model = ContentModel


class Query(graphene.ObjectType):
    all_contents = graphene.List(ContentSchema)
    debug = graphene.Field(DjangoDebug, name='__debug')

    def resolve_all_contents(self, args, context, info):
        return ContentModel.objects.all()
