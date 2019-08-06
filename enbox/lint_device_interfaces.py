#!/usr/bin/env python3

import argparse
from enbox.lib.config import load as loadConfig
import enbox.lib.netboxapi
from pprint import pprint


def _getArgs():
    parser = argparse.ArgumentParser(
        description='Check a device to ensure all interfaces that are active are configured appropriately in NetBox.')
    parser.add_argument('-device', metavar="deviceName",
                        help="Name of device we will be linting.", type=str)
    parser.add_argument('-configFile', metavar="file",
                        help="Config file to use (for details of the NetBox server to check).", type=str, default="./enbox.cfg")
    parser.add_argument("-v", help="Verbose Output", action="store_true")

    return parser.parse_args()


def main():
    args = _getArgs()

    config = loadConfig(args.configFile)

    api = enbox.lib.netboxapi.init(config)

    device = api.dcim.devices.get(name=args.device)
    deviceInterfaces = api.dcim.interfaces.filter(device_id=device.id)


if __name__ == "__main__":
    main()
