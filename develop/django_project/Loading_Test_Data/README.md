## Loading Test Data  
1. After we build our API, we'll want to be able to perform queries to test if it works.    
1. Let's load some data into our database, save the following JSON as projects.json in your project's root directory.  
example  
```   
[
  {
    "model" : "projects.developer",
    "pk" : 1,
    "fields" :{
      "name":  "Maaz Shaikh"
    }
  },
  {
    "model" : "projects.developer",
    "pk" : 2,
    "fields": {
      "name" : "Arif Shaikh"
    }
  },
  {
    "model" : "projects.project",
    "pk" : 1,
    "fields" : {
      "title" : "graphql",
      "developers" : [1,2],
      "year" : "2021"
    }
  }
]
``` 
`$ python manage.py loaddata projects.json `
**Installed 3 object(s) from 1 fixture(s)**   
`