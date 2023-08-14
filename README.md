# **DjangoWebApp (WIP)**
Social Network with Authentication, System of Profiles, Posts and chats. Using Django and Sqlite3, as well as TDD techniques using Unit Tests and Functional Tests (with Selenium). At first, the application will adopt a "Server Side Rendering" method for the front-end.

## **Tools Used**
<h4>[Framework Web]</h4>

**Django** - Used to manage requests, urls, models, html templates and logic behind the site. It abstracts the process of creating and configuring an http web server.

<h4>[Database]</h4>

**Sqlite3** - Relational database used to store information about users and profiles. The choice of Sqlite3 was due to its usefulness for applications with lower volume of requests, making it ideal for academic projects (since it is an embedded database).

<h4>[Tests]</h4>

**Unittest** - Testing library built into Django. Used for unit tests. Similar to Java's JUnit. </br>
**Coverage** - Coverage is a tool for measuring code coverage in programs written in Python. Code coverage refers to the proportion of code that is executed while running automated tests. The main purpose of code coverage is to assess which parts of your code have been tested and which parts have not. Generating reports to assist in the creation of tests.

# **How to Run**

Install the project's dependencies, at the root of the project, run the command below to install the necessary libs to run the project:
```
pip install -r requirements.txt
```
It is important to point out that the ".sqlite3" file must be generated. Django uses a migrations system that tracks changes to the database which we call "migrations". To generate the embedded database file, you need to run the command below in the src folder:
```
python manage.py migrate
```
You can run the server using the command below, if successful, a message with the application's local ip will be displayed by django.
```
python manage.py runserver
```

# **Application Tests**
To run the application's tests, verify that the project's dependencies have already been installed. Tests for a particular app can be found under "app_name/tests/". Use any of the commands below to run the tests:
```
Pytest
```
```
python manage.py test
```
After adding new functionality, use the coverarge library to check code snippets not covered by the test libraries.
```
coverage run manage.py test
```
After running tests using coverage, you can generate reports to visualize code coverage. You can opt for a text report in the terminal:
```
coverage report
```
If you prefer a more detailed report, you can use the command below to generate an html. After generated, a folder called htmlcov will be generated at the root of your project. Open the "index.html" file and check the code snippets not reached by the test library.
```
coverage html
```

## **Login/Register Pages**
> Login Page
![Login page image](/docs/images/loginview.png)
> Register Page
![Register page image](/docs/images/registerview.png)
