"""Defines the application class that handles user interaction"""

from competition import Competition

class Application:
    """Defines the run method and handles the main interaction with the user"""

    def __init__(self):
        """Constructor for the Application class"""
        self._competition = Competition()

    def run(self):
        pass