'''
Additional functions that aren't exclusively associated with either the
DataPuller or <future analysis class>.
'''

import os

from gibraltar_ow_stats._config import config

DEFAULT_WORKING_DIR = config.get('localfiles', 'working_dir')

def verify_working_dir(working_dir=DEFAULT_WORKING_DIR):
	'''
	Verify that the working directory exists, and create it if it doesn't.

	Return value indicates whether or not directory existed before this
	function was called.
	'''
	## Expand path
	working_dir = os.path.expanduser(working_dir)
	## Check for existence and create
	if not os.path.exists(working_dir):
		os.makedirs(working_dir, exist_ok=True)
		return False
	else:
		return True
