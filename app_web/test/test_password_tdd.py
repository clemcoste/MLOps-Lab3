import sys
from app_web.src.password_tdd import get_password_from_input
# Always run from app_web/test
sys.path += ['../src'] 

def test_get_password_valid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'cle@1993')
    assert get_password_from_input() is 'cle@1993'
    
def test_get_password_too_short_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'cle@1')
    assert get_password_from_input() == None
    
def test_get_password_no_number_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'cle@ment')
    assert get_password_from_input() == None
    
def test_get_password_no_letter_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '12345678')
    assert get_password_from_input() == None
    
def test_get_password_no_special_char_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'clement1993')
    assert get_password_from_input() == None
    
def test_get_password_no_special_char_no_number_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'clementcoste')
    assert get_password_from_input() == None
    
def test_get_password_only_special_char_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'é@ù:,à$`-!')
    assert get_password_from_input() == None