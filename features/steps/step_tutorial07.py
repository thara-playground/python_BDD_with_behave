from behave import given, when, then
from hamcrest import assert_that, has_items
from hamcrest.library.collection.issequence_containinginanyorder import contains_inanyorder

@then('we will have the following people in "{department}"')
def step_impl(context, department):
    """
    Compares expected with actual persons in a department.
    NOTE: Unordered comparison (ordering is not important)
    """
    department_ = context.model.departments.get(department, None)
    if not department:
        assert_that(False, "Department {0} is unknown".format(department))
    # -- NORMAL CASE
    expected_persons = [ row['name'] for row in context.table ]
    actual_persons = department_.members

    # -- UNORDERED TABLE-COMPARISON (using:pyhamcrest)
    assert_that(contains_inanyorder(*expected_persons), actual_persons)

@then('we will have at least the following people in "{department}"')
def step_impl(context, department):
    """
    Compress subset of persons with actual persons in a department.
    NOTE: Unordered subset comparison
    """
    department_ = context.model.departments.get(department, None)
    if not department_:
        assert_that(False, 'Department {0} is unknown'.format(department))
    # -- NORMAL CASE
    expected_persons = [ row['name'] for row in context.table ]
    actual_persons = department_.members

    # -- TABLE-SUBSET-COMPARISON (using:pyhamcrest)
    assert_that(has_items(*expected_persons), actual_persons)


# @then('we will have at least the following people in "Super-sonic Cars"')
# def step_impl(context):
#     assert False
