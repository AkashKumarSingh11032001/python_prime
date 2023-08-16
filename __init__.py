from get_stored_network_password import passwordFetch
from helper import check_status_pass

def main():
    
    # Get the stored network password from keychain.
    netPass = passwordFetch()
    if(check_status_pass(netPass)) : print("Password retrival Successful")
    else : 
        print("Password retrival Fails! \n")
        user_res = input("Do you want to retry? [y/n] : ")
        while(user_res == 'y'): 
            if(check_status_pass(passwordFetch())): break
            else: user_res = input("\nDo you want to retry? [y/n] : ")
        

main()
    
    