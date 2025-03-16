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

#def test_exists_save_file(): - THIS TEST IS IN test_log_and_env because i wanted to ignore it in git actions and building
#    '''Test to show at least one file is in saves folder'''
    # adding files in saves down to the minute, don't want to test by number of files here
    # ran this outside of pytest so that there is at least one
#    assert any(Path("saves").iterdir()) is True
