import sys
from app_web.src.username import get_username_from_input
# Always run from app_web/test
sys.path += ['../src'] 

def test_get_username_valid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'clementcoste')
    assert get_username_from_input() == 'clementcoste'

def test_get_username_space_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'clement coste')
    assert get_username_from_input() is None
    
def test_get_username_empty_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '')
    assert get_username_from_input() is None