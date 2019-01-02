'''
Gibraltar objects and functions related to pulling data from online APIs, and
storing it locally.
'''

import logging

from ._config import config

logger = logging.getLogger('gibraltar_ow_stats.DataPuller')

class DataPuller:

	def __init__(self):
		self.logger = logging.getLogger('gibraltar_ow_stats.DataPuller.DataPuller')
		self.logger.debug('Initializing DataPuller instance...')
