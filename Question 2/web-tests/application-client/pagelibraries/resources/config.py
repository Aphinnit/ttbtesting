import os
import sys


class Config(object):
    """Configuration variables for this test suite

    This creates a variable named CONFIG (${CONFIG} when included
    in a test as a variable file.

    Example:

    *** Settings ***
    | Variable | ../../resources/project-name/config.py

    *** Test Cases ***
    | Example
    | | log | username: ${CONFIG}.username
    | | log | root url: ${CONFIG}.root_url

    """

    def __init__(self):
        _here = os.path.dirname(__file__)

        try:
            self.path_to_csv_file = _here[:_here.index("pagelibraries")] + "testdata/datafiles/"
        except ValueError:
        # Handle the error, maybe set a default path or log an error message.
            print("Error: 'pagelibraries' not found in the path.")

        sys.path.insert(0, os.path.abspath(os.path.join(_here, "..", "..")))
        sys.path.insert(0, os.path.abspath(os.path.join(_here)))
        self.root_url = "about:blank"
        self.protocol = "http://the-internet"
        self.branch = "herokuapp"
        self.cluster_url = "com/login"
     

    def __str__(self):
        """
        Used for string representation of an object
        """
        return "<Config: %s>" % str(self.__dict__)


# This creates a variable that robot can see
CONFIG = Config()
