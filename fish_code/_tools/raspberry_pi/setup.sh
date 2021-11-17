sudo chmod a+x /home/pi/TalkingFish/fish_code/_tools/raspberry_pi/boot.sh
echo "add the following line to the end of the next file: "
echo ""
echo "@reboot bash /home/pi/TalkingFish/fish_code/_tools/raspberry_pi/boot.sh"
echo ""
echo ""
sleep 2

echo "Press any key and the ENTER to continue"
while [ true ] ; do
read -t 3 -n 1
if [ $? = 0 ] ; then
exit ;
else
echo "waiting for the keypress/ENTER"
fi
sudo crontab -e
done
