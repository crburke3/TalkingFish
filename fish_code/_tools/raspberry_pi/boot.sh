echo "moving to fish_code dir"
cd ../../
pwd
echo "pulling latest code..."
git stash
git pull --force
echo "installing dependencies..."
pip3 install -r _tools/raspberry_pi/requirements.txt
echo "starting fish!"
python3 main.py