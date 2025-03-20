#!/usr/bin/python3
# Pdf Password Cracker tool 


from pypdf import PdfReader
from colorama import Style,Fore
from tqdm import tqdm
import sys
import time
import os


if len(sys.argv) == 1 or "--help" in sys.argv or "-h" in sys.argv:
        print("help: killer [PDF] [Wordlist (optional)]")
        sys.exit()

before_time = time.time()

def cracker(pdf,password):
        locked_pdf = PdfReader(pdf)

        if(locked_pdf.is_encrypted):
                try:
                        status_code = locked_pdf.decrypt(password)

                        if status_code:
                                tqdm.write(Style.BRIGHT+Fore.GREEN+'---------------------------------------')
                                tqdm.write(f'[\u2714] Password Cracked = "{password}" ')
                                tqdm.write('---------------------------------------')
                                time_elapsed = (time.time() - before_time)
                                tqdm.write(f"Time elapsed : {time_elapsed}s"+Style.RESET_ALL)
                                return True

                except Exception as e:
                        print(e)
        else:
                tqdm.write("File is already decrypted ..")

def main():
        print()
        patterns = ['|',"/","-","\\","|","/","-","\\","|",'|',"/","-","\\","|","/","-","\\","|"]
        for init in patterns:
                print(f"\rPdkiller [INIT] : Initialising the Recovery tool .. {init}",flush=True,end="")
                time.sleep(0.15)
        print()

        if len(sys.argv) == 3:
                with open(sys.argv[2],"r") as wordlist:
                        passwords = wordlist.read()
                        passwords = passwords.splitlines()

        elif len(sys.argv) == 2:
                with open('/usr/share/wordlists/rockyou.txt',"rb") as wordlist:
                        passwords = wordlist.read().decode('latin-1',errors="ignore")
                        passwords = passwords.splitlines()

        print()
        print("--------------------------------")
        print(f"[+] File Name : {sys.argv[1]}")
        print("--------------------------------")
        print()

        time.sleep(2)
        progress_bar = tqdm(passwords,desc="Cracking progress",unit=" [Password Attempts] ")


        try:
                for password in progress_bar:
                        if(cracker(sys.argv[1],password)):
                                progress_bar.close()
                                sys.exit()

        except KeyboardInterrupt:
                tqdm.write("Pdfkiller [+] : Thanks for using our tool !")
                progress_bar.close()
                sys.exit()

        time_elapsed = (time.time() - before_time)
        print()
        tqdm.write(Style.BRIGHT+Fore.BLUE+f'{Pdfkiller : [+] {len(passwords)} Passwords tried but , 0 valid passwords Found .. }'+Style.RESET_ALL)
        print()
        tqdm.write(Style.BRIGHT+Fore.GREEN+f"Time elapsed : {time_elapsed}s"+Style.RESET_ALL)



if __name__ == "__main__":
        if not sys.argv[1].endswith(".pdf"):
                tqdm.write("[\u2716] Invalid document provided ..")
        else:
                main()
