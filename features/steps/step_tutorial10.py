from behave import given, when, then
from hamcrest import assert_that, equal_to
from calculator import Calculator

@given('I have a calculator')
def step_impl(context):
    context.calculator = Calculator()

@when('I add "{x:d}" and "{y:d}"')
def step_impl(context, x, y):
    assert isinstance(x, int)
    assert isinstance(y, int)
    context.calculator.add2(x, y)

@then('the calculator returns "{expected:d}"')
def step_impl(context, expected):
    assert isinstance(expected, int)
    assert_that(context.calculator.result, equal_to(expected))
