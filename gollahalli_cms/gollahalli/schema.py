import graphene

from editor import schema


class Query(schema.Query, graphene.ObjectType):
    """
    GraphQL query class.
    """
    pass


query = graphene.Schema(query=Query)
