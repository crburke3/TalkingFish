echo "Sleeping for 30 seconds to allow boot"
sleep 30
echo "moving to fish_code dir"
cd /home/pi/TalkingFish/fish_code
pwd
echo "pulling latest code..."
git stash
git pull --force
echo "installing dependencies..."
pip3 install -r _tools/raspberry_pi/requirements.txt

# DO NOT FUCK WITH tHE STUFF UP TOP
echo "starting fish!"
python3 main.py &
