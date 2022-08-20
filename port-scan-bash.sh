#!/bin/bash
clear
if test $# -lt 1 
then
        echo -e "\n\n[!] Usage: $0 ip-address"
        echo -e "\nExample: $0 192.168.0.1"
        tput cnorm; exit 1

fi

function ctrl_c(){
                echo -e "\n\n[!] Saliendo...\n"
                tput cnorm; exit 1
}

#Ctrl+Ctrl
trap ctrl_c INT

#Change the networks
ip=($1)

echo -e "[!] Scanning ports for $ip"
tput civis; for i in $(seq 1 5000); do
        timeout 1 bash -c "echo >/dev/tcp/$ip/$i" &>/dev/null && echo -e "PORT $i: ACTIVE"
done; tput cnorm
