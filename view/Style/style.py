import xml.etree.ElementTree as xml
import os


class Style:
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

        color_names = []
        count = 0
        for i in self.root.iter('key'):
            if count % 6 == 0:
                color_names.append(i.text)
            count += 1

        self.color_values = []
        count = 0
        for i in self.root.iter('real'):
            if count % 4 != 0:
                self.color_values.append(i.text)
            count += 1

        count = 0
        self.color_hash = dict()
        for i in color_names:
            self.color_hash[i] = [
                self.color_values[count],
                self.color_values[count + 1],
                self.color_values[count + 2],
            ]

            count += 3

