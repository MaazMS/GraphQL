## Testing Our API
http://127.0.0.1:8000/graphql/
To test our API, let's run the project and then go to the GraphQL endpoint. In the terminal type:  
## Writing Queries
1. get Developers
```  
query getDevelopers {
  developers {
    id
    name
  }
}
```   
1. get specific Developer
```  
query getDevelopers {
  developer (id : 1){
    id
    name
  }
}
```  
1. get Projects
```  
query getProjects {
  projects {
    id
    title 
    year
    developers{
      id
      name
    }
  }
}
```   
1. get specific Project
````  
query getProject {
  project(id: 1) {
    id
    title
    year
    developers {
      id
      name
    }
  }
}
````  

## create Mutations
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