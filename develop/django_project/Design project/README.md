### Object types and fields   
1. The most basic components of a GraphQL schema are object types, which just represent a kind of object you can fetch    
from your service, and what fields it has.   
1.`Types` describe the kind of data that's available in the API.  
example  
```   
type Developer {
  id: ID!
  name: String!
}

type Project {
  id: ID!
  title: String!
  developer: [Developer]
  year: Int!
}
```  
Note: id, title, developer, year are field on type.       
Note : This step in django   
    1. define in model in model.py under projects folder.    
    1. define type as class in schema.py under projects folder.    

## Creating Queries
1. A query specifies what data can be retrieved from server.   
example  
```  
type Query {
  developer(id: ID!): Developer
  project(id: ID!): Project
  developer: [Developer]
  project: [Project]
}
```  
Note : This step in django   
    1. define type Query as class in schema.py under projects folder.  
    1. Query class is inherit ObjectType.  
    1. Query class methods are resolver to fetching data from server.     

## Mutations
1. A mutation describes what operations can be done to change data on the server.
1. `Inputs`   - special types only used as arguments in a mutation when we want to pass an entire object instead of individual fields.  
example  
```  
input DeveloperInput {
  id: ID
  name: String!
}

input ProjectInput {
  id: ID
  title: String
  developers: [DeveloperInput]
  year: Int
}
```  
Note : This step in django   
    1. define input DeveloperInput as class in schema.py under projects folder.  
    1. DeveloperInput class is inherit graphene.InputObjectType.  
    1. ProjectInput class is inherit graphene.InputObjectType.  
    1. DeveloperInput class fields are id and name.  
    1. ProjectInput class fields are id, title,year and developers which is map to class DeveloperInput.    
    
## Creating Mutations   
1. create Developer
````   
mutation createDeveloper {
  createDeveloper(input: {
    name: "Maaz Shaikh"
  }) {
    ok
    developer {
      id
      name
    }
  }
}
````  

1. create Project
````  
mutation createProject {
  createProject(input: {
    title: "Shaikh"
    developers : [
      {
        id: 3
      }
    ],
    year: 2021
    
  	}) {
    ok
    project {
      id
      title
      developers {
        id
        name
      }
      year
    }
  }
} 
````      
Note : This step in django similar to developer and project.   
    1. define mutation CreateDeveloper as class in schema.py under projects folder.  
    1. CreateDeveloper class is inherit graphene.Mutation.  
    1. class Arguments under CreateDeveloper class is the argument for mutation i.e input field.    
    1. developer and ok are the output fields of the Mutation when it is resolved.  
    1. mutate is the function that will be applied once the mutation is called.    
    1. mutate @staticmethod can be used when the code that belongs to a class doesn't use the object itself at all.    
    1. developer_instance variable take input from `Developer` class.   
    1. developer_instance.save() is use Save the current instance.  
    1. return CreateDeveloper(ok=ok, developer=developer_instance)   
## update Mutations  
1. Update Project
````   
mutation UpdateProject {
  updateProject(id: 3, input: {
    title: "django", 
    developers: [
        {
            id: 1
        }
    ], 
    year: 2021
    }) {
    ok
    project {
      id
      title
      developers {
        id
        name
      }
      year
    }
  }
}

````   
1. Update developer  
````  
mutation UpdateDeveloper{
    updateDeveloper(id:3, input:{
    name : "Maazil Shaikh"
     }){
    ok
    developer {
        id
        name
    }
  }    
}
````         
Note : This step in django similar to developer and project.   
    1. define mutation UpdateDeveloper as class in schema.py under projects folder.  
    1. UpdateDeveloper class is inherit graphene.Mutation.  
    1. class Arguments under UpdateDeveloper class is the argument for mutation i.e input and id fields.    
    1. developer and ok are the output fields of the Mutation when it is resolved.  
    1. mutate is the function that will be applied once the mutation is called.    
    1. mutate @staticmethod can be used when the code that belongs to a class doesn't use the object itself at all.     
    1. be careful `id` as argument use to update the specific values in database.      
    1. developer_instance.name = input.name update name of developer and name is the field of class Developer.   
    1. developer_instance.save() is use Save the current instance.  
    1. if developer is update return UpdateDeveloper(ok=ok, developer=developer_instance)    
    1. if developer is not update return UpdateDeveloper(ok=ok, developer=None)  
## Delete Mutations      
1. Delete Developer
```   
mutation DeleteDeveloper{
    deleteDeveloper(id : 1){
    ok 
    }
}
``` 
1. Delete Project
```   
mutation DeleteProject{
    deleteProject(id : 2){
    ok 
    }
}
``` 
Note : This step in django similar to developer and project.   
    1. define mutation DeleteDeveloper as class in schema.py under projects folder.  
    1. DeleteDeveloper class is inherit graphene.Mutation.  
    1. class Arguments under UpdateDeveloper class is the argument for mutation i.e id field.    
    1. ok is the output field of the Mutation when it is resolved.  
    1. mutate is the function that will be applied once the mutation is called.    
    1. mutate @staticmethod can be used when the code that belongs to a class doesn't use the object itself at all.     
    1. be careful `id` as argument use to delete the specific values in database.      
    1. developer_instance.delete() is use delete the current instance.  
    1. if developer is delete return DeleteDeveloper(ok=ok)    
    
1. The Mutation type brings it all together:  
```  
type Mutation {
  createdeveloper(input: DeveloperInput) 
  createproject(input: ProjectInput) 
  updatedeveloper(id: ID!, input: DeveloperInput) 
  updateproject(id: ID!, input: ProjectInput) 
  deleteDeveloper(id: ID!) 
  deleteProject(id: ID!) 

}
```  
Note : This step in django similar to developer and project.   
    1. define mutation as class in schema.py under projects folder.  
    1. Mutation class is inherit graphene.ObjectType.  
    1. In this Mutation class the server will receive CreateDeveloper, UpdateDeveloper, CreateProject, UpdateProject,  
    DeleteDeveloper, DeleteProject field and returning CreateDeveloper, UpdateDeveloper, CreateProject, UpdateProject, 
    DeleteDeveloper, DeleteProject.    
## Defining the Schema
1. Finally, we map the queries and mutations we've created to the schema:
```   
schema {
  query: Query
  mutation: Mutation
}
```  
Note : This step in django for developer and project.   
    1. Making mutation in schema.py under projects folder.  
    1. Making the Schema to map the queries and mutations to our application's API.
    1. `schema = graphene.Schema(query=Query, mutation=Mutation)`