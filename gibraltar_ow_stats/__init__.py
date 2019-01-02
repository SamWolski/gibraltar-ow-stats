'''
Gibraltar: Overwatch stats tracking and analysis
==================================================

Gibraltar (named after Winston's office location) pulls your Overwatch stats
from any web-based API, stores them as JSON files, and provides useful
functions for analysis and seeing trends over time.
'''

import os
import logging
import logging.config

from _logging_conf import LOGGING_CONF
import _config

logging.config.dictConfig(LOGGING_CONF)
logger = logging.getLogger(__name__)

__version__ = '0.1.dev2'

## Config file
CONFIG_PATH = os.path.expanduser('~/.config/gibraltar-ow-stats/gibraltar.ini')
logger.info('Looking for config file at {}'.format(CONFIG_PATH))
if not os.path.exists(CONFIG_PATH):
	logger.info('Config file does not exist; auto-generating new config...')
	new_config = _config.generate_new_config()
	new_config_path = _config.write_config(new_config, CONFIG_PATH)
	logger.info('New config file generated at {}'.format(new_config_path))
## Load from file
logger.info('Reading config file at {}'.format(CONFIG_PATH))
config = _config.get_config(CONFIG_PATH)
logger.info('Config loaded.')
## Preview values
logger.debug('Current config values:')
for section in config.sections():
	logger.debug('Section: {}'.format(section))
	for options in config.options(section):
		logger.debug('{} {} {}'.format(options, config.get(section, options), str(type(options))))
##
