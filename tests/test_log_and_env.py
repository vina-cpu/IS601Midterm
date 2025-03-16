'''My Tests for Logging, Saving, and Environment Variables'''
from pathlib import Path

def test_exists_log_file():
    '''Test to show at least one file is in logs file'''
    # adding log files down to the minute, don't want to test by number of files here
    assert any(Path("logs").iterdir()) is True

def test_exists_save_file():
    '''Test to show at least one file is in saves folder'''
    # adding files in saves down to the minute, don't want to test by number of files here
    # ran this outside of pytest so that there is at least one
    assert any(Path("saves").iterdir()) is True
