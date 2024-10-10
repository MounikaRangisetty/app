from behave import given, when, then
import requests

BASE_URL = 'http://43.203.121.184:4001'

@given('the application is running')
def step_impl(context):
    pass  # Assumes the app is already running

@when('I send a request to add {x} and {y}')
def step_impl(context, x, y):
    if y == 'no':
        response = requests.get(f'{BASE_URL}/add?x={x}')
    else:
        response = requests.get(f'{BASE_URL}/add?x={x}&y={y}')
    context.response = response

@then('I receive a response with the result {result}')
def step_impl(context, result):
    assert context.response.json()['result'] == int(result)

@then('I receive a {status_code} error')
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code)
