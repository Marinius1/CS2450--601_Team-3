import xml.etree.ElementTree as xml
import os
from collections import namedtuple
import math


class Color:
    """
    class to encapsulate the color config data. will take a color scheme as input
    and populate the values based on what is in the file. will likely utilize
    something close to the itermcolor format because it is well defined
    """

    def __init__(self, scheme: str = "Gruvbox Dark"):
        """
        init(config: str): void
        load the correct color config file, assign values to pre-determined constants
        """

        # change working directory to local file location
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        self.scheme = scheme
        self.scheme_path = "./thirdparty/iTerm2-Color-Schemes/schemes" \
                           "/" + self.scheme + ".itermcolors"

        self.tree = xml.parse(self.scheme_path)
        self.root = self.tree.getroot()

        self.colors = self.load_color_config()

    def load_color_config(self):
        """
        load itermcolor xml file, parse, convert to hex strings, and return
        namedtuple with all color data from itermcolor file
        """

        color_names = []
        count = 0
        for i in self.root.iter('key'):
            if not count % 6:
                color_names.append(i.text)
            count += 1

        color_values = []
        count = 0
        for i in self.root.iter('real'):
            if count % 4 != 0:
                color_values.append(math.floor(float(i.text) * 255))
            count += 1

        color_values = [
            color_values[x:x + 3] for x in range(0, len(color_values), 3)
        ]

        # convert rgb tuples to hex strings
        color_hex = []
        for i in color_values:
            rgb_tuple = (int(i[0]), int(i[1]), int(i[2]))
            hex_color = '#%02x%02x%02x' % rgb_tuple
            color_hex.append(hex_color)

        color_pairs = list(zip(color_names, color_values))

        color_mux = {
            'Ansi 0 Color': "a0",
            'Ansi 1 Color': "a1",
            'Ansi 2 Color': "a2",
            'Ansi 3 Color': "a3",
            'Ansi 4 Color': "a4",
            'Ansi 5 Color': "a5",
            'Ansi 6 Color': "a6",
            'Ansi 7 Color': "a7",
            'Ansi 8 Color': "a8",
            'Ansi 9 Color': "a9",
            'Ansi 10 Color': "a10",
            'Ansi 11 Color': "a11",
            'Ansi 12 Color': "a12",
            'Ansi 13 Color': "a13",
            'Ansi 14 Color': "a14",
            'Ansi 15 Color': "a15",
            'Background Color': "background",
            'Badge Color': "badge",
            'Bold Color': "bold",
            'Cursor Color': "cursor",
            'Cursor Guide Color': "cursor_guide",
            'Cursor Text Color': "cursor_text",
            'Foreground Color': "foreground",
            'Link Color': "link",
            'Selected Text Color': "selected_text",
            'Selection Color': "selection"
        }

        # build shorter naming conventions using expanded names as a demux key
        color_keys = []
        for i in color_pairs:
            try:
                color_keys.append(color_mux[i[0]])
            except KeyError as e:
                print("::ERROR:: color demux failed")

        Colors = namedtuple('Colors', color_keys)

        return Colors(*color_hex)
