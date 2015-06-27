import os

## check if file exist then ask if you want to delete old one and create new one. 
## if answer is yes then deelte the old and create this one new. 
fout = open("datasetdetails_Spring15.txt","w")
## each line will contain four parameters. 
## taskname   cfg.py  datasetname  numberofdiles
## cfg.py is configurable because data and MC will have different configurations.
## And number of files canbe used as number of lumis in that case. 

fout.write("WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8 treeMaker_Spring15_cfg.py /WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/MINIAODSIM 1 \n")

fout.write("DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8 treeMaker_Spring15_cfg.py /DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3/MINIAODSIM 1 \n")

fout.write("TT_TuneCUETP8M1_13TeV-powheg-pythia8 treeMaker_Spring15_cfg.py /TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v4/MINIAODSIM 1 \n")

fout.write("TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 treeMaker_Spring15_cfg.py /TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/MINIAODSIM 1 \n")


f = open('datasetdetails_Spring15.txt','r')
for line in f:
    print line
    a=[]
    b=[]
    c=[]
    d=[]
    a,b,c,d = line.split()
    datasetdetail=[a,b,c,d]
    print datasetdetail
    os.system('crab submit General.requestName='+datasetdetail[0]+' JobType.psetName='+datasetdetail[1]+' Data.inputDataset='+datasetdetail[2]+' Data.unitsPerJob='+datasetdetail[3])
    #name =  'crab submit General.requestName='+datasetdetail[0]+' JobType.psetName='+datasetdetail[1]+' Data.inputDataset='+datasetdetail[2]+' Data.unitsPerJob='+datasetdetail[3]
    #print name 

