'''My Tests for Logging and Environment Variables'''
from pathlib import Path

def test_exists_log_file():
    '''Test to show at least one file is in logs file'''
    # adding log files down to the minute, don't want to test by number of files here
    assert any(Path("logs").iterdir()) is True
