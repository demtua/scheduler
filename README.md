# Python Scheduler

## Overview
`Scheduler` is a lightweight Python class that runs a specified function at a fixed interval using a separate thread. It allows periodic task execution without blocking the main program.

## Features
- Runs a function at a user-defined interval.
- Uses a background thread to execute the function asynchronously.
- Can be stopped gracefully.

## Installation
No installation is required. Simply copy the `Scheduler` class into your project.

## Usage

### Example 1: Running a Function Every 2 Seconds
```python
import time
from scheduler import Scheduler  # Import the Scheduler class

def my_task():
    print("Task executed at", time.strftime("%X"))

# Create a scheduler that runs `my_task` every 2 seconds
scheduler = Scheduler(my_task, 2)

# Let it run for 10 seconds, then stop
time.sleep(10)
scheduler.cancel()
