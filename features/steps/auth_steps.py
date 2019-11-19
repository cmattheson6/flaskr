from behave import *

@given(u'Flaskr is set up')
def flask_is_set_up(context):
    assert context.client