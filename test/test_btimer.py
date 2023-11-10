# Pytests tests

from btimer import Timer
from time import sleep

def test_create_timer():
    """Test that a timer can be created"""
    t = Timer()
    assert isinstance(t, Timer)
    assert t.name is None
    assert t.precision == 2
    assert t.start_time is not None

def test_create_timer_with_name():
    """Test that a timer can be created with a name"""
    t = Timer("Task1")
    assert isinstance(t, Timer)
    assert t.name == "Task1"
    assert t.precision == 2
    assert t.start_time is not None

def test_create_timer_with_precision():
    """Test that a timer can be created with a precision"""
    t = Timer(precision=3)
    assert isinstance(t, Timer)
    assert t.name is None
    assert t.precision == 3
    assert t.start_time is not None

def test_create_timer_with_name_and_precision():
    """Test that a timer can be created with a name and precision"""
    t = Timer("Task1", 3)
    assert isinstance(t, Timer)
    assert t.name == "Task1"
    assert t.precision == 3
    assert t.start_time is not None

def test_timer_milliseconds():
    """Test that the timer returns the elapsed time in milliseconds"""
    t = Timer()
    sleep(0.1)
    assert t.milliseconds >= 99

def test_timer_seconds():
    """Test that the timer returns the elapsed time in seconds"""
    t = Timer()
    sleep(0.1)
    assert t.seconds >= 0.1

def test_timer_minutes():
    """Test that the timer returns the elapsed time in minutes"""
    t = Timer(precision=5)
    sleep(0.1)
    assert t.minutes >= 0.0016

def test_timer_hours():
    """Test that the timer returns the elapsed time in hours"""
    t = Timer(precision=6)
    sleep(0.1)
    assert t.hours >= 0.000027

def test_timer_str():
    """Test that the timer returns a string representation"""
    t = Timer("Task1", 1)
    sleep(0.1)
    assert isinstance(str(t), str)
    assert str(t) == "Timer 'Task1': 0.1 seconds"

def test_timer_str_no_name():
    """Test that the timer returns a string representation without a name"""
    t = Timer(precision=1)
    sleep(0.1)
    assert isinstance(str(t), str)
    assert str(t) == "0.1 seconds"

def test_timer_repr():
    """Test that the timer returns a string representation"""
    t = Timer("Task1", 1)
    sleep(0.1)
    assert isinstance(repr(t), str)
    assert "Timer(name=Task1, precision=1, start_time=" in repr(t)
    assert "elapsed_time=0.1s)" in repr(t)




