import struct
from os import path
from typing import IO


class MinecraftDatapacksEditorsExplanationFile:
    file_path: str
    file_data: bytes = b''
    project_name: str = 'MyProject'
    file_version: int = 1

    def __init__(self, file_path: str):
        self.file_path = file_path
        if path.exists(self.file_path):
            with open(self.file_path, "rb") as fp:
                self.file_data = fp.read()
            self.__get_data()
        else:
            self.__init_file()
            self.__write_into()

    def __init_file(self):
        data = self.project_name.encode("utf-8")
        self.file_data += struct.pack(">ii", self.file_version, len(data))
        self.file_data += data

    def __write_into(self):
        file_stream = open(self.file_path, "wb")
        file_stream.write(self.file_data)
        file_stream.close()

    def __get_data(self):
        self.file_version, name_length = struct.unpack(">ii", self.file_data[0:8])
        self.project_name = self.file_data[8: name_length + 9].decode("utf-8")

    def save(self):
        self.file_data = b''
        self.__init_file()
        self.__write_into()


if __name__ == "__main__":
    demo_file = MinecraftDatapacksEditorsExplanationFile("MyProject.mcde")
    print(demo_file.project_name)
    print(demo_file.file_version)
