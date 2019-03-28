import os
import glob
path = 'Files/*txt'

files = glob.glob(path)

dryrun=True

for file in files:
	fout = open('crabConf.py','w')
	temp_file=open('crabConf_temp','r')
        txtFile=file.split('/')[-1]
        strtag=txtFile.replace('.txt','')
       for line in temp_file:
		if 'datastr' in line:
			newLine = line.replace('datastr',strtag)
                        fout.write(newLine)
		elif 'testFile' in line:
			newLine = line.replace('testFile',""+"'"+"Files/"+txtFile+"'")
			fout.write(newLine)
		else:
			fout.write(line) 
        fout.close()
	if dryrun:
                print ("+++++++++++++++++++++++++"+"\n")
                print ("checking dryrun  for the txtfile"+txtFile+"\n")
		os.system('crab submit -c '+fout+' '+'--dryrun')
	else:
		print ("+++++++++++++++++++++++++"+"\n")
                print ("subming crab jobs for the txtfile"+txtFile+"\n")
		os.system('crab submit -c '+fout+' '+'--dryrun')

