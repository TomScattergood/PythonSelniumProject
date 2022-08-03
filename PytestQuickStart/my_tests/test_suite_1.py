import pytest
from pytest import mark

@mark.smoke
def test_login_page_valid_user():
    print("Login with valid user")

@mark.smoke
@mark.regression
def test_login_wrong_password():
    print("Login with wrong password")
    #assert 1==2, 'failed'
