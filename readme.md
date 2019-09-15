# Web of Reductions

A script which generates a directed graph where vertices are problems
and there is an edge from problem A to problem B iff A reduces to B
in polynomial time (or logarithmic space).

### How to run

First you must install `jinja2` (`pip install jinja2`) and `graphviz`.

The graph is specified in `vertices.json` and `edges.json`. So run

    python3 make-web.py vertices.json edges.json output

to generate output in a directory named `output`.
This directory contains:

* `graph.dot`: representation of the graph in the
<a href="https://en.wikipedia.org/wiki/DOT_(graph_description_language)">dot</a>
file format.
* `index.html`: HTML page containing the graph in SVG and links/references to reduction proofs.

### How to contribute

If you want to add a problem or reduction:

* Make an entry in `vertices.json` or `edges.json`.
* Run `make-web.py` to check if your changes are displayed correctly.
* Send me a pull request. I'll review, merge and deploy your changes.
