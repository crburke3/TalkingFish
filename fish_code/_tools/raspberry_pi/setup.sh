sudo chmod a+x /home/pi/TalkingFish/fish_code/_tools/raspberry_pi/boot.sh
sudo chmod 777 /home/pi/TalkingFish/fish_code/billy_bass_controller/downloads
#curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash


echo "add the following line to the end of the next file: "
echo ""
echo "@reboot bash /home/pi/TalkingFish/fish_code/_tools/raspberry_pi/boot.sh &"
echo ""
echo ""
sleep 2

echo "Please enter the following command to then paste the code line into:"
echo "sudo crontab -e"
