
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
import os,time,datetime
import pandas as pd
import pprint
from queue import Queue
from handler_binary import *
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------#

#-----------------------------------------------------#
time_formatter = "%y%m%d%H%M%S"
bin_f_name = "folder_data"
bin_i_name = "folders"
fd_patt = {"Folder_Name":"",
        "Folder_Path":"",
        "Child_Names":[],
        "Child_Paths":[]} #  M???U DICTIONARY TH??NG TIN FOLDER
#-----------------------------------------------------#

#-----------------------------------------------------#
def main_folder_access():
    """KHAI B??O KHO CH???A C??C D??? ??N BIM TRI???N KHAI """

    # ip = "172.16.2.29"
    # domain = "hcmcfcfs01"
    # projects_root = "" #r"R:\BimESC\01_PROJECTS"
    # projects_root_ip = f"\\\\{ip}\\databim$\\BimESC\\01_PROJECTS"
    # projects_root_domain = f"\\\\{domain}\\databim$\\BimESC\\01_PROJECTS"
    
    # if os.path.exists(projects_root_ip):
    #     projects_root = projects_root_ip
    
    # if os.path.exists(projects_root_domain):
    #     projects_root = projects_root_domain   

    projects_root = input('Root path: ')
    
    
    print(f"B???n ??ang [Duy???t] th?? m???c BIM: {projects_root}")
    
    folder_data_dir = projects_root+"\\"+""+"_DATA"    
    #   TRUY C???P D??? LI???U V??? FOLDER C??C D??? ??N BIM
    folder = None
    folders_df = None
    folders_df = read_data_folder(folder_data_dir)
    flag_data_exist = False
    if folders_df.empty:
        flag_data_exist = True
    if flag_data_exist:
        folders,folders_df= folder_traverse(projects_root)
        print(folders_df)        
        #   WRITE DATA FILE  
        folder_data_path = write_data_folder(folders_df,folder_data_dir)
        update_bin(folder_data_dir,folder_data_path)
    summary_traverse(folders_df)

def find_child():
    """"""
    pass
def find_bim_data():
    """"""
    pass

def folder_traverse(projects_root):
    """"""
    folders = []
    for f in os.listdir(projects_root):
        fd = fd_patt.copy()
        if "." not in f:
            fd['FolderName'] = f
            fd['FolderPath'] = projects_root + "\\" + f
            folders.append(fd)
    folders_df = pd.DataFrame(folders)
    return folders,folders_df
def summary_traverse(folders_df):
    print(f"""---K???t qu??? traverse Folders:
    ------T???ng: {folders_df.shape[0]} folder d??? ??n Ph??ng BIM ??ang tri???n khai
    --------------------------------------------------
    ------T???ng: {0} folder ?????t t??n SAI CHU???N
    ------T???ng: {0} folder B??? CH???A L???NG (NESTED)
    --------------------------------------------------
    ------T???ng: {0} folder D??? ??n th??? lo???i CAO T???NG
    ------T???ng: {0} folder D??? ??n th??? lo???i H??? T???NG
    ------T???ng: {0} folder D??? ??n th??? lo???i C??NG NGHI???P
    ------T???ng: {0} folder D??? ??n th??? lo???i C??NG C???NG
    ------T???ng: {0} folder D??? ??n th??? lo???i KH??C
    --------------------------------------------------
    ------T???ng: {0} folder c?? D??? li???u ** B I M **
    """)
#-----------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------#?????C TH??NG TIN V??? FOLDERS
def read_data_folder(folder_data_dir):
    """"""
    bin_f_path = f"{folder_data_dir}\\{bin_f_name}"
    if os.path.exists(bin_f_path+".dat"):
        folder_data = pd.read_json(read_bin(bin_f_path,bin_i_name).get())
        print(folder_data)
        return folder_data
    else:
        return pd.DataFrame([])

def write_data_folder(folders_df,folder_data_dir): #to JSON
    date_write = time.strftime(time_formatter,time.localtime(time.time()))
    folder_data_path = f"{folder_data_dir}\\folder_data-{date_write}.json"
    try:
        folders_df.to_json(folder_data_path,orient='records',indent=4)    
        print(f"---Th??nh c??ng ghi d??? li???u Folder: {folder_data_path}---Size: {round(float(os.stat(folder_data_path).st_size)/1000,2)} KB")
        return folder_data_path    
    except Exception as ex:
        print(f"---Ghi d??? li???u -*Kh??ng th??nh c??ng\n------C?? l???i: {ex}")
        pass

def update_bin(folder_data_dir,folder_data_path,i_name = bin_i_name):
    """"""
    bin_f_path = f"{folder_data_dir}\\{bin_f_name}"
    flag_exist_bin = os.path.exists(bin_f_path+".dat")
    if flag_exist_bin:
        quere_data = read_bin(bin_f_path,i_name)
        quere_data.put(folder_data_path)
        write_bin_quere_object(bin_f_path,i_name,quere_data)
    else: # TR?????NG H???P KH??NG C?? FILE BINARY N??O
        data_files = [folder_data_dir+"\\"+d for d in os.listdir(folder_data_dir) if ".json" in d]
        write_bin_from_list(bin_f_path,i_name,data_files)
    pass


#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    main_folder_access()