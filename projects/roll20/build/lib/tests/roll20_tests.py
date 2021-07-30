from nose.tools import*
import roll20

def setup():
    print("SETUP!")

def teardown():
    print("Tear Down!")

def test_basic():
    print("I RAN!", end='')
