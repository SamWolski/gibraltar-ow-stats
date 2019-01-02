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

from gibraltar_ow_stats._logging_conf import LOGGING_CONF

logging.config.dictConfig(LOGGING_CONF)
logger = logging.getLogger(__name__)

from gibraltar_ow_stats._config import config

__version__ = '0.1.dev10'

from gibraltar_ow_stats.DataPuller import DataPuller
from gibraltar_ow_stats.extras import verify_working_dir
