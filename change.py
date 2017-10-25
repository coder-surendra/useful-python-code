# this file changes the name of every file, whose name starts with "string", in folder
import os

for filename in os.listdir('.'):
# 	let's say, we wanna change names files, who name starts with 'IMG', and remove the 'IMG' content
	if filename.startswith('IMG'):
# 		we 
		newName = ''+ filename[11:]
		os.rename(filename,newName)
