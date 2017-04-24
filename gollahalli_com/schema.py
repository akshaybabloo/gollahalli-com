from editor import schema

import graphene


class Query(schema.Query, graphene.ObjectType):
    pass

query = graphene.Schema(query=Query)
