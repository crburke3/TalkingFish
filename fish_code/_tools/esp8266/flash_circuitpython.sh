#esptool.py --chip esp8266 --port /dev/tty.usbserial-0001 --baud 460800 write_flash -z 0x1000 ../_firmware/circuitpython_esp8266.bin

esptool.py --port /dev/tty.usbserial-0001 --baud 115200 write_flash --flash_size=detect 0 ../_firmware/circuitpython_esp8266.bin
