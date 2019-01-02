'''
Config parameters for Gibraltar.
'''

import ConfigParser
import io

DEFAULT_CONFIG_DICT = {
	'userprofile': {
		'battletag': 'Surefour',
		'battletag_id': 2559,
	},
	'api': {
		'url': 'https://ovrstat.com/stats/pc/{region}/{username}',
	},
}


def generate_new_config(config_dict=DEFAULT_CONFIG_DICT):
	new_config = ConfigParser.ConfigParser()
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
	config = ConfigParser.RawConfigParser(allow_no_value=True)
	config.readfp(io.BytesIO(config_data))
	return config

def get_config(config_path):
	config_data = read_config(config_path)
	config = parse_config(config_data)
	return config
