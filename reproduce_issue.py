#!/usr/bin/env python

import os
import sys
import tempfile

from octodns.manager import Manager, ManagerException

# Create a temporary directory for YAML_TMP_DIR
temp_dir = tempfile.mkdtemp()
os.environ['YAML_TMP_DIR'] = temp_dir

# Path to the test config file
config_file = os.path.join('tests', 'config', 'dynamic-config.yaml')

try:
    # Try to sync a non-existent zone
    Manager(config_file).sync(['missing.zones.'])
except ManagerException as e:
    # Print the exception message
    print(f"Exception message: {str(e)}")
    # Check if the message contains the expected text
    if 'Requested zone:' in str(e):
        print("Test passed: Exception message contains 'Requested zone:'")
        sys.exit(0)
    else:
        print(
            "Test failed: Exception message does not contain 'Requested zone:'"
        )
        print(f"Actual message: {str(e)}")
        sys.exit(1)
