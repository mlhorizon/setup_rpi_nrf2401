#/bin/bash
sudo apt-get update
wget https://github.com/Gadgetoid/py-spidev/archive/master.zip
unzip master.zip
rm master.zip
cd py-spidev-master/
sudo python setup.py install
cd ~/Desktop
git clone https://github.com/BLavery/lib_nrf24
cp lib_nrf24/lib_nrf24.py ~/Desktop
