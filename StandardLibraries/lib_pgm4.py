# Common data archiving and compression formats are directly supported by modules 
# including: zlib, gzip, bz2, lzma, zipfile and tarfile.

import zlib
s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))
print(t)

print(zlib.decompress(t))

print(zlib.crc32(s))
