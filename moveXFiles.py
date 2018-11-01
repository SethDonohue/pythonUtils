print ('Moving Files...')

import shutil
import os
source = 'D:\\Seth\\Photos and Video\\2016\\2-21-16 Tasmania x\\Video\\GoPro'
destination = 'D:\\Seth\\Photos and Video\\2016\\2-21-16 Tasmania x\\Video\\summary'

print(source)

files = os.listdir(source)

for f in files:
	if "x" in f:
		shutil.move(source + "/" + f, destination)
		print(f, ' moved')
	else:
		print(f, ' not moved')
