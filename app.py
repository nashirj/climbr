import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

test_config = None

# def create_app(test_config=None):
    # create and configure the app

## create the Flask instance
### __name__ allows setting up paths
### instance_relative_config tells app that config files are
### relative to the instance folder (which is located outside
### of the flaskr package). the instance folder holds local data
### that shouldn't be commited to VCS, like DB and config secrets
app = Flask(__name__, instance_relative_config=True)

app.config.from_object(os.environ['APP_SETTINGS'])

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ## set some default configuration that the app will use
# ### SECRET_KEY is used to keep data safe. should be overridden
# ### with some random value when deploying, set to 'dev' for
# ### convenience
# ### DATABASE is path where SQLite db file will be saved 
# app.config.from_mapping(
#     SECRET_KEY='dev',
#     DATABASE=os.path.join(app.instance_path, 'climbr.sqlite'),
# )

# if test_config is None:
#     # load the instance config, if it exists, when not testing
#     app.config.from_pyfile('config.py', silent=True)
# else:
#     # load the test config if passed in
#     app.config.from_mapping(test_config)


# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass


# a simple page that says hello
@app.route('/hello')
def hello():
    return f'Hello, World!'

from climbr.models.user import User
from climbr.models.post import Post


from climbr import auth
app.register_blueprint(auth.bp)


from climbr import blog
app.register_blueprint(blog.bp)
app.add_url_rule('/', endpoint='index')


# allows printing debug statements from the jinja template
# usage: {{ mdebug("any text or variable") }}
@app.context_processor
def utility_functions():
    def print_in_console(message):
        print(str(message))

    return dict(mdebug=print_in_console)

# return app

# app = create_app()

if __name__ == '__main__':
    app.run()