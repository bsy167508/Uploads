#!/bin/bash
echo '=+=+=+=+=+= System Information =+=+=+=+=+='
echo "Processor -  $($_CMD cat /proc/cpuinfo | grep 'model name' | uniq | awk '{print $4,"",$5,"", $6,"", $7,"", $8 }' )"
echo "RAM -  $($_CMD free -mto | grep Mem: | awk '{ print $2 " MB" }')"
echo "$($_CMD lscpu | grep 'Architecture' )"
echo "MAC Address - $($_CMD ifconfig | grep 'wlan0     Link encap' | awk '{ print $5 }' )"
echo "Linux Kernel - $($_CMD uname -r )"
echo "Ubuntu Release - $($_CMD lsb_release -d | awk '{print $2,"",$3,"",$4,"",$5 }')"
echo -n "Python version - "
echo "$($_CMD python --version)"
echo '=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+'
