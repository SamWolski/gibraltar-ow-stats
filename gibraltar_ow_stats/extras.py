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

	Return value is the (expanded) path to the working directory.
	'''
	## Expand path
	working_dir = os.path.expanduser(working_dir)
	## Check for existence and create
	os.makedirs(working_dir, exist_ok=True)
	## Create additional required subdirs
	data_dir = os.path.join(working_dir, 'data')
	os.makedirs(data_dir, exist_ok=True)
	analysis_dir = os.path.join(working_dir, 'analysis')
	os.makedirs(analysis_dir, exist_ok=True)
	## Return working_dir path
	return working_dir
