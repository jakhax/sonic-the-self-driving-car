## Setup 
### Bluetooth setup 
```bash 
sudo apt-get install bluetooth libbluetooth3 libusb-dev
sudo systemctl enable bluetooth.service
sudo usermod -G bluetooth -a pi
```
- Reboot
- Plug in the PS3 with USB cable. Hit center PS logo button. Get and build the command line pairing tool. Run it:


```bash
gcc -o sixpair sixpair.c -lusb
sudo ./sixpair
```
- Use bluetoothctl to pair
```bash
bluetoothctl
agent on
devices
trust <MAC ADDRESS>
default-agent
quit
```
- Unplug USB cable. Hit center PS logo button.
- To test that the Bluetooth PS3 remote is working, verify that `/dev/input/js0` exists.
```bash
ls /dev/input/js0
```
- run `python3 controller.py` to test the controller.
