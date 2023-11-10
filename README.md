# btimer
A simple and useful code timer for python.

Originally intended for web apps and batch jobs, btimer offers a simple timing solution implemented with minimal code.

Created by Ben Hymans in 2023.

MIT License

## Install

```bash
pip install git+https://github.com/benhymans/btimer.git
```

## Example Usage

```python
from btimer import Timer

    t1 = Timer() # Timer starts automatically
    # Code to be timed
    t1.seconds # Returns the elapsed time in seconds
    
    t2 = Timer("Task2", 4) # Timer name and precision are optional
    # Code to be timed
    t2.minutes # Available units: milliseconds, seconds, minutes, and hours

    print(t1) # Returns a string of the elapsed time in seconds with timer name```