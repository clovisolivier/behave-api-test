# -- FILE:features/environment.py
def before_all(context):
    # -- SET LOG LEVEL: behave --logging-level=ERROR ...
    # on behave command-line or in "behave.ini".
    context.baseUrl = 'http://10.100.1.82:8082/api/v3/stats/'


def after_all(context):
    # -- SET LOG LEVEL: behave --logging-level=ERROR ...
    # on behave command-line or in "behave.ini".
    if hasattr(context,'response'):
        print("Response",context.response.text)
