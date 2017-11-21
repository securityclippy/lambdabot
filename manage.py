#!/usr/bin/env python3

import os
import argparse
import subprocess

def apply():
    homedir = os.path.abspath(os.curdir)
    config_file = os.path.join(homedir, "lambdabot_config.json")
    os.chdir("terraform/dev/ssm_parameter_store")
    print(subprocess.check_call(["terraform", "apply", "-var-file", config_file]))
    os.chdir(homedir)
    os.chdir("terraform/dev/lambda")
    print(subprocess.check_call(["terraform", "apply", "-var-file", config_file]))
    os.chdir(homedir)
    os.chdir("terraform/dev/api_gateway")
    print(subprocess.check_call(["terraform", "apply", "-var-file", config_file]))
    os.chdir(homedir)


def destroy():
    homedir = os.path.abspath(os.curdir)
    config_file = os.path.join(homedir, "lambdabot_config.json")
    os.chdir("terraform/dev/ssm_parameter_store")
    print(subprocess.check_call(["terraform", "destroy", "-var-file", config_file, "-f"]))
    os.chdir(homedir)
    os.chdir("terraform/dev/lambda")
    print(subprocess.check_call(["terraform", "destroy", "-var-file", config_file, "-f"]))
    os.chdir(homedir)
    os.chdir("terraform/dev/api_gateway")
    print(subprocess.check_call(["terraform", "destroy", "-var-file", config_file, "-f"]))
    os.chdir(homedir)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', help='deploy lambdabot', action='store_true')
    parser.add_argument('--destroy', help='destroy lambdabot',  action='store_true')
    args = parser.parse_args()
    if args.apply:
        apply()
    if args.destroy:
        destroy()


if __name__ == '__main__':
    main()
