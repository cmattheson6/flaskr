import os
import sys

# get current working directory
cwd = os.path.abspath(os.path.dirname(__file__))
# isolate the last folder
project = os.path.basename(cwd)
# remove the last folder from cwd
new_path = cwd.strip(project)
# create a new path to point to where our Flask object is defined
full_path = os.path.join(new_path, 'flaskr')


try:
    from flaskr.flaskr import app
except ImportError:
    sys.path.append(full_path)
    from flaskr.flaskr import app


def before_feature(context, feature):
    context.client = app.test_client()
