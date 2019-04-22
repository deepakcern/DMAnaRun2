#ifndef  TREE_MAKERTEST_H
#define  TREE_MAKERTEST_H

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DelPanj/TreeMaker/interface/puweight.h"
#include "DelPanj/TreeMaker/interface/eventInfo.h"
#include "DelPanj/TreeMaker/interface/patMetTree.h"
#include "DelPanj/TreeMaker/interface/patHltTree.h"
#include "DelPanj/TreeMaker/interface/patFilters.h"
#include "DelPanj/TreeMaker/interface/genInfoTree.h"
#include "DelPanj/TreeMaker/interface/patElecTree.h"
#include "DelPanj/TreeMaker/interface/patMuonTree.h"
#include "DelPanj/TreeMaker/interface/hpstauInfo.h"
#include "DelPanj/TreeMaker/interface/photonTree.h"
#include "DelPanj/TreeMaker/interface/jetTree.h"


#include "TTree.h"
#include "TFile.h"

using namespace edm;
class TreeMakertest : public edm::EDAnalyzer {
   public:
      explicit TreeMakertest(const edm::ParameterSet&);
      ~TreeMakertest();
      edm::EDGetTokenT<View<pat::Jet> > jetToken_;


   private:
      virtual void beginJob() ;
      virtual void beginRun(const edm::Run&, const edm::EventSetup& ) ;
      virtual void analyze(const edm::Event&, const edm::EventSetup& );
      //edm::EDGetTokenT<View<pat::Jet> > jetToken_;
      virtual void endRun(const edm::Run&, const edm::EventSetup& );
      virtual void endJob() ;
      TFile* file;
      TTree* tree_;
      std::string outFileName_ ;

      //edm::EDGetTokenT<View<pat::Jet> > jetToken_;
      bool fillPUweightInfo_; 
      bool fillEventInfo_;
      bool fillMetInfo_;
      bool fillTrigInfo_;
      bool fillFilterInfo_;

      bool fillGenInfo_;

      
      bool fillElecInfo_;
      bool fillMuonInfo_;
      bool fillTauInfo_;
      bool fillPhotInfo_;


      bool fillJetInfo_;
      bool fillFATJetInfo_;
      bool fillAK4PuppiJetInfo_;
      bool fillAK8PuppiJetInfo_;
      bool fillCA15PuppiJetInfo_;
      
      puweight *puweight_;
      eventInfo   *eventInfo_;
      patMetTree  *patMetTree_;

      patHltTree  *patHltTree_;      
      patFilters  *patFilterTree_;
      
      genInfoTree *genInfoTree_;    

      patElecTree *patElecTree_;
      patMuonTree *patMuTree_;
      hpstauInfo  *tauTree_;
      photonTree  *photonTree_;


      jetTree     *THINjetTree_;
      jetTree     *FATjetTree_;
      jetTree     *AK4PuppijetTree_;     
      jetTree     *AK8PuppijetTree_;     
      jetTree     *CA15PuppijetTree_;     
 
      

};


#endif
