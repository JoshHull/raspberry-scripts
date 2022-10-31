nohup python pet-hat.py > log/pet-hat.log.log 2>&1 &
echo $! > log/background_pid.txt
