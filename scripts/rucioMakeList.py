import os

def rucioMakeList(dsname,tempfname):
    #gridSite = "MWT2_UC_LOCALGROUPDISK"
    gridSite = "DESY-HH_LOCALGROUPDISK"
    l = os.popen("rucio list-file-replicas --protocol root "+dsname+" | grep "+gridSite)
    f = open(tempfname,"w")
    for line in l:
        line = line.split(gridSite+": ")[-1]
        line = line.split()[0]
        f.write(line+"\n")
        #print(line)

    f.close()
