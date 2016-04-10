svgpath2mpl
===========

Parse SVG paths into matplotlib ``Path`` objects for plotting.

A path in SVG is defined by a 'path' element which contains a d="(path data)" attribute, where the ``d`` attribute contains the moveto, line, curve (both cubic and quadratic Béziers), arc and closepath instructions. Matplotlib actually supports all of these instructions natively but doesn't provide a parser.

Based on:

1. `svg_parse <https://github.com/rougier/LinuxMag-HS-2014/blob/master/matplotlib/firefox>`_ for matplotlib by Nicolas P. Rougier (BSD license).

2. `svg.path <https://github.com/regebro/svg.path>`_ by Lennart Regebro (MIT license).

I basically added the missing path commands from (1), including smooth curves and endpoint-parameterized elliptical arcs.

	>>> from svgpath2mpl import parse_path
	>>> parse_path('M 100 100 L 300 100')
	Path(array([[ 100.,  100.], [ 300.,  100.]]), array([1, 2], dtype=uint8))


Resources
---------
See the `SVG Specification <https://www.w3.org/TR/SVG/paths.html>`_.

See the matplotlib path `tutorial <http://matplotlib.org/users/path_tutorial.html>`_ and `API docs <http://matplotlib.org/1.2.1/api/path_api.html>`_.


License
-------

MIT