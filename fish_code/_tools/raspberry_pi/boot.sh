echo "Setting up Wifi passwords"
sudo cp -f ~/TalkingFish/fish_code/_tools/raspberry_pi/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf

echo "Sleeping for 10 seconds to allow boot"
sleep 10
echo "moving to fish_code dir"
cd /home/pi/TalkingFish/
sudo chown -R pi .git/
cd fish_code/
pwd
echo "pulling latest code..."
git config --global user.email "fish@billybass.com"
git config --global user.name "Billy bass"
git stash
git pull --force
echo "installing dependencies..."
pip3 install -r _tools/raspberry_pi/requirements.txt

# DO NOT FUCK WITH tHE STUFF UP TOP
echo "starting fish!"
python3 main.py
