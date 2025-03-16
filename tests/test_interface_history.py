'''Tests for Testing History and Exit/Menu Commands with Interface'''
import pytest
from commands import Interface

def test_interface_start_exit_command(capsys, monkeypatch):
    '''Test that the REPL exits with 'exit' input''' 
    #this is SIMULATING USER
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()

def test_interface_start_no_command(capfd, monkeypatch):
    '''Test that the REPL doesn't explode if i put in something other than a command it knows'''
    inputs = iter(['unknown command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()
    captured = capfd.readouterr()
    assert "No such command: unknown command" in captured.out

def test_interface_start_look(capfd, monkeypatch):
    '''Test that the REPL can handle looking at a history correctly'''
    inputs = iter(['add', '1', '2', 'look', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()
    captured = capfd.readouterr()
    assert "Num 1 Num 2 Operation Result" in captured.out
    assert "1     2       add      3" in captured.out

def test_interface_start_clear(capfd, monkeypatch):
    '''Test that the REPL can handle clearing history correctly''' # do not need to test for clearing if it's empty because i am just reinitializing a new empty dataframe each time it clears
    inputs = iter(['add', '1', '2', 'look', 'clear', 'look', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()
    captured = capfd.readouterr()
    assert "Clearing history now ... " in captured.out
    assert "History cleared!" in captured.out
    assert "Num 1 Num 2 Operation Result" in captured.out
    assert "1     2       add      3" in captured.out
    assert "Empty DataFrame\nColumns: [Num 1, Num 2, Operation, Result]" in captured.out

def test_interface_start_delete_empty(capfd, monkeypatch):
    '''Test that the REPL can handle deleting an index correctly'''
    inputs = iter(['clear', 'add', '5', '-4', 'look', 'delete', '0', 'look', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()
    captured = capfd.readouterr()
    assert "Deleting index 0 now ... " in captured.out
    assert "Num 1 Num 2 Operation Result" in captured.out
    assert "5    -4       add      1" in captured.out
    assert "Empty DataFrame\nColumns: [Num 1, Num 2, Operation, Result]" in captured.out
