'''
Gibraltar objects and functions related to pulling data from online APIs, and
storing it locally.
'''

import logging
import urllib.request
import json

from ._config import config

logger = logging.getLogger('gibraltar_ow_stats.DataPuller')

class DataPuller:

	def __init__(self):
		self.logger = logging.getLogger('gibraltar_ow_stats.DataPuller.DataPuller')
		self.logger.debug('Initializing DataPuller instance...')
		self.logger.debug('DataPuller instance initialized.')

	def pull_data(self, battletag, battletag_ID, region):
		'''
		Get data for the given account

		Uses the web API specified in the config file. Currently PC only.
		'''
		## Convert battletag and numeric ID to full username
		username = battletag+'-'+str(battletag_ID)
		## Generate target url based on config
		target_url = config.get('api', 'url').format(region=region, username=username)
		self.logger.info('Fetching data from {}'.format(target_url))
		## Fetch data
		self.fetched_data = json.loads(urllib.request.urlopen(target_url).read())
