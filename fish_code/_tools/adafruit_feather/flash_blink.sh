ampy -p /dev/tty.usbserial-022F211C put ../../tests/blink.py
echo "Wrote blink.py to board"
ampy -p /dev/tty.usbserial-022F211C get blink.py