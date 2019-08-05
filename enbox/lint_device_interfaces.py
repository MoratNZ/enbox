#!/usr/bin/env python3

import argparse
from enbox.lib.config import load as loadConfig
from enbox.lib.device import get as getDevice


def main():
    parser = argparse.ArgumentParser(
        description='Check a device to ensure all interfaces that are active are configured appropriately in NetBox.')
    parser.add_argument('-device', metavar="deviceName",
                        help="Name of device we will be linting.", type=str, default="./enbox.cfg")
    parser.add_argument('-configFile', metavar="file",
                        help="Config file to use (for details of the NetBox server to check).", type=str)
    parser.add_argument("-v", help="Verbose Output", action="store_true")

    args = parser.parse_args()

    config = loadConfig(args['configFile'])

    device = getDevice(args['device'])


if __name__ == "__main__":
    main()
