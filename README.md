# Disney-Zippity-Tools
Tools for handling Disney Zippity game data

The ROM fixer takes an input Zippity ROM dump and removes the 16 bytes of padding that shows up every 0x200 bytes

The sound package unpacker takes a wavs container (for example, mca_wavs.bin from Cars) and outputs the embedded DRM files with a txth file for playback with VGMStream
