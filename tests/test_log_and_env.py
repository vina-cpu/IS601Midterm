'''My Tests for Logging and Environment Variables'''
from pathlib import Path
from commands import Interface

def test_exists_log_file():
    '''Test to show at least one file is where i put my log files'''
    # adding log files down to the minute, don't want to test by number of files here
    myinterface = Interface.newInterface()
    assert any(Path(myinterface.get_env("LOG_DESTINATION")).iterdir()) is True

def test_env_var():
    '''Test to test that environment variables are inside of Interface'''
    myinterface = Interface.newInterface()
    assert myinterface.get_env("LOG_LEVEL") is not None
    assert myinterface.get_env("LOG_DESTINATION") is not None
