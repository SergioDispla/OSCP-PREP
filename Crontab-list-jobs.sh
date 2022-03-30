#!/bin/bash

old_process=$(ps -eo command)

While True; 
do
	new_process=$(ps -eo command)
	diff <(echo "$old_process") <(echo "$new_process") | grep "[\>\<]" | grep -v -E "procmon|command"
	old_process=$new_process
	
Done



#Este script nos va a mostrar los jobs que se estan ejecuntando frecuentemente. De ahi podemos sacar una via potencial de escalada de privilegios, #ya que ciertos jobs se ejecutan como root. 
