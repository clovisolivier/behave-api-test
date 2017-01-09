# -- FILE:features/environment.py
def before_all(context):
    # -- SET LOG LEVEL: behave --logging-level=ERROR ...
    # on behave command-line or in "behave.ini".
    context.baseUrl = 'http://openweathermap.org/data/2.5/'