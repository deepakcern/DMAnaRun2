""" In CRAB3 the configuration file is in Python language. It consists of creating a Configuration object imported from the WMCore library: """
from WMCore.Configuration import Configuration
config = Configuration()

"""  Once the Configuration object is created, it is possible to add new sections into it with corresponding parameters."""

workname='DATA'
reqname='scalar_NLO_Mchi-450_Mphi-1000'
dataset='/BBbarDMJets_scalar_NLO_Mchi-450_Mphi-1000_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'

PERIOD='H'
EPLS=20


config.section_("General")
config.General.requestName = reqname
config.General.workArea = 'crab_'+workname
config.General.transferOutputs = True
config.General.transferLogs = True

DATAJEC='Summer16_23Sep2016'+PERIOD+'V3_DATA'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'treeMaker_Summer16_cfg.py'
config.JobType.pyCfgParams = ['runOnMC=False','period='+PERIOD]
config.JobType.inputFiles = ['effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt','effAreasMuons_cone03_Spring15_25ns.txt',
'../../TreeMaker/data/model-18.data-00000-of-00001',
'../../TreeMaker/data/model-18.meta',
'../../TreeMaker/data/model-18.index',
'../../TreeMaker/data/model-18.pb',
'../../TreeMaker/data/BoostedSVDoubleCA15_withSubjet_v4.weights.xml',
DATAJEC+'_Uncertainty_AK8PFchs.txt',
DATAJEC+'_Uncertainty_AK8PFPuppi.txt',
DATAJEC+'_Uncertainty_AK4PFchs.txt',
DATAJEC+'_L3Absolute_AK8PFchs.txt',
DATAJEC+'_L3Absolute_AK8PFPuppi.txt',
DATAJEC+'_L3Absolute_AK4PFchs.txt',
DATAJEC+'_L2Relative_AK8PFchs.txt',
DATAJEC+'_L2Relative_AK8PFPuppi.txt',
DATAJEC+'_L2Relative_AK4PFchs.txt',
DATAJEC+'_L1RC_AK8PFchs.txt',
DATAJEC+'_L1RC_AK4PFchs.txt',
DATAJEC+'_L1FastJet_AK8PFchs.txt',
DATAJEC+'_L1FastJet_AK8PFPuppi.txt',
DATAJEC+'_L1FastJet_AK4PFchs.txt',
DATAJEC+'_L2L3Residual_AK8PFchs.txt',
DATAJEC+'_L2L3Residual_AK8PFPuppi.txt',
DATAJEC+'_L2L3Residual_AK4PFchs.txt']


config.JobType.sendExternalFolder = True
config.JobType.sendPythonFolder = True

config.section_("Data")
config.Data.inputDataset = dataset
config.Data.inputDBS = 'global'
config.Data.outputDatasetTag = reqname
config.Data.splitting = 'LumiBased'
#config.Data.splitting = 'Automatic'

config.Data.unitsPerJob = 20 #EPLS

#config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
config.Data.lumiMask = 'Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'#'Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
#config.Data.ignoreLocality = True


config.JobType.allowUndistributedCMSSW=True


#maxtarballsize = 50 
config.section_("Site")
#config.Site.storageSite = "T3_TW_NCU"
config.Site.storageSite = "T2_CH_CERN"
##config.Site.storageSite = "T2_US_Wisconsin"                                                         
#config.Site.storageSite = "T2_TW_NCHC"                                                               

config.Data.outLFNDirBase = '/store/group/phys_exotica/bbMET/monoH_2016_ntuples_20Aug/DATA' 
