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

## Creating Mutations
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
1. The Mutation type brings it all together:  
```  
type Mutation {
  createdeveloper(input: DeveloperInput) 
  createproject(input: ProjectInput) 
  updatedeveloper(id: ID!, input: DeveloperInput) 
  updateproject(id: ID!, input: ProjectInput) 

}
```
## Defining the Schema
1. Finally, we map the queries and mutations we've created to the schema:
```   
schema {
  query: Query
  mutation: Mutation
}
```