"""
 Author : wzpMC
 Date:   2022/1/22
 Time:   11:52
"""
import xml.sax


class mcdeFile:
    fileContent: str = None

    def __init__(self, filepath=None, fp=None):
        """
        to make a mcdeFile Object
        :param filepath: the path of the file
        :param fp:the file object of the file
        """
        if filepath is None:
            with open(filepath, "r") as fp:
                fileContent = fp.read()
        elif fp is None:
            fileContent = fp.read()
        else:
            raise FileNotFoundError
