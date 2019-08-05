
import unittest
import os
import sys
import configparser

scriptPath = os.path.split(__file__)[0]  # noqa
sys.path.append("%s/../" % scriptPath)  # noqa

from enbox.lint_device_interfaces import main  # noqa
from enbox.lib.config import load as loadConfig  # noqa

sampleConfigFileName = "enbox.cfg.example"


class LoadTests(unittest.TestCase):
    def test_nonexistent_file_errors(self):
        with self.assertRaises(IOError):
            loadConfig("nonexistent_file")

    def test_config_file_loads(self):
        config = loadConfig("%s/../%s" % (scriptPath, sampleConfigFileName))
        self.assertIsInstance(config, configparser.ConfigParser)

# pylint: disable=invalid-sequence-index


class SampleConfigFileTests(unittest.TestCase):

    def test_sample_config_has_correct_entries(self):
        config = loadConfig("%s/../%s" % (scriptPath, sampleConfigFileName))

        url = config['NetBox']['ApiUrl']
        self.assertEqual(url, "your.url.here",
                         "Sample config file missing netbox url")

        sshUserName = config['ssh']['userName']
        self.assertEqual(sshUserName, "sshUserName")


if __name__ == '__main__':
    unittest.main()
