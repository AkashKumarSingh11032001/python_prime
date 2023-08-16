import os

def check_status_pass(status):
    passValue = ["Pass","pass",1,True]
    failValue = ["Fail","fail",0,False]
    if(status in passValue): return True
    else: return False
    
def getFileNameFromFilePath(path):
    file_name = os.path.basename(path).split('/')[-1]
    return file_name