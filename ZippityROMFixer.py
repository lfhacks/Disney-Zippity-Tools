#LeapFrog Disney Zippity ROM fixer
from codingTools import *

#Open the ROM file
ROM = dialogs.file()

#Create the output directory
outDir = fileTools.outputDirectory(ROM)

#Get the size of the ROM file
size = fileTools.size(ROM)

#Open the ROM
with open(ROM, "rb") as rom:
    #The ROM contents minus the padding will get stored in this bytearray
    data = bytearray() 

    try:
        while rom.tell() < size: #This gets looped until the end of the file
            #Extend the data bytearray with 0x200 bytes
            data.extend(rom.read(0x200))
            
            #Skip the 16 bytes of padding that follows
            rom.seek(16, 1)
    except EOFError:
        #In case there ever somehow happens to be an end of file error
        print("EOF")

    #Write the fixed ROM
    fileTools.writeNewBinaryFile(outDir + "FAT16-IMAGE.img", data)
