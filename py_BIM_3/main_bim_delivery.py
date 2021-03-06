#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
import pandas as pd
import numpy as np
import os, sys, json

from handler_cad_data import *
from handler_project import *

from data_projects import *
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#



if __name__ == '__main__':  
    #----------------------------------------------------------------#
    # L???I CH??O
    #----------------------------------------------------------------#
    program_version = "1.0 - 14/06/2021"
    welcome_promp = f"""
    #----------------------------------------------------------------#
        CH??O M???NG ?????N CH????NG TR??NH : M?? H??NH TH??NG TIN T??A NH??
            Version :   {program_version}
            Author  :   tvpduy
    #----------------------------------------------------------------#
    """
    print(welcome_promp)
    #----------------------------------------------------------------#
    # H???I ? D??? ??N M???I ?
    #----------------------------------------------------------------#
    isNewProject = input(f"""
    <C??u h???i>           :   B???N MU???N T???O D??? ??N M???I hay TRUY C???P V??O D??? ??N ???? T???N T???I??
    1   T???O D??? ??N M???I
    2   TRUY C???P V??O D??? ??N ???? T???N T???I
    3   THO??T
    <Tr??? l???i c???a b???n>   :   """)

    if isNewProject == "1":
        print("---B???n ???? ch???n T???O D??? ??N M???I, Template d??? ??n m???i ??ang ???????c T???I...")
        project_number = input("---Vui l??ng ch???n M?? d??? ??n mu???n t???o m???i: ")
        print(f"---B???n ???? ch???n T???O D??? ??N M???I v???i M?? {project_number} --- ??ang ki???m tra v???i C?? s??? d??? li???u D??? ??n ???? t???n t???i")
        flag_exist = [project_number != proj['ProjectNumber'] for proj in bim_projects_data]
        print(flag_exist)
        if False in flag_exist:
            print(f"<--!--> M?? D??? ??N ???? T???N T???I, vui l??ng ?????t l???i m?? kh??c <--!-->")
        else:
            project_creator = projectCreater(project_number)
            project_creator.start()
            project_creator.end()

    if isNewProject == "2":
        print("---B???n ???? ch???n TRUY C???P V??O D??? ??N ???? T???N T???I, C?? s??? d??? li???u d??? ??n ??ang ???????c T???I...")    
        print("---Danh s??ch c??c d??? ??n: ",[proj['ProjectNumber'] for proj in bim_projects_data])
        project_number = input("---Vui l??ng ch???n M?? d??? ??n mu???n truy c???p: ")
        project_name = [proj['ProjectName'] for proj in bim_projects_data if proj['ProjectNumber'] == project_number][0]
        print(f"---B???n ???? ch???n d??? ??n {project_number} - {project_name} --- D??? li???u d??? ??n ??ang ???????c T???I...")
        pass
    if isNewProject == "3":
        quit()