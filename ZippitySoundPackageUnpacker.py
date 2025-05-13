#(short name)_wavs.bin unpacker for LeapFrog Disney Zippity games
from codingTools import *

#Prompt user to open a file
wavsBinary = dialogs.file()

#Generate the output directory
outDir = fileTools.outputDirectory(wavsBinary)

#Create the TXTH file (used so VGMStream can play these)
txth = """codec = IMA                 
sample_rate = @0x10$4
channels = 1
start_offset = 0x28
num_samples = @0x14"""
fileTools.writeNewTextFile(outDir+".ALP.txth", txth)

#Open the WAVS binary for extraction
with open(wavsBinary, "rb") as wavs:
    #Get the file count
    fileCount = LE_unpack.uint(wavs.read(4))
    for fileIndex in range(fileCount):
        #Get the start offset and size of the file
        fileOffset, fileSize = LE_multiunpack.uint(wavs.read(8))
        
        #Save the current offset we're at in the table so we can return later
        last = wavs.tell() 
        
        #Go to and get the data
        wavs.seek(fileOffset) 
        fileData = wavs.read(fileSize)

        #Save the data
        fileTools.writeNewBinaryFile(outDir+f'{fileIndex:04}.alp', fileData)

        #Return to the saved table offset before next loop
        wavs.seek(last) 
