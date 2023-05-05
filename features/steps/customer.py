from behave import given, when, then
from django.contrib.auth.models import User
from myapp.models import Customer
from django.conf import settings

# configure Django settings
settings.configure(
    DEBUG=True,
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'my_ecommerce',
    ]
)

@given('a new user with the username "{username}" and password "{password}"')
def step_create_user(context, username, password):
    User.objects.create_user(username=username, password=password)

@when('I create a new customer with the name "{name}" and email "{email}"')
def step_create_customer(context, name, email):
    user = User.objects.get(username=context.table[0]['username'])
    customer = Customer.objects.create(user=user, name=name, email=email)
    context.customer = customer

@then('the customer should have a user with the username "{username}" and password "{password}"')
def step_check_customer_user(context, username, password):
    user = context.customer.user
    assert user.username == username
    assert user.check_password(password)

@then('the customer should have the name "{name}"')
def step_check_customer_name(context, name):
    assert context.customer.name == name

@then('the customer should have the email "{email}"')
def step_check_customer_email(context, email):
    assert context.customer.email == email
