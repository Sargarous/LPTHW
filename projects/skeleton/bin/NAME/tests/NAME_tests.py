from nose.tools import*
import NAME

def setup():
    print("SETUP!")

def teardown():
    print("Tear Down!")

def test_basic():
    print("I RAN!", end='')
