#!/usr/bin/env python3

import os
from os.path import join as pjoin
import argparse
import json
import subprocess

from jinja2 import Template


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOT_TEMPLATE_PATH = pjoin(BASE_DIR, 'graph.dot.jinja2')
HTML_TEMPLATE_PATH = pjoin(BASE_DIR, 'page.html.jinja2')


def read_file(fpath):
    with open(fpath) as fp:
        return fp.read()


def write_file(fpath, s):
    with open(fpath, 'w') as fp:
        fp.write(s)


REDUCTION_TYPES = {
    "polytime": "P",
    "logspace": "L",
}


def process_vertices(vertices):
    for vid, vinfo in vertices.items():
        vinfo['id'] = vid


def process_edges(vertices, edges):
    for i, edge in enumerate(edges):
        edge['id'] = i + 1
        if edge.get('type') is None:
            edge['type'] = 'polytime'
        if edge['type'] not in REDUCTION_TYPES:
            raise ValueError('reduction type should be one of ' + list(REDUCTION_TYPES.keys()))
        edge['typechar'] = REDUCTION_TYPES[edge['type']]

        edge['from'] = vertices[edge['from']]
        edge['to'] = vertices[edge['to']]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('vertices_file')
    parser.add_argument('edges_file')
    parser.add_argument('out_dir')
    args = parser.parse_args()

    vertices = json.loads(read_file(args.vertices_file))
    process_vertices(vertices)
    edges = json.loads(read_file(args.edges_file))
    process_edges(vertices, edges)
    dot_template = Template(read_file(DOT_TEMPLATE_PATH))
    dot_graph = dot_template.render({'vertices': vertices, 'edges': edges})

    os.makedirs(args.out_dir, exist_ok=True)
    dot_path = pjoin(args.out_dir, 'graph.dot')
    svg_path = pjoin(args.out_dir, 'graph.svg')
    write_file(dot_path, dot_graph)
    subprocess.check_call(['dot', '-Tsvg', dot_path, '-o', svg_path])

    html_template = Template(read_file(HTML_TEMPLATE_PATH), trim_blocks=True, lstrip_blocks=True)
    html = html_template.render({'vertices': vertices, 'edges': edges, 'svg': read_file(svg_path)})
    write_file(pjoin(args.out_dir, 'index.html'), html)
    os.remove(svg_path)


if __name__ == '__main__':
    main()
