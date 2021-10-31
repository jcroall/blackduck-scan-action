#!/usr/bin/env python

import argparse
import json
import sys
import os
import subprocess

detect_cmd = "/detect.sh"

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run Black Duck Security Scan")
    parser.add_argument("--url", required=True, type=str, help="Black Duck Hub URL")
    parser.add_argument("--token", required=True, type=str, help="Black Duck Hub Token")
    parser.add_argument("--mode", default="intelligent", type=str, help="Black Duck scanning mode, either intelligent or rapid")
    parser.add_argument("--output", default="blackduck-output", type=str, help="Output directory")

    args = parser.parse_args()

    url = args.url
    token = args.token
    if (url == None or token == None):
        print(f"ERROR: Must specify Black Duck Hub URL and API Token")
        sys.exit(1)
    mode = args.mode
    if (mode != "intelligent" and mode != "rapid"):
        print(f"ERROR: Scanning mode must be intelligent or rapid")
        sys.exit(1)
    output = args.output

    detect_opts = f"--blackduck.url=\"{url}\" --blackduck.api.token=\"{token}\" --detect.blackduck.scan.mode={mode} --detect.output.path={output}"

    print(f"INFO: Running Black Duck detect with the following options: {detect_opts}")

    result = subprocess.Popen(f"/bin/bash {detect_cmd} {detect_opts}", shell=True)
    detect_output = result.communicate()[0]
    return_code = result.returncode

    print(f"INFO: Done, return value {return_code}")

    sys.exit(return_code)
