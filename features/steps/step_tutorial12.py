from behave import given, when, then

@given('behaveをインストールしている')
def step_impl(context):
    context.execute_steps("前提 we have behave installed")

@when('テストを実装する')
def step_impl(context):
    context.execute_steps("もし we implement a test")

@then('behaveがそれをテストしてくれる!')
def step_impl(context):
    context.execute_steps("ならば behave will test it for us!")
