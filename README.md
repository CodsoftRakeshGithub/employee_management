1)Employee Management Django App

2)open command prompt 
 
3)run cod:
        pip install Django mysql-connector-python
        pip install mysqlclient(it transfer the data from django to mysql and store the data its very important to data imporatation while bulding wheel )
        
4)if your using virtualenv activate that and then:
        django-admin startproject employee_management
        cd employee_management
        python manage.py startapp employees
        python manage.py startapp  staticfiles
        open visual studio or any (code .) simply from command prompt to visual studio 
5)open employee_management/settings.py:
           database 
          'ENGINE': 'django.db.backends.mysql',
        'NAME': 'employee_management',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306'
 6)creating the functions with (add,remove ,view,delete )and connecting them with urls path and 
                     creating only html 
 7)run code in commandprompt:
                     python manage.py makemigartions 
                     python manage.py  migarte
                     python manage.py runserver
 8)These are  the following URLs:
            Add Employee: http://localhost:8000/employees/add/
            Remove Employee: http://localhost:8000/employees/remove/
            View Employee: http://localhost:8000/employees/view/
            List Employees: http://localhost:8000/employees/list/
 9)*adding:
           it will add the employee into the database
    remove:
           it will remove the employee
     veiw:
           it will view the employees
      list:
           it will list the employes present the database
  10) everthing will be automtically doing in the database also(actually im connected with mysql)datbase
           
    
                     
 
 
 
        



        
