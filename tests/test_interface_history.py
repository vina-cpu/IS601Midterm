'''Tests for Testing History and Exit/Menu Commands with Interface - without Save b/c I want to ignore that file in github actions - it is in log and env tests'''
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
    assert "Num 1" in captured.out # can not do these in the same line, getting spacing inconsistencies"
    assert "Num 2" in captured.out
    assert "0" in captured.out # thesei three let me know that i successfully looked at the history in the command line

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
    assert "Num 1" in captured.out
    assert "Num 2" in captured.out
    assert "0" in captured.out
    assert "Empty DataFrame\nColumns: [Num 1, Num 2, Operation, Result]" in captured.out

def test_interface_start_delete(capfd, monkeypatch):
    '''Test that the REPL can handle deleting an index correctly'''
    inputs = iter(['clear', 'add', '5', '-4', 'look', 'delete', '0', 'look', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()
    captured = capfd.readouterr()
    assert "Deleting index 0 now ... " in captured.out
    assert "Index: []" in captured.out # this lets me know that an index was deleted after there were items in the DataFrame

def test_interface_start_delete_empty(capfd, monkeypatch):
    '''Test that the REPL can handle deleting an empty dataframe correctly'''
    inputs = iter(['clear', 'delete', '0', 'look', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()
    captured = capfd.readouterr()
    assert "An error occured: '[0] not found in axis'" in captured.out

def test_interface_start_menu(capfd, monkeypatch):
    '''Test that the REPL dynamically prints a menu'''
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()
    captured = capfd.readouterr()
    assert "Type 'add' to add two numbers" in captured.out
    assert "Type 'clear' to clear the calculator's history" in captured.out
    assert "Type 'delete' to be asked for an index in the history to delete" in captured.out
    assert "Type 'divide' to divide two numbers" in captured.out
    assert "Type 'exit' to exit the program" in captured.out
    assert "Type 'load' to load a history located in a .csv file: be sure to know where your file is!" in captured.out
    assert "Type 'look' to look at the current history without saving it" in captured.out
    assert "Type 'menu' to look at the menu of commands" in captured.out
    assert "Type 'multiply' to multiply two numbers" in captured.out
    assert "Type 'save' to save the current history into a new file in the 'saves' folder; if the 'saves' folder does not exist, this will also create the 'saves' folder" in captured.out
    assert "Type 'subtract' to subtract one number from another" in captured.out
