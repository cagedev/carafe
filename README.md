Carafe
======

Flask (python) based server framework.

Implements (TODO):
 * login system
   * Google (OAuth2)
   * GitHub


Virtual Environment (venv)
--------------------------

https://realpython.com/python-virtual-environments-a-primer/

``python3 -m venv ./venv``
`source ./venv/bin/activate` (using source so `activate` script needs not to be executable)


Development Web Server
----------------------

Set the `FLASK_APP` enviranment variable
``(venv) $ export FLASK_APP=test_app.py``
(use `set` in stead of `export` on MSW)

Run the development server
``(venv) $ flask run``


Application structure
---------------------

|-{appname}
  |-app/
    __init__.py
    |-auth/ (Blueprint)
      __init__.py
      email.py
      forms.py
      routes.py
    |-errors/ (Blueprint)
    |-templates/
      {for all Blueprint}
      |-auth/
        login.html
        register.html
        reset_password_request.html
        reset_password.html
      |-errors/
    |-static/
    |-main/
      |-__init__.py
      |-errors.py
      |-forms.py
      |-views.py
    |-__init__.py
    |-email.py
    |-models.py
      User(db.Model)
  |-migrations/
  |-tests/
    |-__init__.py
    |-test*.py
      UserModelTestCase(unittest.TestCase)
  |-venv/
  |-requirements.txt
  |-config.py
    Config(object)
  |-{appname}.py
