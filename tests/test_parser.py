import matplotlib as mpl
import matplotlib.pyplot as plt
from svgpath2mpl import parse_path


def test_parse_path():
    d = "M300,200 h-150 a150,150 0 1,0 150,-150 z"
    fill = "red"
    stroke = "blue"
    stroke_width = 5

    path = parse_path(d)
    patch = mpl.patches.PathPatch(
        path, facecolor=fill, edgecolor=stroke, linewidth=stroke_width
    )

    fig = plt.figure(figsize=(12, 5.25))
    ax = fig.add_subplot(111)
    ax.add_patch(patch)
    ax.set_aspect(1)
    ax.set_xlim([0, 1200])
    ax.set_ylim([0, 400])
