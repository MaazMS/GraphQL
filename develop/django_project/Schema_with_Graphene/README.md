## Creating our Schema with Graphene  
1. GraphQL is a strongly typed language.     
1. Type System defines various data types that can be used in a GraphQL application.    
1. The type system helps to define the schema, which is a contract between client and server.    
common used types are scalar,query,mutation. etc    

## ObjectType  
1. A Graphene ObjectType is the building block used to define the relationship between Fields in your Schema and how     
their data is retrieved.   
    * Each ObjectType is a Python class that inherits from `graphene.ObjectType`.  
    * Each attribute of the ObjectType represents a Field.  
    * Each Field has a resolver method to fetch data   
    
### Making Queries 
1. Every schema has a special type called query for getting data from the server. 
1. A Resolver is a method that helps us answer Queries by fetching data for a Field in our Schema.   
1. When we execute a query against that schema. `schema = Schema(query=Query)`  

### Making Mutation
1. A mutation describes what operations can be done to change data on the server.    
1. To use an `InputField` you define an InputObjectType that specifies the structure of your input data.  
1. developer and ok are the output fields of the Mutation when it is resolved.
```  
ok = graphene.Boolean()
developer = graphene.Field(DeveloperType)
```    
1. `Arguments` attributes are the arguments that the Mutation `CreateDeveloper` and `CreateProject` needs for resolving,  
 in this case `input` will be the only argument for the mutation.   
1. create and update mutation function is create for developer and project.  
1. create the Mutation type means mutation class for CreateDeveloper,UpdateDeveloper,CreateProject,UpdateProject.  

## Making the Schema
1. As before when we designed our schema, we map the queries and mutations to our application's API. 
`schema = graphene.Schema(query=Query, mutation=Mutation)`     

## Registering the Schema in the Project    
1. we need to make a schema available project wide.
````  
import django_graphql_projects.projects.schema  

class Query(django_graphql_projects.projects.schema.Query, graphene.ObjectType):
    pass

class Mutation(django_graphql_projects.projects.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation) 
````

## INSTALLED_APPS  
1. INSTALLED_APPS add schema.  
```  
GRAPHENE = {
    'SCHEMA': 'django_graphql_projects.schema.schema'
}
```

## register route
1. We need to register that route, or rather view, in Django.  
1. inside project url.py  
1. Creating GraphQL and GraphiQL views.  
1. Unlike a RESTful API, there is only a single URL from which GraphQL is accessed.   
1. Requests to this URL are handled by Graphene’s GraphQLView view.   
1. This view will serve as GraphQL endpoint.   

