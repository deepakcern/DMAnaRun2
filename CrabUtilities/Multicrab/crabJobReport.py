import os,sys
#folder="crab_bbDM_bkg"
#listfolders = [f for f in os.listdir(folder) ]
#for fold1 in listfolders:
 #   os.system("crab resubmit crab_bbDM_bkg/"+fold1)
  #  print("Resubmitted "+fold1+"\n")

folder=sys.argv[1]
listfolders = [f for f in os.listdir(folder) ]
for fold1 in listfolders:
    print("Report of "+fold1+"\n")
    os.system("crab report "+folder+"/"+fold1)

