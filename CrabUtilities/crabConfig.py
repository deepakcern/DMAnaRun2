""" In CRAB3 the configuration file is in Python language. It consists of creating a Configuration object imported from the WMCore library: """
from WMCore.Configuration import Configuration
config = Configuration()

"""  Once the Configuration object is created, it is possible to add new sections into it with corresponding parameters."""

config.section_("General")
config.General.requestName = 'dihiggs'
config.General.workArea = 'crab_20151114'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = 'miniAODTreeMaker_MC_cfg.py'
config.JobType.psetName = 'MVA-And-PFUnCorrectedMET.py'
config.JobType.inputFiles = ['effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt','effAreasMuons_cone03_Spring15_25ns.txt',
                             'Summer15_25nsV6_MC_L1FastJet_AK4PFchs.txt',
                             'Summer15_25nsV6_MC_L2Relative_AK4PFchs.txt',
                             'Summer15_25nsV6_MC_L3Absolute_AK4PFchs.txt',
                             'Summer15_25nsV6_MC_Uncertainty_AK4PFchs.txt',
                             'Summer15_25nsV6_MC_L1FastJet_AK8PFchs.txt',
                             'Summer15_25nsV6_MC_L2Relative_AK8PFchs.txt',
                             'Summer15_25nsV6_MC_L3Absolute_AK8PFchs.txt',
                             'Summer15_25nsV6_MC_Uncertainty_AK8PFchs.txt',
                             'Summer15_25nsV6_DATA_L1FastJet_AK4PFchs.txt',
                             'Summer15_25nsV6_DATA_L2Relative_AK4PFchs.txt',
                             'Summer15_25nsV6_DATA_L3Absolute_AK4PFchs.txt',
                             'Summer15_25nsV6_DATA_L2L3Residual_AK4PFchs.txt',
                             'Summer15_25nsV6_DATA_Uncertainty_AK4PFchs.txt',
                             'Summer15_25nsV6_DATA_L1FastJet_AK8PFchs.txt',
                             'Summer15_25nsV6_DATA_L2Relative_AK8PFchs.txt',
                             'Summer15_25nsV6_DATA_L3Absolute_AK8PFchs.txt',
                             'Summer15_25nsV6_DATA_L2L3Residual_AK8PFchs.txt',
                             'Summer15_25nsV6_DATA_Uncertainty_AK8PFchs.txt'
                             ]
config.section_("Data")
#config.Data.inputDataset = '/DYJetsToLL_M-50_HT-100to200_Tune4C_13TeV-madgraph-tauola/Spring14dr-PU20bx25_POSTLS170_V5-v1/AODSIM '
config.Data.inputDataset = '/DYJetsToLL_M-50_HT-100to200_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
#config.Data.inputDataset = '/DYJetsToLL_M-50_13TeV-madgraph-pythia8/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
#config.Data.publication = True
#config.Data.publishDbsUrl = 'phys03'
#config.Data.publishDataName = 'CRAB3_CSA_DYJets'
config.JobType.allowUndistributedCMSSW=True

#maxtarballsize = 50 
config.section_("Site")
config.Site.storageSite = "T2_CH_CERN"
