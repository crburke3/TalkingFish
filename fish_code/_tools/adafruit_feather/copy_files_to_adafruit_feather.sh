ampy --port /dev/tty.usbserial-022F211C put ../../src/esp32_motor_controller.py
echo "copied motor_controller.py"
ampy --port /dev/tty.usbserial-022F211C put ../../src/main.py
echo "copied main.py"
chmod 755 serial_into_feather.sh
./serial_into_feather.sh