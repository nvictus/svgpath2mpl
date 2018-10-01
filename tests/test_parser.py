import matplotlib as mpl
import matplotlib.pyplot as plt
from svgpath2mpl import parse_path


PATH_DATA = {
    'triangle01': {
        'd': "M 100 100 L 300 100 L 200 300 z",
        'fill': "red",
        'stroke': "blue",
        'stroke-width': 3,
    },

    'cubic01': {
        'd': "M100,200 C100,100 250,100 250,200 S400,300 400,200",
        'fill': "none",
        'stroke': "red",
        'stroke-width': 5,
    },

    'quad01a': {
        'd': "M200,300 Q400,50 600,300 T1000,300",
        'fill': "none",
        'stroke': "red",
        'stroke-width': 5,
    },

    'quad01b': {
        'd': "M200,300 L400,50 L600,300 L800,550 L1000,300",
        'fill': "none",
        'stroke': "#888888",
        'stroke-width': 2,
    },

    'arcs01a': {
        'd': "M300,200 h-150 a150,150 0 1,0 150,-150 z",
        'fill': "red",
        'stroke': "blue",
        'stroke-width': 5,
    },

    'arcs01b': {
        'd': "M275,175 v-150 a150,150 0 0,0 -150,150 z",
        'fill': "yellow",
        'stroke': "blue",
        'stroke-width': 5,
    },

    'arcs01c': {
        'd': "M600,350 l 50,-25 a25,25 -30 0,1 50,-25 l 50,-25 "
             "a25,50 -30 0,1 50,-25 l 50,-25 "
             "a25,75 -30 0,1 50,-25 l 50,-25 "
             "a25,100 -30 0,1 50,-25 l 50,-25",
        'fill': "none",
        'stroke': "red",
        'stroke-width': 5,
    },

    'arcs02': {
        'd': "M 125,75 a100,50 0 ?,? 100,50",
        'fill': "none",
        'stroke': "red",
        'stroke-width': 6,
    },
}


def test_parse_path():
    d = "M300,200 h-150 a150,150 0 1,0 150,-150 z"
    fill = "red"
    stroke = "blue"
    stroke_width = 5

    path = parse_path(d)
    patch = mpl.patches.PathPatch(path, facecolor=fill, edgecolor=stroke, linewidth=stroke_width)

    fig = plt.figure(figsize=(12, 5.25))
    ax = fig.add_subplot(111)
    ax.add_patch(patch)
    ax.set_aspect(1)
    ax.set_xlim([0, 1200])
    ax.set_ylim([0, 400])

