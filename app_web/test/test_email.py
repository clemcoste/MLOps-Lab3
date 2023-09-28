import sys
from app_web.src.email import get_email_from_input
# Always run from app_web/test
sys.path += ['../src'] 

def test_get_email_valid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'clement@coste.fr')
    assert get_email_from_input() is 'clement@coste.fr'

def test_get_email_no_at_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'clementcoste.fr')
    assert get_email_from_input() == None
    
def test_get_email_no_point_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'clement@costefr')
    assert get_email_from_input() == None
    
def test_get_email_no_point_no_at_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'clementcostefr')
    assert get_email_from_input() == None