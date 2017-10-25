import os
for filename in os.listdir('.'):
	if filename.startswith('_Ohys-Raws_'):
		newName = '[Ohys-Raws]'+ filename[11:]
		os.rename(filename,newName)