# MS RBC DETECTION AI DASHBOARD

This repository contains both the back-end and front-end of the MS RBC Detection AI Dashboard.
Don't forget to run 

1. `cd client` to go to client folder.
2. `npm install` from within the /client folder.
3. `npm run serve` to start the frontend on local server.
4. open new terminal.
5. `cd api` to go to api folder.


## Setup backend

#### Create a virtual env
> ##### For MacOSX:
> ```console
> foo@bar:~$ virtualenv -p python3 .venv
> ```

##### For windows:
> ```
> foo@bar:~$ python -m venv .venv
> ```

##### For Unix/POSIX/Linux:
> ```
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
