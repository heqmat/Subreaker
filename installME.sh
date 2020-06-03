echo -e "\e[1;35m Maybe you did not install some requirements like python,g and some modules. So i will install all requirements for you.  \e[0m"
echo -e "\e[1;35m -----------------------------------------------------------------------------------------------------------------------\e[0m"
echo -e "\e[1;33m If you not root please be root and again run. \e[0m"
echo -e "\e[1;33m Updating your system... \e[0m"
sudo apt-get update 
echo -e "\e[1;32m Done!! \e[0m"
echo -e "\e[1;33m Checking python versions... \e[0m"
sudo apt-get install python3.7 
echo -e "\e[1;32m Done!! \e[0m"
echo -e "\e[1;33m Checking pip versions..."
sudo python get-pip.py
echo -e "\e[1;36m Now i will install some modules for you. Program \e[0m"
pip install numpy
pip install scapy
#echo -e "\e[1;36m Now installing gnome-terminal this process can  \e[0m" -----Not need this.
#sudo apt-get install gnome-terminal --------Not need this.
echo ' -> set command'
MYPWD=`pwd`
echo '#/usr/bin/python
python '$MYPWD'/subreaker.py $*' >> /usr/bin/subreaker
echo 'Set Perm'
chmod 755 /usr/bin/subreaker
echo -e "\e[1;32m Done!! \e[0m"
echo -e "\e[1;32m Everything ready to start now you can use Barrel!!\e[0m"





















