#!/bin/bash
clear
if test $# -lt 1 
then
        echo -e "\n\n[!] Usage: $0 network"
        echo -e "\nExample: $0 192.168.0  <- DO NOT INCLUDE THE LAST OCTET"
        tput cnorm; exit 1

fi

function ctrl_c(){
                echo -e "\n\n[!] Saliendo...\n"
                tput cnorm; exit 1
}

#Ctrl+Ctrl
trap ctrl_c INT

#Change the networks
networks=($1)

tput civis; for network in ${networks[@]}; do
                echo -e "\n[+] Scanning the network $network.0/24: "
                for i in $(seq 1 254); do
                                timeout 1 bash -c "ping -c 1 $network.$i" &>/dev/null && echo -e "\t[+] Host $network.$i - ACTIVE" &
                done; wait
done; tput cnorm
