kill -9 `cat log/background_pid.txt`;
echo 'killed process id ' `cat log/background_pid.txt`; 
rm log/background_pid.txt;
