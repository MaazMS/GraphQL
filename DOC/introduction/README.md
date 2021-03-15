## Introduction of GraphQL       
  
1. Originally created by Facebook but now developed under the GraphQL Foundation.    
1. GraphQL is a query language and server-side runtime for application programming interfaces (APIs) that prioritizes    
giving clients exactly the data they request and no more.   
1. GraphQL is a query language for API and server runtime that allows us to retrieve and manipulate data.   
example :  sql for database same graphql for api. 
1. GraphQL isn't tied to any specific database or storage engine and is instead backed by your existing code and data.     
1. GraphQL does not dictate a specific application architecture.   
1. It can be introduced on top of an existing REST API and can work with existing API management tools.  

* application architecture :   
    An application architecture describes the patterns and techniques used to design and build an application.     
* API management tools:  
    API management refers to the processes for distributing, controlling, and analyzing the APIs that connect applications   
     and data across the enterprise and across clouds.     


##  GraphQL benefits
**Avoid over-fetching**: You avoid fetching more data than you need because you can specify the exact fields you need.    
**Prevent multiple API calls**: In case you need more data, you can also avoid making multiple calls to your API.   
you don't need to make 2 API calls to fetch user and address separately. single end point to fetch multiple field.    
**Less communication overhead with API developers**: Sometimes to fetch the exact data you need, especially if you need     
to fetch more data and want to avoid multiple API calls, you will need to ask your API developers to build a new API.     
 With GraphQL, your work is independent of the API team! This allows you to work faster on your app.   
**Data loading efficient** when use low network on small device i.e mobile data loading is efficient on mobile network.    

## Building block of graphql  
```         
Schema   |______________|     |______________|     |______________|                                          
         |    Type      | +   |    Queries   | +   |    Mutations |
         |              |     |    (fetch)   |     |    (Modify)  |
         |______________|     |______________|     |______________| 
        
                            |______________|
                            |    Resolver  | 
                            |    function  | 
                            |______________|
```     

1. Schema: It telling client these are all the data type associate with app server. 
These are all the queries 
1. Queries means the data is fetching from server using get method.  
1. Mutations changes to make database i.e create new record, update record, delete record using post,patch,delete method.   
1. Resolver implementation of api.    
1. why use `resolvers` ?   
A Resolver is a method that helps us answer Queries by fetching data for a Field in our Schema.     

## Schema      
Define types,queries, mutation and map them to define schema,   
example   
```   
schema {
    query :Query
    mutation : Mutation
}
```
## define Schema   
1. Define object type  
1. Define query type  
1. Define Mutation type   