In this documentation flask project structure will be generated. Flask is a python based microframework with very good documentation which you can find [here](https://flask.palletsprojects.com/en/2.0.x/). At time of writing Flask version 2.0.2 and Python version 3.10.1 was used.

This repository will contain backend for bellik app, which will not have generated views and any static content. It will expose public API, which will be used by web and mobile apps.

## Virtual Environment

It is a _de facto_ to use virtual environment during development. If you are not familiar with virtual environments, please read [Virtual environments](https://flask.palletsprojects.com/en/2.0.x/installation/#virtual-environments) section in official Flask documentation.

Note that, if you use `fish` as your shell, command to activate virtual environment is as below:

```
. venv/bin/activate.fish
```

If you user bash, command to activate virtual environment is as below:

```
source venv/bin/activate
```

You should not commit your virtual environment directory becuase it contains to much local files which just needed to run your code. All packages installed in virtual environment will be downloaded to this directory.

## Python setup script

Python projects should have `setup.py` which contains meta information about package and it's dependencies. It is very big topic, maybe in future you will need to tweak your `setup.py` you can read [github.com/kennethreitz/setup.py](https://github.com/kennethreitz/setup.py).

Initial `setup.py` code is below


```
from setuptools import setup, find_packages

setup(
	name='bellikd',
	description='Bellik Backend',
	version='0.1',
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	install_requires=['Flask'],
)
```

Since there will be no static content or generated content, there is no need for `static` and `templates` folders. For project which contains static files and html templates, there is a need for `MANIFEST.in` file, contents of which are below

```
recursive-include bellik/static *
recursive-include bellik/templates *
```

## Initial project structure

At the beginning of the project you will have file/directory structure similar to as below.

```
.
├── bellik
│   ├── static
│   └── templates
├── CONTRIBUTING.md
├── docs
├── tests
├── LICENSE
├── MANIFEST.in
├── README.md
└── setup.py

```

## Hello World

Let's add `bellik/__init__.py` file which will have code below.

```
import os

from flask import Flask

def create_app():
	app = Flask(__name__, instance_relative_config=True)

	@app.route('/')
	def root():
		return 'Hello Flask'

	@app.route('/hello')
	def hello():
		return 'Hello!'

	return app
```

Before running the app, please be sure that your virtual environment is active. Now you have to install the app to your virtual environment in development mode, so run `python setup.py develop`, this command will download dependencies and install your code as a package to your virtual environment as a development package. It means that if you change your code, all your changes will be available if you re-run the server.

There are final steps, we can use [flask command line interface](https://flask.palletsprojects.com/en/2.0.x/cli/) to run our development server. Run below commands if you are using `fish` as your shell.

```
set -x FLASK_APP 'bellik:create_app()'
set -x FLASK_ENV development
flask run
```

and below code if you use `bash`:

```
export FLASK_APP='bellik:create_app()'
export FLASK_ENV=development
flask run
```

You will see output something like below:

```
 * Serving Flask app 'bellik:create_app()' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 669-108-668
```

If you redirect your browser to address in output you will see `Hello Flask`, if you add navigate to `http://127.0.0.1:5000/hello` you will see `Hello!`.

From now on, you have your hello world app running. It is strongly advised by your self experiment with `bellik/__init__.py`.

