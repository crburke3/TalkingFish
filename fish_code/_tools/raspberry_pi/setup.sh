sudo chmod a+x /home/pi/TalkingFish/fish_code/_tools/raspberry_pi/boot.sh
echo "add the following line to the end of the next file: "
echo ""
echo "@reboot bash /home/pi/TalkingFish/fish_code/_tools/raspberry_pi/boot.sh"
echo ""
echo ""
sleep 2

echo "Please enter the following command to then paste the code line into:"
echo "sudo crontab -e"
