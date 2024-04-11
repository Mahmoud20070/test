import os , datetime
# import pandas as pd






# path = r"Z:\Desktop\Users_Admin"

# # ~ for date
# # $ for time
# # _ for delemite ,

# s = ["SN","Date","Category","Item","Q","Request Time","Request By","ACD 1","Old shift1","New shift1","ACD 2","Old shift2","New shift2","Approval WFM Time","Approval WFM By","Comment","Resolution"]


# username =  str(os.getenv("username")) 




# def writedb(
#         path, # full path
#         actiontype="add", # write or edit
#         ticketname=None,
#         newupdate=None,
#         SN="-",
#         Date="-",
#         Category="-",
#         item="-",
#         Q="-",
#         requestedby="-",
#         ACD1="-",
#         oldshift1="-",
#         newshift1="-",
#         ACD2="-",
#         oldshift2="-",
#         newshift2="-",
#         approval_wfm_time="-",
#         approval_wfm_by="-",
#         comment="-",
#         resolution="Pending" # Pending , Rejected , Done , Hide
#         ):
    
#     createdtime = datetime.datetime.now().strftime("%d~%b~%y %H$%M$%S.%f") + "-"

#     if actiontype == "add":
#         with open(file=os.path.join(path , createdtime + username + "," + Date + "," + Category + "," + item + "," + Q + "," + createdtime + "," + requestedby + "," + ACD1 + "," + oldshift1 + "," + newshift1 + "," + ACD2 + "," + oldshift2 + "," + newshift2 + "," + approval_wfm_time + "," + approval_wfm_by + "," + comment + "," + resolution),mode="w"): pass
#     elif actiontype == "edit": 
#         os.rename(os.path.join(path,ticketname),os.path.join(path ,newupdate))
#     else: pass    





# #writedb(path=path,actiontype="add",resolution="Done")
# writedb(path=path,actiontype="edit",ticketname="03~Mar~24 10$20$42.225961-test,-,-,-,-,03~Mar~24 10$20$42.225961-,-,-,-,-,-,-,-,-,mashussein,-,Reject",newupdate="03~Mar~24 10$20$42.225961-test,-,-,-,-,03~Mar~24 10$20$42.225961-,-,-,-,-,-,-,-,-,-,-,Done")
        

# quit()
# tkts = [everytkt.name.split("_") for everytkt in os.scandir(path)]

# df = pd.DataFrame(tkts)




# replacements = {"~":"-" , "@":":" , "_":","}

# df.replace(to_replace=replacements, regex=True , inplace=True)


















