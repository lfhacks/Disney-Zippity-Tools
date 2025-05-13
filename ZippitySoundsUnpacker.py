#(short name)_wavs.bin unpacker for LeapFrog Disney Zippity games
from codingTools import *
wavsBinary = dialogs.file() #Prompt user to open a file
outDir = fileTools.outputDirectory(wavsBinary) #Generate the output directory
txth = """codec = IMA                 
sample_rate = @0x10$4
channels = 1
start_offset = 0x28
num_samples = @0x14"""
fileTools.writeNewTextFile(outDir+".ALP.txth", txth)

with open(wavsBinary, "rb") as wavs:
    fileCount = LE_unpack.uint(wavs.read(4))
    for fileIndex in range(fileCount):
        fileOffset, fileSize = LE_multiunpack.uint(wavs.read(8))
        
        #Save offset so we can return later
        last = wavs.tell() 
        
        #Go to and get the data
        wavs.seek(fileOffset) 
        fileData = wavs.read(fileSize)

        #Save the data
        fileTools.writeNewBinaryFile(outDir+f'{fileIndex:04}.alp', fileData)

        #Return to saved offset
        wavs.seek(last) 
