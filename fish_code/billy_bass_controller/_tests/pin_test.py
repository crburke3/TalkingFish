import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
PIN = 26

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

while True: # Run forever
    if GPIO.input(PIN) == GPIO.HIGH:
        print("Button was pushed!")
    else:
        print("NOT PRESSED")
