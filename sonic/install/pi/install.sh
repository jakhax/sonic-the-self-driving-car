
#standard updates (5 min)
sudo apt update -y
sudo apt upgrade -y
sudo rpi-update -y

#helpful libraries (2 min)
sudo apt install build-essential python3-dev python3-distlib python3-setuptools  python3-pip python3-wheel -y

sudo apt-get install git cmake pkg-config -y
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev -y
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
sudo apt-get install libxvidcore-dev libx264-dev -y
sudo apt-get install libatlas-base-dev gfortran -y

sudo apt install libzmq-dev -y
sudo apt install xsel xclip -y
sudo apt install python3-h5py -y

#install numpy and pandas (3 min)
sudo apt install libxml2-dev python3-lxml -y
sudo apt install libxslt-dev -y 
# install pandas and numpy
pip install pandas #also installs numpy

