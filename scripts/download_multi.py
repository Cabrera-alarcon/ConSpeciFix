from multiprocessing import Pool
import multiprocessing
import os
from config import *

def downloadFile(args):
	commands = args.strip('\n').split('\t');
	for com in commands:
		os.system(com)
	

if __name__ == '__main__':
	species = getSpecies()
	print multiprocessing.cpu_count()
	p = Pool(MAX_THREADS)
	f = open('todo/download.txt','r')
	args = []
	for l in giveMulti(f.readlines()):
		args.append(l)
	p.map(downloadFile,args)
	