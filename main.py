# Helpful read:
# https://bulbapedia.bulbagarden.net/wiki/Save_data_structure_(Generation_I)

import sys
with open(sys.argv[1], 'rb+') as f:
    sav = bytearray(f.read())
    sav[0x2f56] = 0xfb # Party slot 1 Attack and Defense DVs
    sav[0x2f57] = 0xdf # Party slot 1 Speed and Special DVs

    checksum = 0xff
    for c in sav[0x2598:0x352A]:
        checksum -= c
    sav[0x352A] = checksum & 0xff
    f.seek(0)
    f.write(sav)
    print(f"Checksum updated: {hex(sav[0x352A])}")
