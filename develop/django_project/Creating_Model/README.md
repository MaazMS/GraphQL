## Creating a Model  
1. Django models describe the layout of our project's database.   
1. Each model is a Python class that's usually mapped to a database table.   
1. The class properties are mapped to the database's columns.   

## our project model
1. Developer model has field is name.  
1. Project model has title, developer and year.  
1. As with the GraphQL schema, the Developer model has a name whereas the Project model has a title, a many-to-many    
relationship with the actors and a year.   
1. The IDs are automatically generated for us by Django.    
1. many-to-many relationship, use ManyToManyField.   
 