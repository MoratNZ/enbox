#!/usr/bin/env python3

import configparser
import os


def load(fileName):
    """Load the enbox config file from the specified location, and ensure that it has sane contents.

    Arguments:
        fileName {string} -- the file 

    Returns:
        configParser  -- effectively a dict of dicts of config settings.
    """

    config = configparser.ConfigParser()

    if os.path.exists(fileName):
        config.read(fileName)
    else:
        raise IOError("Config file '%s' does not exist" % fileName)

    config = configparser.ConfigParser()
    config.read(fileName)

    return config
