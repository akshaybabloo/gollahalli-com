import graphene

from gollahalli_cms.editor import schema


class Query(schema.Query, graphene.ObjectType):
    """
    GraphQL query class.
    """
    pass


query = graphene.Schema(query=Query)
