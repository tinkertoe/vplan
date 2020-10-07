sudo screen -X -S "web_vplan" quit
sleep 1
sudo screen -S "web_vplan" -d -m
sleep 1
sudo screen -r "web_vplan" -X stuff 'sudo python3 vplan.py\n'
