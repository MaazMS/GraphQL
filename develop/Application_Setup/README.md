# Application Setup  
## Virtual Environments  
1. It's considered best practice to create virtual environments for Django projects.   
1. Using the terminal, enter your workspace and create the following folder:  
`$ mkdir django_graphql_projects`   
* Now create the virtual environment:  
````   
$ virtualenv --python=python3.6 env1
created virtual environment CPython3.6.13.final.0-64 in 5404ms
  creator CPython3Posix(dest=/home/maaz/github/GraphQL/django_graphql_movies/env1, clear=False, global=False)
  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=/home/maaz/.local/share/virtualenv/seed-app-data/v1.0.1)
  activators PythonActivator,FishActivator,XonshActivator,CShellActivator,PowerShellActivator,BashActivator
````  
1. You should see a new env folder in your directory. We need to activate our virtual environment, so that when we      
install Python packages they would only be available for this project and not the entire system:   
1. To activate virtual environment outside of env1 folder.   
`$ source env1/bin/activate`   
Note: To leave the virtual environment and use your regular shell, type deactivate.     

## Installing and Configuring Django    
1. Install Django with version 2.1.3   
`$ pip install Django==2.1.3`     
```   
Collecting Django==2.1.3
  Using cached Django-2.1.3-py3-none-any.whl (7.3 MB)
Collecting pytz
  Downloading pytz-2021.1-py2.py3-none-any.whl (510 kB)
     |████████████████████████████████| 510 kB 2.3 MB/s 
Installing collected packages: pytz, Django
Successfully installed Django-2.1.3 pytz-2021.1
```
## Installing and configuration graphene-django  
1. Install graphene for django  
`pip install "graphene-django>=2.0"`   
```    
Collecting graphene-django>=2.0
  Downloading graphene_django-2.15.0-py2.py3-none-any.whl (83 kB)
     |████████████████████████████████| 83 kB 111 kB/s 
Collecting promise>=2.1
  Using cached promise-2.3.tar.gz (19 kB)
Collecting six>=1.10.0
  Using cached six-1.15.0-py2.py3-none-any.whl (10 kB)
Requirement already satisfied: Django>=1.11 in ./env1/lib/python3.6/site-packages (from graphene-django>=2.0) (2.1.3)
Collecting singledispatch>=3.4.0.3
  Downloading singledispatch-3.6.1-py2.py3-none-any.whl (9.5 kB)
Collecting graphql-core<3,>=2.1.0
  Using cached graphql_core-2.3.2-py2.py3-none-any.whl (252 kB)
Collecting graphene<3,>=2.1.7
  Using cached graphene-2.1.8-py2.py3-none-any.whl (107 kB)
Collecting text-unidecode
  Downloading text_unidecode-1.3-py2.py3-none-any.whl (78 kB)
     |████████████████████████████████| 78 kB 524 kB/s 
Requirement already satisfied: pytz in ./env1/lib/python3.6/site-packages (from Django>=1.11->graphene-django>=2.0) (2021.1)
Collecting rx<2,>=1.6
  Using cached Rx-1.6.1-py2.py3-none-any.whl (179 kB)
Collecting graphql-relay<3,>=2
  Using cached graphql_relay-2.0.1-py3-none-any.whl (20 kB)
Collecting aniso8601<=7,>=3
  Using cached aniso8601-7.0.0-py2.py3-none-any.whl (42 kB)
Building wheels for collected packages: promise
  Building wheel for promise (setup.py) ... done
  Created wheel for promise: filename=promise-2.3-py3-none-any.whl size=21495 sha256=f2893c632bd6b3e25996306d258be42e2b0b822070f5688df8f69cc2bef6e7a4
  Stored in directory: /home/maaz/.cache/pip/wheels/59/9a/1d/3f1afbbb5122d0410547bf9eb50955f4a7a98e53a6d8b99bd1
Successfully built promise
Installing collected packages: six, promise, singledispatch, rx, graphql-core, graphql-relay, aniso8601, graphene, text-unidecode, graphene-django
Successfully installed aniso8601-7.0.0 graphene-2.1.8 graphene-django-2.15.0 graphql-core-2.3.2 graphql-relay-2.0.1 promise-2.3 rx-1.6.1 singledispatch-3.6.1 six-1.15.0 text-unidecode-1.3
```   
