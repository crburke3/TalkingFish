echo "Please go through all the prompts on this next command. And reboot 1st time. Do not reboot 2nd time!"
sleep 3
curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash

sudo chmod a+x /home/pi/TalkingFish/fish_code/_tools/raspberry_pi/boot.sh
sudo chmod 777 /home/pi/TalkingFish/fish_code/billy_bass_controller/downloads
sudo apt-get install python-pygame
#curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash

echo "\r\n\r\n\r\n"
echo "your dependencies are setup!"
echo "Now it is time to make sure the Pi runs the proper script on boot..."
echo "\r\n\r\n\r\n"
sleep 5
echo "Please enter the following command to then paste the code line into:"
echo "sudo crontab -e"
echo ""
echo "add the following line to the end of the next file: "
echo ""
echo "@reboot bash /home/pi/TalkingFish/fish_code/_tools/raspberry_pi/boot.sh &"
echo ""
echo ""
sleep 5
echo "ONCE YOU HAVE COMPLETED THE PROMPTS ABOVE, reboot your system"
