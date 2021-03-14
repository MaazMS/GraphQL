## REST vs Graphql  
1. As they are both specifications for building and consuming APIs, GraphQL and REST have things in common.   
1. They both retrieve resources by sending queries, can return JSON data in the request, and be operated over HTTP.  
 1. Also, REST endpoints are similar to GraphQL fields, as they are entry points into the data that call functions on the server.   
 
| description | Graphql | REST  
|---|---|---|  
|Architecture | client-driven | serve-driven  
|organized in term of | schema & type system | endpoints  
|Operation | Query, Mutation, Subscription | Create, Read, Update, Delete  
|Data fetching | specific data with a single api call | fixed data with multiple api call  
|Community | growing | Large  
|performance | fast | multiple network calls take up more time  
|Development speed | rapid | slower  
|file uploading | No | Yes  
stability | less error prone, automatic validation and type checking| better choice for complex queries   
usecase | multiple microservices,mobile apps |simple apps, resource driven apps|   

## GraphQL vs REST: an example  
Let's say you have an API to fetch a user's p`rofile` and their `address`.    
In a typical REST scenario, this is what the request/response would look like:   
![](https://graphql-engine-cdn.hasura.io/learn-hasura/assets/graphql-react/rest-api.png)   
The core of REST API revolves around resources. Resources are identified by URLs and request type (GET, POST etc.).   
If your API server was a GraphQL server instead, this is what your API calls would look like:     
 
![](https://graphql-engine-cdn.hasura.io/learn-hasura/assets/graphql-react/graphql-api.gif)  
You can see that the response JSON is different for different "queries" sent by the client.  
````   
Request1:         |  Response1:
query {           |  {
  user (id: 1) {  |    "user": {
    id            |       "id": 1
  }               |     }
}                 |  }
----------------------------------------
Request2:         |   Response2:
query {           |   {
  user (id: 1) {  |     "user": {
    id            |       "id": 1
    name          |       "name": "Elmo"
  }               |     }
}                 |   }
````    
