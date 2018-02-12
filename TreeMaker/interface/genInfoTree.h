#ifndef _GEN_INFO_TREE_H_
#define _GEN_INFO_TREE_H_

/*
  Updated by: Shin-Shan Yu
  Date      : 20 March 2016
  Replace getByLabel with getByToken
*/

#include <memory>
#include <vector>
#include <string>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"

#include "SimDataFormats/GeneratorProducts/interface/LHERunInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"


#include "DelPanj/TreeMaker/interface/baseTree.h"
#include "TH1.h"
#include "TFile.h"
#include "TTree.h"

//
// class declaration
//

class genInfoTree : public baseTree{

 public:
  genInfoTree(std::string name, TTree* tree, const edm::ParameterSet& cfg);
  ~genInfoTree();
  void GetRunInfo(const edm::Run& iRun);
  void Fill(const edm::Event& iEvent);
  void Clear();

  edm::EDGetTokenT<reco::GenParticleCollection>     genParticleToken;
  edm::EDGetTokenT<reco::GenParticleCollection>     genMETpTToken;
  edm::EDGetTokenT<GenEventInfoProduct>             genEventToken;
  edm::EDGetTokenT<LHERunInfoProduct>               lheRunToken;
  edm::EDGetTokenT<LHEEventProduct>                 lheEventToken;

  edm::EDGetTokenT<reco::GenMETCollection>          genMETToken_true;
  edm::EDGetTokenT<reco::GenMETCollection>          genMETToken_calo;
  edm::EDGetTokenT<reco::GenMETCollection>          genMETToken_caloNonPrompt;
  edm::EDGetTokenT<reco::GenJetCollection>          ak4genJetsToken;

  unsigned int MAXNGENPAR_;
  bool applyStatusSelection_;  // keep only particles with status code <=30
  bool applyPromptSelection_;  // keep only prompt particles or particles with status<=30
  bool saveLHEWeights_;        // save all LHE weights
  bool saveGenJets_;           // save genJets information
 private:

  genInfoTree(){};
  void SetBranches();


  float ptHat_;      // added by Eiko
  float mcWeight_;   // added by Eiko
  float HT_;       // added by Eiko
  float genMET_true_; // added by Eiko
  float genMET_calo_;  // added by Eiko
  float genMET_caloNonPrompt_; // added by Eiko
  float genMETPt_; //Added by Praveen

  std::vector<float>       pdf_;
  float                    originalLHEweight_;
  std::vector<float>       pdfscaleSysWeights_;

  int nGenPar_;
  TClonesArray       *genParP4_;
  std::vector<int>   genParQ_;
  std::vector<int>   genParId_;
  std::vector<int>   genParSt_;
  std::vector<int>   genMomParId_; // added by Eiko
  std::vector<int>   genParIndex_;    // added by Eiko
  std::vector<int>   genNMo_;
  std::vector<int>   genNDa_;
  std::vector<int>   genMo1_;
  std::vector<int>   genMo2_;
  std::vector<int>   genDa1_;
  std::vector<int>   genDa2_;
  std::vector<int>   genStFlag_;
  


  // save this informatio if saveGenJets is true

  int ak4nGenJet_;
  TClonesArray       *ak4GenJetP4_;

};

#endif
