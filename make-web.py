#!/usr/bin/env python3

import os
from os.path import join as pjoin
import argparse
import json
import subprocess

from jinja2 import Template


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOT_TEMPLATE_PATH = pjoin(BASE_DIR, 'graph.dot.jinja2')


def read_file(fpath):
    with open(fpath) as fp:
        return fp.read()


def write_file(fpath, s):
    with open(fpath, 'w') as fp:
        fp.write(s)


def validate():
    # validate reduction type in polytime and logspace
    pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('vertices_file')
    parser.add_argument('edges_file')
    parser.add_argument('out_dir')
    args = parser.parse_args()

    vertices = json.loads(read_file(args.vertices_file))
    edges = json.loads(read_file(args.edges_file))
    dot_template = Template(read_file(DOT_TEMPLATE_PATH))
    # trim_blocks=True, lstrip_blocks=True)
    dot_graph = dot_template.render({'vertices': vertices, 'edges': edges})

    os.makedirs(args.out_dir, exist_ok=True)
    dot_path = pjoin(args.out_dir, 'graph.dot')
    write_file(dot_path, dot_graph)
    subprocess.check_call(['dot', '-Tsvg', dot_path, '-o', pjoin(args.out_dir, 'graph.svg')])


if __name__ == '__main__':
    main()
