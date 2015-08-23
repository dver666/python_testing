# -*- coding: utf-8 -*-
import sys
sys.path.append('/home/diver/www_python_testing/bank')
sys.path.append('/home/diver/www_python_testing/bank/test')
sys.path.append('/home/diver/www_python_testing/bank/test/bdd')
sys.path.append('/home/diver/www_python_testing/bank/test/bdd/features')
sys.path.append('/home/diver/www_python_testing/bank/test/bdd/steps')
sys.path.append('/home/diver/www_python_testing/bank/bank')
sys.path.append('/home/diver/www_python_testing/bank/templates')

from lettuce import *
from nose.tools import assert_equal
from webtest import TestApp

from bank_app import app

@step(u'I visit the homepage')
def i_visit_the_homepage(step):
    world.browser=TestApp(app)
    world.response=world.browser.get('http://localhost:5000/')
    assert_equal(world.response.status_code,200)
    assert_equal(world.response.text,u'Hello World!')

@step(u'I enter the account number "([^"]*)"')
def when_enter_account_number_group1(step, account_number):
    form=world.response.forms['account-number']
    form['account_number']=account_number
    world.form_response=form.submit()
    assert_equal(world.form_response.status_code,200)
