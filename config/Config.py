__author__ = 'matt'
#! /usr/bin/python
from ConfigBase import Config

import os
import inspect
import logging

config = Config()

config['db_connection_string'] = 'mysql://matt:testpassword@localhost'

# load local config overrides
# these can be passed in env variables
if 'TEST_CONFIG' in os.environ:
    configModule = 'config.' + os.environ['TEST_CONFIG']
    print 'Using', configModule
    localConfig = __import__(configModule)
    config.update(getattr(localConfig, os.environ['TEST_CONFIG']).config)
