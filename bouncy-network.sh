#!/bin/bash
bounce=false;

sleeptime=0;
while sleep $sleeptime; do
 if $bounce; then
    echo 'turning off wlan0';
    sudo ifconfig wlan0 down;
    bounce=false;
 else 
    echo 'turning on  wlan0';
    sudo ifconfig wlan0 up;
    bounce=true;
 fi;

 sleeptime=$(( $RANDOM%300+10 ));
 echo 'sleeping ' $sleeptime;
done
