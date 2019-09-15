# Web of Reductions

A script which generates a directed graph where vertices are problems
and there is an edge from problem A to problem B iff A reduces to B
in polynomial time (or logspace).

I plan to extend this to generate more than just a graph in SVG format.
Maybe I'll add pages with short descriptions of the problems
or links to external resources or graph-theoretic statistics.

The graph is specified in `vertices.json` and `edges.json`.
I first use [Jinja2](https://jinja.palletsprojects.com) to create a
<a href="https://en.wikipedia.org/wiki/DOT_(graph_description_language)">dot</a> file
and then run [graphviz](https://www.graphviz.org/) on it to get an SVG image.
