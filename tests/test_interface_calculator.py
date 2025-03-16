'''Tests for Testing Calculator Commands with Interface'''
import pytest
from commands import Interface

def run_interface(inputs, monkeypatch, capfd):
    '''Helper function for running an interface - to reduce redundancy'''
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()
    captured = capfd.readouterr()
    return captured.out

def test_interface_start_add_command(capfd, monkeypatch):
    '''Test that the REPL can add'''
    inputs = iter(['add', '2', '4', 'exit'])
    output = run_interface(inputs, monkeypatch, capfd)
    assert "The result of 2 add 4 is equal to 6" in output

def test_interface_start_add_invalid_oper(capfd, monkeypatch):
    '''Test that REPL can show invalid operation error for add'''
    inputs = iter(['add', 'a', '4', 'add', '4', 'b', 'exit'])
    output = run_interface(inputs, monkeypatch, capfd)
    assert "Invalid number input: a or 4 is not a valid number." in output
    assert "Invalid number input: 4 or b is not a valid number." in output

def test_interface_start_subtract_command(capfd, monkeypatch):
    '''Test that the REPL can subtract'''
    inputs = iter(['subtract', '-1', '2', 'exit'])
    output = run_interface(inputs, monkeypatch, capfd)
    assert "The result of -1 subtract 2 is equal to -3" in output

def test_interface_start_subtract_invalid_oper(capfd, monkeypatch):
    '''Test that REPL can show invalid operation error for subtract'''
    inputs = iter(['subtract', 'a', '4', 'subtract', '4', 'b', 'exit'])
    output = run_interface(inputs, monkeypatch, capfd)
    assert "Invalid number input: a or 4 is not a valid number." in output
    assert "Invalid number input: 4 or b is not a valid number." in output

def test_interface_start_multiply_command(capfd, monkeypatch):
    '''Test that the REPL can multiply'''
    inputs = iter(['multiply', '3', '5', 'exit'])
    output = run_interface(inputs, monkeypatch, capfd)
    assert "The result of 3 multiply 5 is equal to 15" in output

def test_interface_start_multiply_invalid_oper(capfd, monkeypatch):
    '''Test that REPL can show invalid operation error for multiply'''
    inputs = iter(['multiply', 'a', '4', 'multiply', '4', 'b', 'exit'])
    output = run_interface(inputs, monkeypatch, capfd)
    assert "Invalid number input: a or 4 is not a valid number." in output
    assert "Invalid number input: 4 or b is not a valid number." in output

def test_interface_start_divide_command(capfd, monkeypatch):
    '''Test that the REPL can divide'''
    inputs = iter(['divide', '2', '4', 'exit'])
    output = run_interface(inputs, monkeypatch, capfd)
    assert "The result of 2 divide 4 is equal to 0.5" in output

def test_interface_start_divide_invalid_oper(capfd, monkeypatch):
    '''Test that REPL can show invalid operation error for divide'''
    inputs = iter(['divide', 'a', '4', 'divide', '4', 'b', 'exit'])
    output = run_interface(inputs, monkeypatch, capfd)
    assert "Invalid number input: a or 4 is not a valid number." in output
    assert "Invalid number input: 4 or b is not a valid number." in output

def test_interface_start_divide_divide_zero(capfd, monkeypatch):
    '''Test that REPL can handle divide by zero correctly'''
    inputs = iter(['divide', '1', '0', 'exit'])
    output = run_interface(inputs, monkeypatch, capfd)
    assert "An error occured: Cannot divide by zero" in output
