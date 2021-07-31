from nose.tools import*
import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
