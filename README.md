# Getting Started


Clone the project in your local computer
```
$ git clone https://github.com/GouravSardana/ft_django_rest.git
```

## Prerequisites



```
asgiref==3.2.7
Django==3.0.6
djangorestframework==3.11.0
gunicorn==20.0.4
pytz==2020.1
sqlparse==0.3.1
dj-static

```



## Installing and Running the project

```
$ cd ft_django_rest
```
```
$ pip install -r requirement.txt
```
After installing all the requirement. Run the following command.

```
$ python manage.py migrate
```

```
$ python manage.py runserver
```
you will see something like This
```
Performing system checks...

System check identified no issues (0 silenced).
June 07, 2018 - 11:12:23
Django version 1.11.13, using settings 'Project_SLS.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### API End Points

List all the users with their respective activity period.
```
https://ftlab-assessment.herokuapp.com/users
```


You can add more users and set their activities period by logging with admin.

username - gourav

password - 1234

```
https://ftlab-assessment.herokuapp.com/admin/
```

![OnPaste 20200527-161309](https://user-images.githubusercontent.com/31731827/83009843-0244de00-a035-11ea-94c4-730344ad7519.png)
