from get_stored_network_password import passwordFetch
from helper import check_status_pass
from pdf_to_audio import pdfToAudio

def main():
    print("Choose from below mentioned List \n")
    
    user_opt = 0
    
    print("1. Get Stored Network Password\n")
    print("2. Convert PDF to Audio\n")
    
    user_opt = int(input("Please Choose: "))
    
    match user_opt:
        case 1:
            # Get the stored network password from keychain.    
            netPass = passwordFetch()
            if(check_status_pass(netPass)) : print("Password retrival Successful")
            else : 
                print("Password retrival Fails! \n")
                user_res = input("Do you want to retry? [y/n] : ")
                while(user_res == 'y'): 
                    if(check_status_pass(passwordFetch())): break
                    else: user_res = input("\nDo you want to retry? [y/n] : ")
        case 2:
            # Get audio file of your pdf
            file_path = input("Please enter File path: ")
            netPass = pdfToAudio(filePath=file_path)
            if(check_status_pass(netPass)) : print("Audio file creation Successful")
            else : 
                print("Audio file creation Fails! \n")
                user_res = input("Do you want to retry? [y/n] : ")
                while(user_res == 'y'): 
                    if(check_status_pass(passwordFetch())): break
                    else: user_res = input("\nDo you want to retry? [y/n] : ")
            
            
        

main()
    
    