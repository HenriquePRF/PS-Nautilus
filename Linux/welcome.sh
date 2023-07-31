#!/bin/bash

echo "Bem vindo ao $USER ao terminal $HOSTNAME."
curl wttr.in/?0
echo "Data de execucao: $(date)" >> ~/.welcome.data 
