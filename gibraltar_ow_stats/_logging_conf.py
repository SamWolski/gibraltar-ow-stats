## Configuration for Gibraltar's logging

LOGGING_CONF = {
	'version': 1,

	'loggers': {
	},

	'handlers': {
		'defaultFileHandler': {
			'class': 'logging.FileHandler',
			'level': 'DEBUG',
			'formatter': 'rootFormatter',
			'filename': 'gibraltar.log',
		},
	},

	'formatters': {
		'rootFormatter': {
			'format': '%(asctime)s %(name)-16s %(levelname)-8s %(message)s',
			'datefmt': '%y-%m-%d %H:%M:%S',
		},
	},

	'root': {
		'level': 'DEBUG',
		'handlers': ['defaultFileHandler'],
	},
}
