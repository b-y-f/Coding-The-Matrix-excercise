# Copyright 2013 Philip N. Klein
# additions 2015 Iain Coghill
"""
This file contains a simple plotting interface, which uses a browser with SVG to
present a plot of points represented as either complex numbers or 2-vectors.
"""

import webbrowser
from numbers import Number

import tempfile
import os
import atexit

_browser = None

def plot(L, scale=4, dot_size = 3, browser=None):
    """ plot takes a list of points, optionally a scale (relative to a 200x200 frame),
        optionally a dot size (diameter) in pixels, and optionally a browser name.
        If running within an ipython notebook and no explicit browser given, then
        it returns an SVG plot directly to the notebook. Otherwise it produces an
        html file with the SVG plot, opens the file in a web browser, and returns nothing.
    """

    svg = plot2svg(L, scale, dot_size)


    return svg2ipynb(svg)

def svg2html(svg, browser):
    """ svg2html takes an svg document, wraps it in a temporary html
        file, and opens the file in a web browser.
    """
    hpath = create_temp('.html')
    with open(hpath, 'w') as h:
        h.writelines(
            ['<!DOCTYPE html>\n'
            ,'<head>\n'
            ,'<title>plot</title>\n'
            ,'</head>\n'
            ,'<body>\n'
            ,svg
            ,'\n</body>\n'
            ,'</html>'])
    webbrowser.get(browser).open('file://%s' % hpath)

def svg2ipynb(svg):
    """ svg2ipynb takes an svg document and displays it directly into
        the current ipython notebook.
    """
    from IPython.display import SVG
    return SVG(svg)

def plot2svg(L, scale, dot_size):
    """ plot2svg takes a list of points, a scale (relative to a 200x200 frame),
        and a dot size (diameter) in pixels.
        It produces an SVG document representing the given plot as a string.
    """
    import xml.etree.ElementTree as ET

    scalar = 200./scale
    origin = (210, 210)
    svg = ET.Element('svg', xmlns="http://www.w3.org/2000/svg", version="1.1",
                    height="420", width="420")
    # axis
    ET.SubElement(svg,"line",
                  x1="0", y1="210", x2="420", y2="210",
                  style="stroke:rgb(0,0,0);stroke-width:2")
    ET.SubElement(svg,"line",
                  x1="210", y1="0", x2="210", y2="420",
                  style="stroke:rgb(0,0,0);stroke-width:2")
    for pt in L:
        if isinstance(pt, Number):
            x,y = pt.real, pt.imag
        else:
            if isinstance(pt, tuple) or isinstance(pt, list):
                x,y = pt
            else:
                raise ValueError
        ET.SubElement(svg, "circle",
                        cx="%d" %(origin[0]+scalar*x),
                        cy="%d" %(origin[1]-scalar*y),
                        r="%d" %dot_size,
                        fill="red")
    return ET.tostring(svg, encoding="unicode")


def setbrowser(browser=None):
    """ Registers the given browser and saves it as the module default.
        This is used to control which browser is used to display the plot.
        The argument should be a value that can be passed to webbrowser.get()
        to obtain a browser.  If no argument is given, the default is reset
        to the system default.
        webbrowser provides some predefined browser names, including:
        'firefox'
        'opera'
        If the browser string contains '%s', it is interpreted as a literal
        browser command line.  The URL will be substituted for '%s' in the command.
        For example:
        'google-chrome %s'
        'cmd "start iexplore.exe %s"'
        See the webbrowser documentation for more detailed information.
        Note: Safari does not reliably work with the webbrowser module,
        so we recommend using a different browser.
    """
    global _browser
    if browser is None:
        _browser = None  # Use system default
    else:
        webbrowser.register(browser, None, webbrowser.get(browser))
        _browser = browser

def getbrowser():
    """ Returns the module's default browser """
    return _browser

# Create a temporary file that will be removed at exit
# Returns a path to the file
def create_temp(suffix='', prefix='tmp', dir=None):
    _f, path = tempfile.mkstemp(suffix, prefix, dir)
    os.close(_f)
    remove_at_exit(path)
    return path

# Register a file to be removed at exit
def remove_at_exit(path):
    atexit.register(os.remove, path)