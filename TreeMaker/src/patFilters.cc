// Updated By : Raman Khurana 
// Dated      : Mon May 25 15:40:47 CDT 2015
// Added possible triggers for DM analysis, Jets and MET
#include "DelPanj/TreeMaker/interface/patFilters.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "FWCore/Common/interface/TriggerNames.h" 
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/METReco/interface/HcalNoiseSummary.h"

patFilters::patFilters(std::string name,TTree* tree):
  baseTree(name,tree),
  nfilters_(0)
{
  SetBranches();
}

void
patFilters::Fill(const edm::Event& iEvent)
{
  Clear();
  using namespace edm;
  
  /*
  edm::Handle<bool> HBHET;
  iEvent.getByToken(HBHETToken,HBHET);
  hbhet_ = (*HBHET.product());

  edm::Handle<bool> HBHEL;
  iEvent.getByToken(HBHELToken,HBHEL);
  hbhel_ = (*HBHEL.product());

  edm::Handle<bool> HBHEIso;
  iEvent.getByToken(HBHEIsoToken,HBHEIso);
  hbheIso_ = (*HBHEIso.product());
  */
  
  edm::Handle<edm::TriggerResults> trigResults;
  if (not iEvent.getByToken(filterTrigResultsToken, trigResults)) {
    std::cout << ">>> TRIGGER collection for filters does not exist !!!\n";
    return;
  }

  const edm::TriggerNames & trigNames = iEvent.triggerNames(*trigResults);
  //const std::vector<std::string> & triggerNames_ = trigNames.triggerNames();

  for (unsigned int i=0; i<trigResults->size(); i++)
    {
      std::string trigName = trigNames.triggerName(i);
      // lepton triggers
      size_t foundallFlag=trigName.find("Flag_");
            

      if(false) std::cout<<" trigName = "<<trigName
			<<" : "<<trigResults->accept(i)
			<<std::endl;
      
      if ( foundallFlag==std::string::npos  )     	continue;
      

      
      filterName_.push_back(trigName);
      bool trigResult = trigResults->accept(i); //bool not to use
      filterResult_.push_back(trigResult);
      nfilters_++;
    }
}

void patFilters::SetBranches(){
  
  AddBranch(&nfilters_,"nfilters");
  AddBranch(&filterResult_,"filterResult");
  AddBranch(&hbhet_,"hbhet");
  AddBranch(&filterName_,"filterName");


}

void
patFilters::Clear(){
  nfilters_ = 0;
  filterResult_.clear();
  filterName_.clear();
  hbhet_ = false;
}


