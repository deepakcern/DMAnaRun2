import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import updatedPatJets

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'root://xrootd.cmsaf.mit.edu//store/user/bmaier/moriond17/2HDMa_gg_tb_1p0_MH3_600_MH4_100_MH2_600_MHC_600/2HDMa_gg_tb_1p0_MH3_600_MH4_100_MH2_600_MHC_600_42732727_miniaod.root'
    )
)



process.appliedRegJets= cms.EDProducer('bRegressionProducer',
                                           JetTag=cms.InputTag("slimmedJets"),
                                           rhoFixedGridCollection = cms.InputTag('fixedGridRhoFastjetAll'),
                                           bRegressionWeightfile= cms.untracked.string("/afs/cern.ch/work/d/dekumar/public/flashgg_setup/CMSSW_8_0_28/src/flashgg/MetaData/data/DNN_models/model-18"), 
                                           y_mean = cms.untracked.double(1.0454729795455933) ,
                                           y_std = cms.untracked.double( 0.31628304719924927)
                                           )


process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)


process.p = cms.Path(process.appliedRegJets)

process.e = cms.EndPath(process.out)

