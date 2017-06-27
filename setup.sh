sudo apt-get install python-setuptools
sudo easy_install pip
sudo pip install pymongo
sudo apt-get install curl
curl -O https://fastdl.mongodb.org/osx/mongodb-osx-x86_64-3.4.5.tgz
tar -zxvf mongodb-osx-x86_64-3.4.5.tgz
mkdir -p mongodb
cp -R -n mongodb-osx-x86_64-3.4.5/ mongodb

