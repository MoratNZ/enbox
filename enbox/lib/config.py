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
        raise OSError("Config file '%s' does not exist" % fileName)

    config = configparser.ConfigParser()
    config.read(fileName)

    return config


def create(fileName, url=None, token="your.token.here"):
    """Creates a default config file in the indicated location.

    Arguments:
        fileName {string} -- Path and filename for where you want the file created

    Keyword Arguments:
        url {string} -- The URL (including http: / https:, but not /api) for your NetBox API (default: {"your.url.here"})
        token {string} -- An API access token for your enbox user within NetBox (default: {"your.token.here"})

    Returns:
        string -- Success message
    """
    config = configparser.ConfigParser(allow_no_value=True)

    config['NetBox'] = {}
    config.set(
        "NetBox", "\n# The URL for the API root for your NetBox install\nUrl", url)
    config.set("NetBox", "Token", token)
    config.set("NetBox", "KeyFile", "secrets/keyFile")

    config['ssh'] = {}
    config.set(
        "ssh", "\n# Default username to use for SSH connections\nuserName", "sshUserName")

    passwordComment = ("\n# Uncomment the below line if you want to specify an SSH password for the\n"
                       "# above user.\n"
                       "#\n"
                       "# If not specified here, you will be prompted to enter it\n"
                       "# password = superSekretP455w0rd")

    config.set("ssh", passwordComment)

    with open(fileName, 'w') as configfile:
        config.write(configfile)

    return "Config file successfully generated"
