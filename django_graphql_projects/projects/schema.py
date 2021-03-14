import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from django_graphql_projects.projects.models import (
    Developer,
    Project,
)

# Create graphql type for the developer type
class DeveloperType(DjangoObjectType):
    class Meta:
        model = Developer


# create graphql type for the Project type
class ProjectType(DjangoObjectType):
    class Meta:
        model = Project


# craete query type
class Query(ObjectType):
    developer = graphene.Field(DeveloperType, id=graphene.Int())
    project = graphene.Field(ProjectType, id=graphene.Int())
    developers = graphene.List(DeveloperType) # List use a type modifier, which indicates that this field will return a list.
    projects = graphene.List(ProjectType)

    def resolve_developer(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return Developer.objects.get(pk=id)
        return None

    def resolve_project(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return Project.objects.get(pk=id)

        return None

    def resolve_developers(self, info, **kwargs):
        return Developer.objects.all()

    def resolve_projects(self, info, **kwargs):
        return Project.objects.all()


# create input object types for developer
class DeveloperInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


# create input object types for project
class ProjectInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    developers = graphene.List(DeveloperInput)
    year = graphene.Int()

# create mutation for developers
class CreateDeveloper(graphene.Mutation):
    class Arguments:
        input = DeveloperInput(required=True)

    # developer and ok are the output fields of the Mutation when it is resolved.
    ok = graphene.Boolean()
    developer = graphene.Field(DeveloperType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        developer_instance = Developer(name=input.name)
        developer_instance.save()
        return CreateDeveloper(ok=ok, developer=developer_instance)


# update mutation for developer
class UpdateDeveloper(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = DeveloperInput(required=True)

    # developer and ok are the output fields of the Mutation when it is resolved.
    ok = graphene.Boolean()
    developer = graphene.Field(DeveloperType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        developer_instance = Developer.objects.get(pk=id)

        if developer_instance:
            ok = True
            developer_instance.name = input.name
            developer_instance.save()
            return UpdateDeveloper(ok=ok, developer=developer_instance)
        return UpdateDeveloper(ok=ok, developer=None)


# create mutation for project
class CreateProject(graphene.Mutation):
    class Arguments:
        input = ProjectInput(required=True)

    ok = graphene.Boolean()
    project = graphene.Field(ProjectType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        developers = []

        for developer_input in input.developers:
            developer = Developer.objects.get(pk=developer_input.id)
            if developer is None:
                return CreateProject(ok=False, Project=None)
            developers.append(developer)

        project_instance = Project(title=input.title, year=input.year)
        project_instance.save()
        project_instance.developers.set(developers)
        return CreateProject(ok=ok, project=project_instance)


# update mutation for project
class UpdateProject(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ProjectInput(required=True)

    ok = graphene.Boolean()
    project = graphene.Field(ProjectType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        project_instance = Project.objects.get(pk=id)
        if project_instance:
            ok = True
            developers = []
            for developer_input in input.developers:
                developer = Developer.objects.get(pk=developer_input.id)
                if developer is None:
                    return UpdateDeveloper(ok=False, project=None)
                developers.append(developer)
            project_instance.title = input.title
            project_instance.year = input.year
            project_instance.save()
            project_instance.developers.set(developers)
            return UpdateProject(ok=ok, project=project_instance)
        return UpdateProject(ok=ok, project=None)

# delete mutation for developer
class DeleteDeveloper(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        developer_instance = Developer.objects.get(pk=id)
        if developer_instance:
            ok = True
            developer_instance.delete()
            return DeleteDeveloper(ok=ok)

# delete mutation for project
class DeleteProject(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        project_instance = Project.objects.get(pk=id)
        if project_instance:
            ok = True
            project_instance.delete()
            return DeleteProject(ok=ok)


# create the Mutation type
class Mutation(graphene.ObjectType):
    create_developer = CreateDeveloper.Field()
    update_developer = UpdateDeveloper.Field()
    create_project = CreateProject.Field()
    update_project = UpdateProject.Field()
    delete_developer = DeleteDeveloper.Field()
    delete_project = DeleteProject.Field()


# Making the Schema to map the queries and mutations to our application's API.
schema = graphene.Schema(query=Query, mutation=Mutation)