# MS RBC DETECTION AI DASHBOARD

This repository contains both the back-end and front-end of the MS RBC Detection AI Dashboard.

## Setup forntend

#### Go to client folder
> ```console
> foo@bar:~$ cd client
> ```

#### Install packages
> ```console
> foo@bar:~$ npm install
> ```

#### Start local server
> ```console
> foo@bar:~$ npm run serve
> ```

## Setup backend
#### Go to api folder
> ```console
> foo@bar:~$ cd api
> ```

#### Create a virtual env
> ##### For MacOSX:
> ```console
> foo@bar:~$ python3.9 -m venv .venv
> ```

##### For windows:
> ```console
> foo@bar:~$ python -m venv .venv
> ```

##### For Unix/POSIX/Linux:
> ```console
> foo@bar:~$ python3.9 -m virtualenv .venv
> ```

#### Activate virtual environment in python.<br>
> ##### For windows:
> ```console
> foo@bar:~$ .venv\Scripts\activate
> ```

> ##### For Unix/POSIX/Linux:
> ```console
> foo@bar:~$ source .venv/bin/activate
> ```

#### Install requirements
> ```console
> foo@bar:~$ pip install -r requirements.txt
> ```
> or:
> ```console
> foo@bar:~$ python -m pip install -r requirements.txt
> ```


#### Set Flask ENV
> ##### For windows:
> ```console
> foo@bar:~$ set FLASK_APP=manage.py
> ```

> ##### For Unix/POSIX/Linux:<br>
> ```console
> foo@bar:~$ export FLASK_APP=manage.py
> ```

## To run the backend
flask run <br>
```console
foo@bar:~$ python -m flask run
```
