#!/usr/bin/env python3
"""
This script pulls the nerd font spec from their repo on github,
then generates a python version of it.

Much of this script was inspired by fontawesome-python:
https://github.com/justbuchanan/fontawesome-python
Which was inspired by fontawesome-markdown:
https://github.com/bmcorser/fontawesome-markdown/blob/master/scripts/update_icon_list.py
"""

import sys

import requests

INDENT = " " * 4

def add_icon(out, icon_name, icon):
    # dict entry with character code
    entry = f"'{icon_name}': '\\U{icon['code'].zfill(8)}',"
    indent_to = 80 - 10 - len(INDENT)
    entry += " " * (indent_to - len(entry))  # pad
    # comment with nerd font icon
    entry += f"# {icon['char']}"

    out.write(INDENT + entry + "\n")

def main(uri, version):
    icons_dict = requests.get(uri).json()
    meta_data = icons_dict.pop("METADATA", {})
    site = meta_data.get(
        "development-website", "https://github.com/ryanoasis/nerd-fonts"
    )
    version = meta_data.get("version", version)

    out = sys.stdout

    out.write("# -*- coding: utf-8 -*-\n")
    out.write("# This file was generated automatically by nerdfont-python\n")
    out.write(f"# It contains the icon set from: {site}\n")
    out.write("\n")
    out.write(f"__version__ = '{version}'\n")
    out.write("\n")
    out.write("icons = {\n")
    for icon_name, icon in icons_dict.items():
        add_icon(out, icon_name, icon)
        # Nerd font displays an extra `nf-` prefix in
        # https://www.nerdfonts.com/cheat-sheet
        add_icon(out, f"nf-{icon_name}", icon)

    out.write("}\n")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate icons.py, containing a python mapping for nerd font icons"
    )
    parser.add_argument(
        "--revision",
        help="Nerd font version to use. Should correspond to a git branch name.",
        default="master",
    )
    args = parser.parse_args()

    REVISION = args.revision
    URI = (
        "https://raw.githubusercontent.com"
        "/ryanoasis/nerd-fonts/%s/glyphnames.json" % REVISION
    )

    main(URI, args.revision)
