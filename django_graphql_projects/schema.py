import graphene
import django_graphql_projects.projects.schema

class Query(django_graphql_projects.projects.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple queries
    # as we begin to add more apps to our project
    pass

class Mutation(django_graphql_projects.projects.schema.Mutation, graphene.ObjectType):
    # This class will inherit from multiple queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)