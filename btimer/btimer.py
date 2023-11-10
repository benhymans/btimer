"""
btimer Module

This module provides a simple way to measure execution time with minimal code.

Author: Ben Hymans
Email: ben@hytreks.org
Version: 1.0.0

Usage:
    from btimer import Timer

    t1 = Timer() # Timer starts automatically
    # Code to be timed
    t1.seconds # Returns the elapsed time in seconds
    
    t2 = Timer("Task2", 4) # Timer name and precision are optional
    # Code to be timed
    t2.minutes # Available units: milliseconds, seconds, minutes, and hours

    print(t1) # Returns a string of the elapsed time in seconds with timer name
"""

from time import perf_counter

class Timer:
    def __init__(self, name: str = None, precision: int = 2):
        """Set up the timer and implicilty start it"""
        # Timer name
        self.name = name

        # Precision
        self.precision = precision

        # implicitly start the timer
        self.start_time = perf_counter()

    def _calc_time(self):
        """Calculate the elapsed time"""
        return perf_counter() - self.start_time
    
    @property
    def milliseconds(self) -> float:
        """Return the elapsed time in milliseconds"""
        return round(self._calc_time() * 1000, self.precision)
    
    @property
    def seconds(self) -> float:
        """Return the elapsed time in seconds"""
        return round(self._calc_time(), self.precision)
    
    @property
    def minutes(self) -> float:
        """Return the elapsed time in minutes"""
        return round(self._calc_time() / 60, self.precision)
    
    @property
    def hours(self) -> float:
        """Return the elapsed time in hours"""
        return round(self._calc_time() / 3600, self.precision)

    def __str__(self):
        """Return a string representation of the timer"""
        if self.name is not None:
            return f"Timer '{self.name}': {self.seconds} seconds"
        else:
            return f"{self.seconds} seconds"
        
    def __repr__(self):
        """Return a string representation of the timer"""
        details = f"Timer(name={self.name}, precision={self.precision}, start_time={self.start_time}, elapsed_time={self.seconds}s)"
        return details
    