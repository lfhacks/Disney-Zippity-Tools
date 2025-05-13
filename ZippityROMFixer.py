#LeapFrog Disney Zippity ROM fixer
from codingTools import *

ROM = dialogs.file()
outDir = fileTools.outputDirectory(ROM)
size = fileTools.size(ROM)

with open(ROM, "rb") as rom:
    data = bytearray()

    try:
        while rom.tell() < size:
            data.extend(rom.read(0x200))
            rom.seek(16, 1)
    except EOFError:
        print("EOF")

    #Write the fixed ROM
    fileTools.writeNewBinaryFile(outDir + "FAT16-IMAGE.img", data)
