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
    # LỜI CHÀO
    #----------------------------------------------------------------#
    program_version = "1.0 - 14/06/2021"
    welcome_promp = f"""
    #----------------------------------------------------------------#
        CHÀO MỪNG ĐẾN CHƯƠNG TRÌNH : MÔ HÌNH THÔNG TIN TÒA NHÀ
            Version :   {program_version}
            Author  :   tvpduy
    #----------------------------------------------------------------#
    """
    print(welcome_promp)
    #----------------------------------------------------------------#
    # HỎI ? DỰ ÁN MỚI ?
    #----------------------------------------------------------------#
    isNewProject = input(f"""
    <Câu hỏi>           :   BẠN MUỐN TẠO DỰ ÁN MỚI hay TRUY CẬP VÀO DỰ ÁN ĐÃ TỒN TẠI??
    1   TẠO DỰ ÁN MỚI
    2   TRUY CẬP VÀO DỰ ÁN ĐÃ TỒN TẠI
    3   THOÁT
    <Trả lời của bạn>   :   """)

    if isNewProject == "1":
        print("---Bạn đã chọn TẠO DỰ ÁN MỚI, Template dự án mới đang được TẢI...")
        project_number = input("---Vui lòng chọn Mã dự án muốn tạo mới: ")
        print(f"---Bạn đã chọn TẠO DỰ ÁN MỚI với Mã {project_number} --- Đang kiểm tra với Cơ sở dữ liệu Dự án Đã tồn tại")
        flag_exist = [project_number != proj['ProjectNumber'] for proj in bim_projects_data]
        print(flag_exist)
        if False in flag_exist:
            print(f"<--!--> MÃ DỰ ÁN ĐÃ TỒN TẠI, vui lòng đặt lại mã khác <--!-->")
        else:
            project_creator = projectCreater(project_number)
            project_creator.start()
            project_creator.end()

    if isNewProject == "2":
        print("---Bạn đã chọn TRUY CẬP VÀO DỰ ÁN ĐÃ TỒN TẠI, Cơ sở dữ liệu dự án đang được TẢI...")    
        print("---Danh sách các dự án: ",[proj['ProjectNumber'] for proj in bim_projects_data])
        project_number = input("---Vui lòng chọn Mã dự án muốn truy cập: ")
        project_name = [proj['ProjectName'] for proj in bim_projects_data if proj['ProjectNumber'] == project_number][0]
        print(f"---Bạn đã chọn dự án {project_number} - {project_name} --- Dữ liệu dự án đang được TẢI...")
        pass
    if isNewProject == "3":
        quit()