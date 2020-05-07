#!/usr/bin/env python

import sys
import requests
from os import environ


REPOS = [
    'diginc/pipenv-goodies',
    'diginc/debian-terraform-aws'
]


def main():
    for repo, repo_build_url in REPOS:
        build_url_key = repo.replace('/', '_').replace('-', '_')
        if environ.get(build_url_key) is not None:
            requests.post(environ.get(build_url_key))
        else:
            print("No build URL environment variable found:", build_url_key)
            sys.exit(1)


if __name__ == "__main__":
    main()
