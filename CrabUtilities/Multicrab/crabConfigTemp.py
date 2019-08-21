from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import getUsernameFromSiteDB
config = Configuration()

workname='monoH_2016_20190730'
reqname='MonoHbb_ZpBaryonic_MZp-1000_MChi-1_13TeV-madgraph_MC25ns_LegacyMC_20170328'
dataset='/MonoHbb_ZpBaryonic_MZp-1000_MChi-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'

config.section_("General")
config.General.requestName = reqname
config.General.workArea = 'crab_'+workname
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'treeMaker_Summer16_cfg.py'
#config.JobType.maxMemoryMB = 2400
#config.JobType.maxJobRuntimeMin = 2750
config.JobType.inputFiles = ['effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt','effAreasMuons_cone03_Spring15_25ns.txt',
'../../TreeMaker/data/model-18.data-00000-of-00001',
'../../TreeMaker/data/model-18.meta',
'../../TreeMaker/data/model-18.index',
'../../TreeMaker/data/model-18.pb',
'../../TreeMaker/data/BoostedSVDoubleCA15_withSubjet_v4.weights.xml',
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
'Summer16_23Sep2016V3_MC_L1FastJet_AK4PFchs.txt'
]
config.JobType.sendExternalFolder = True
config.JobType.sendPythonFolder   = True
config.section_("Data")
config.Data.inputDataset = dataset
config.Data.inputDBS = 'global'
#config.Data.splitting = 'Automatic'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 10000
config.Data.publication = False

config.JobType.allowUndistributedCMSSW=True

config.section_("Site")
config.Site.storageSite = "T2_CH_CERN"
config.Data.outputDatasetTag = reqname
config.Data.outLFNDirBase = '/store/group/phys_exotica/bbMET/monoH_2016_ntuples_24July/ZPSamples/%s' %(workname)
