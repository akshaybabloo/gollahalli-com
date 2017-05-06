from editor import schema

import graphene


class Query(schema.Query, graphene.ObjectType):
    """
    GraphQL query class.
    """
    pass

query = graphene.Schema(query=Query)
