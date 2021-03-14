## Architecture
1. architecture of GraphQL to understand how GraphQL is used in an HTTP client, especially in a web/mobile app.    
1. The client makes a request to the GraphQL server. This request is called a query. When a client requests a query to    
communicate with the server, the transport layer of GraphQL can be connected with any available network protocol such as   
 TCP, WebSocket, or any other transport layer protocol.   
1. The GraphQL server doesn't care about the database you use. It is neutral to databases. You can use a relational or a NoSQL database.   

## Client-Server flow in GraphQL
1. The GraphQL query is not written in JSON. When a client makes a 'POST' request to send a GraphQL query to the server,   
 this query is sent as a string.
1. The server receives and extracts the query string. After that, the server processes and validates the GraphQL query    
according to the GraphQL syntax and the graph data model (GraphQL schema).   
1. After that, the server takes the data and returns it to the client in a JSON object.  

## How to build a GraphQL server?
* There are three common architectural models for a GraphQL server.
1. GraphQL server with a connected database  
1. GraphQL server integrated with the existing system.  
1. A hybrid approach with a connected database and integration of the existing system  

## GraphQL Server with a Connected Database
1. This architecture setup is mostly used for new projects. In this architecture setup, the GraphQL server is integrated   
with the database. When the client sends a query, the server reads the requested query and fetches data from the database.   
This process is known as resolving the query. After resolving the query, the response is returned to the client in the    
official GraphQL specification format.  
![](https://static.javatpoint.com/tutorial/graphql/images/graphql-architecture.png)   

## GraphQL Server integrated with the Existing System.
1. This architecture model is used for companies having complicated projects which have legacy infrastructure and many    
different APIs. In this architecture model, GraphQL can be used to merge microservices, legacy infrastructure, and         
third-party APIs in the existing system and hide the complexity of data fetching logic. The server doesn't care about    
the database you use. It may be a relational or a NoSQL database.   
![](https://static.javatpoint.com/tutorial/graphql/images/graphql-architecture2.png)   

## A Hybrid approach with a Connected Database and Integrated Systems
1. This architecture model is a combination of the above two approaches: the GraphQL server with a connected database    
and the GraphQL server integrated with the existing system. In this architecture model, when a query is received by the   
server, the server resolves the received query and retrieves data either from the connected database or from the integrated API's.  
![](https://static.javatpoint.com/tutorial/graphql/images/graphql-architecture3.png)   
