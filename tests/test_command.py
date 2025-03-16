'''Tests for Commands'''
import pytest
from plugins.add import AddCommand
from plugins.subtract import SubtractCommand
from plugins.multiply import MultiplyCommand
from plugins.divide import DivideCommand
from plugins.exit import ExitCommand

def test_add_command(capfd, monkeypatch):
    '''Test AddCommand()'''
    inputs = iter(['1', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    newadd = AddCommand()
    newadd.execute()
    captured = capfd.readouterr()
    assert "The result of 1 add 2 is equal to 3" in captured.out

def test_subtract_command(capfd, monkeypatch):
    '''Test SubtractCommand()'''
    inputs = iter(['1', '4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    newsubtract = SubtractCommand()
    newsubtract.execute()
    captured = capfd.readouterr()
    assert "The result of 1 subtract 4 is equal to -3" in captured.out

def test_multiply_command(capfd, monkeypatch):
    '''Test MultiplyCommand()'''
    inputs = iter(['200', '1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    newmultiply = MultiplyCommand()
    newmultiply.execute()
    captured = capfd.readouterr()
    assert "The result of 200 multiply 1 is equal to 200" in captured.out

def test_divide_command(capfd, monkeypatch):
    '''Test DivideCommand()'''
    inputs = iter(['1', '-1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    newdivide = DivideCommand()
    newdivide.execute()
    captured = capfd.readouterr()
    assert "The result of 1 divide -1 is equal to -1" in captured.out

def test_exit_command(capfd):
    '''Test ExitCommand()'''
    newexit = ExitCommand()
    with pytest.raises(SystemExit):
        newexit.execute()
    captured = capfd.readouterr()
    assert "Goodbye!" in captured.out
