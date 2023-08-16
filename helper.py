def check_status_pass(status):
    passValue = ["Pass","pass",1,True]
    failValue = ["Fail","fail",0,False]
    if(status in passValue): return True
    else: return False