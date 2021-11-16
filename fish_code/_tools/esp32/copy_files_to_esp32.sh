ampy --port /dev/tty.usbserial-0001 put ../../src/motor_controller.py
echo "copied motor_controller.py"
ampy --port /dev/tty.usbserial-0001 put ../../src/main.py
echo "copied main.py"
ampy --port /dev/tty.usbserial-0001 put ../../tests/blink.py
echo "copied main.py"

chmod 755 serial_into_feather.sh
./serial_into_feather.sh