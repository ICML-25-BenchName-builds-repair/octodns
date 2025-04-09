#!/usr/bin/env python

import os

from octodns.manager import Manager, ManagerException

# Set the environment variable needed by the test
os.environ['YAML_TMP_DIR'] = '/tmp'
os.environ['YAML_TMP_DIR2'] = '/tmp'

# Path to the test config file
config_file = 'tests/config/dynamic-config.yaml'

try:
    # Try to sync a non-existent zone
    Manager(config_file).sync(['missing.zones.'])
except ManagerException as e:
    # Print the exception message
    print(f"Exception message: {str(e)}")
    # Check if the expected text is in the exception message
    if 'Requested zone:' in str(e):
        print("Test PASSED: Exception message contains 'Requested zone:'")
    else:
        print(
            "Test FAILED: Exception message does not contain 'Requested zone:'"
        )
        print(f"Actual message: {str(e)}")
