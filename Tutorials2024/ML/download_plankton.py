import os

files = ['https://darchive.mblwhoilibrary.org/bitstream/handle/1912/7342/2006.zip', 'https://darchive.mblwhoilibrary.org/bitstream/handle/1912/7343/2007.zip', 'https://darchive.mblwhoilibrary.org/bitstream/handle/1912/7345/2008.zip', 'https://darchive.mblwhoilibrary.org/bitstream/handle/1912/7346/2009.zip', 'https://darchive.mblwhoilibrary.org/bitstream/handle/1912/7348/2010.zip', 'https://darchive.mblwhoilibrary.org/bitstream/handle/1912/7347/2011.zip', 'https://darchive.mblwhoilibrary.org/bitstream/handle/1912/7344/2012.zip', 'https://darchive.mblwhoilibrary.org/bitstream/handle/1912/7349/2013.zip']

for f in [files[0]]:
    cmd = 'wget ' + f
    os.system(cmd)