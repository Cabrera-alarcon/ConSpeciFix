import os

for f in os.listdir('/path/to/sets/to/run'):
	try:
		os.system('python runner.py '+f)
	except:
		print 'error! '+str(f)