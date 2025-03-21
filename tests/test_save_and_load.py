'''Tests for Saving and Loading Files'''
from pathlib import Path
import pytest
from commands import Interface

def test_exists_save_file():
    '''Test to show at least one file is in saves folder'''
    # adding files in saves down to the minute, don't want to test by number of files here
    # ran this outside of pytest so that there is at least one
    # cov is low for save plugin; could test that saving a file does save a file,
    # but i don't want to save a file every time i run pytest
    assert any(Path("saves").iterdir()) is True

def test_load_file(capfd, monkeypatch):
    '''Test to show loading file from directory stored in env variable went successfully'''
    inputs = iter(['clear', 'load', 'saves/03.16.10.34.csv', 'look', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()
    captured = capfd.readouterr()
    assert "-1354" in captured.out # used a unique number in my input here to see if this specific file was loaded correctly

def test_load_wrong_file(capfd, monkeypatch):
    '''Test to show loading file from wrong directory doesn't crash my program'''
    inputs = iter(['clear', 'load', '', 'look', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()
    captured = capfd.readouterr()
    assert "An error occured: [Errno 2] No such file or directory: ''" in captured.out # used a unique number in my input here to see if this specific file was loaded correctly
