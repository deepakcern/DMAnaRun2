""" In CRAB3 the configuration file is in Python language. It consists of creating a Configuration object imported from the WMCore library: """
from WMCore.Configuration import Configuration
config = Configuration()
from CRABClient.UserUtilities import  getUsernameFromSiteDB


"""  Once the Configuration object is created, it is possible to add new sections into it with corresponding parameters."""

config.section_("General")
config.General.requestName = datastr
config.General.workArea = 'crab_20190323'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'treeMaker_Summer16_cfg.py'
config.JobType.inputFiles = ['effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt','effAreasMuons_cone03_Spring15_25ns.txt',
'../../MetaData/data/DNN_models/model-18.data-00000-of-00001',
'../../MetaData/data/DNN_models/model-18.meta',
'../../MetaData/data/DNN_models/model-18.index',
'../../MetaData/data/DNN_models/model-18.pb',
'../TreeMaker/data/BoostedSVDoubleCA15_withSubjet_v4.weights.xml',
'Summer16_23Sep2016V3_MC_Uncertainty_AK8PFchs.txt',
'Summer16_23Sep2016V3_MC_Uncertainty_AK8PFPuppi.txt',
'Summer16_23Sep2016V3_MC_Uncertainty_AK4PFchs.txt',
'Summer16_23Sep2016V3_MC_L3Absolute_AK8PFchs.txt',
'Summer16_23Sep2016V3_MC_L3Absolute_AK8PFPuppi.txt',
'Summer16_23Sep2016V3_MC_L3Absolute_AK4PFchs.txt',
'Summer16_23Sep2016V3_MC_L2Relative_AK8PFchs.txt',
'Summer16_23Sep2016V3_MC_L2Relative_AK8PFPuppi.txt',
'Summer16_23Sep2016V3_MC_L2Relative_AK4PFchs.txt',
'Summer16_23Sep2016V3_MC_L2L3Residual_AK8PFchs.txt',
'Summer16_23Sep2016V3_MC_L2L3Residual_AK8PFPuppi.txt',
'Summer16_23Sep2016V3_MC_L2L3Residual_AK4PFchs.txt',
'Summer16_23Sep2016V3_MC_L1RC_AK8PFchs.txt',
'Summer16_23Sep2016V3_MC_L1RC_AK4PFchs.txt',
'Summer16_23Sep2016V3_MC_L1FastJet_AK8PFchs.txt',
'Summer16_23Sep2016V3_MC_L1FastJet_AK8PFPuppi.txt',
'Summer16_23Sep2016V3_MC_L1FastJet_AK4PFchs.txt']
config.JobType.sendExternalFolder      = True
config.JobType.sendPythonFolder        = True

config.section_("Data")
#config.Data.inputDataset = '/DYJetsToLL_M-50_HT-100to200_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
config.Data.userInputFiles=open(testFile).readlines()
#config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
##config.Data.outLFNDirBase = '/store/user/khurana/MonoH2016/V3/'
config.Data.outputPrimaryDatase = '2HDMa_2016Signal'
config.Data.publication = False
#config.Data.ignoreLocality = True
#config.JobType.allowUndistributedCMSSW=True

workname='monoH_test'

config.section_("Site")
config.Site.storageSite = "T2_IN_TIFR"
#config.Site.storageSite = "T2_CH_CERN"
##config.Site.storageSite = "T2_US_Wisconsin"
#config.Site.storageSite = "T2_TW_NCHC"
config.Data.outLFNDirBase = '/store/user/%s/t3store2/%s' % (getUsernameFromSiteDB(), workname)
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
