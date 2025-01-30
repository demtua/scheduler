import threading
import time

class Scheduler:
    """
    A simple scheduler that runs a function at a fixed interval in a separate thread.

    Attributes:
        function (callable): The function to execute periodically.
        interval (float): Time interval in seconds between executions.
        stop_event (threading.Event): Event used to signal stopping the scheduler.
        thread (threading.Thread): Background thread running the scheduled function.
    """

    def __init__(self, function, interval):
        """
        Initializes the scheduler with a function and an interval.

        Args:
            function (callable): The function to execute at each interval.
            interval (float): The time interval (in seconds) between function executions.
        """
        self.function = function
        self.interval = interval
        self.stop_event = threading.Event()  # Event to control stopping the scheduler
        self.thread = threading.Thread(target=self._run)  # Create a new thread to run the function
        self.thread.daemon = True  # The thread will stop when the main program exits
        self.thread.start()  # Start the scheduler thread

    def _run(self):
        """
        Private method that runs the function at regular intervals
        until the stop event is set.
        """
        while not self.stop_event.is_set():
            time.sleep(self.interval)  # Wait for the specified interval
            self.function()  # Execute the function

    def cancel(self):
        """
        Stops the scheduler by setting the stop event and waiting for the thread to exit.
        """
        self.stop_event.set()  # Signal the thread to stop
        self.thread.join()  # Ensure the thread completes execution before proceeding
