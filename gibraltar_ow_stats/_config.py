'''
Config parameters for Gibraltar.
'''

import os
import configparser
import logging

logger = logging.getLogger('gibraltar_ow_stats._config')

DEFAULT_CONFIG_DICT = {
	'localfiles': {
		'working_dir': '~/gibraltar-ow-stats/',
	},
	'userprofile': {
		'battletag': 'Surefour',
		'battletag_id': 2559,
		'platform': 'pc',
		'region': 'us',
	},
	'api': {
		'url': 'https://ovrstat.com/stats/pc/{region}/{username}',
	},
}

DEFAULT_CONFIG_PATH = os.path.expanduser('~/.config/gibraltar-ow-stats/gibraltar.ini')

def generate_new_config(config_dict=DEFAULT_CONFIG_DICT):
	new_config = configparser.ConfigParser()
	for section, section_values in config_dict.items():
		new_config.add_section(section)
		for key, value in section_values.items():
			new_config.set(section, key, value)
	return new_config

def write_config(new_config, config_path):
	with open(config_path, 'w') as new_file:
		new_config.write(new_file)
	return config_path

def read_config(config_path):
	with open(config_path) as config_file:
		config_data = config_file.read()
	return config_data

def parse_config(config_data):
	config = configparser.ConfigParser(allow_no_value=True)
	config.read_string(config_data)
	return config

def get_config(config_path):
	config_data = read_config(config_path)
	config = parse_config(config_data)
	return config

## Load config file
logger.info('Looking for config file at {}'.format(DEFAULT_CONFIG_PATH))
if not os.path.exists(DEFAULT_CONFIG_PATH):
	logger.info('Config file does not exist; auto-generating new config...')
	new_config = generate_new_config()
	new_config_path = write_config(new_config, DEFAULT_CONFIG_PATH)
	logger.info('New config file generated at {}'.format(new_config_path))
## Load from file
logger.info('Reading config file at {}'.format(DEFAULT_CONFIG_PATH))
config = get_config(DEFAULT_CONFIG_PATH)
logger.info('Config loaded.')
## Preview values
logger.debug('Current config values:')
for section in config.sections():
	logger.debug('Section: {}'.format(section))
	for options in config.options(section):
		logger.debug('{} {} {}'.format(options, config.get(section, options), str(type(options))))
##
