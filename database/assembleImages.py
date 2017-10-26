from config import *
import os

species = getAllSpecies()

for sp in species:
	os.system('convert -verbose -density 150 -trim '+PATH_TO_OUTPUT+sp+'/Distrib.pdf -quality 100 -flatten -sharpen 0x1.0 '+PATH_TO_OUTPUT+sp+'/Distrib.png')
	os.system('convert -verbose -density 150 -trim '+PATH_TO_OUTPUT+sp+'/gno1.pdf -quality 100 -flatten -sharpen 0x1.0 '+PATH_TO_OUTPUT+sp+'/gno1.png')
	os.system('convert -verbose -density 150 -trim '+PATH_TO_OUTPUT+sp+'/kmeans.pdf -quality 100 -flatten -sharpen 0x1.0 '+PATH_TO_OUTPUT+sp+'/kmeans.png')
	os.system('convert '+PATH_TO_OUTPUT+sp+'/Distrib.png '+PATH_TO_OUTPUT+sp+'/gno1.png  +append '+PATH_TO_OUTPUT+sp+'/tmp.png')
	os.system('convert '+PATH_TO_OUTPUT+sp+'/tmp.png '+PATH_TO_OUTPUT+sp+'/kmeans.png  +append '+PATH_TO_OUTPUT+sp+'/combine.png')
	os.system('rm '+PATH_TO_OUTPUT+sp+'/tmp.png')

i = 0
perPage = 4
while i < len(species):
	command = 'convert '
	for z in range(min(perPage,len(species)-i)):
		command += PATH_TO_OUTPUT+species[i+z]+'/combine.png '
	command+=' -append /Volumes/ITDR/brian/figures/gno'+str(int(i/perPage)+1)+'.png'
	os.system(command)
	i +=perPage
