git clone https://github.com/UluBeyCRS/WEB-HACK-K-T.git

cd WEB-HACK-K-T

# Kali Linux 

sudo apt update && sudo apt upgrade -y

sudo apt install python3 python3-pip -y

sudo apt install -y \
    dirb \
    sqlmap \
    gobuster \
    sublist3r \
    nmap \
    wpscan \
    set \
    theharvester \
    curl \
    git

pip3 install requests

nano web_hack_kit.py

chmod +x web_hack_kit.py

sudo python3 web_hack_kit.py

# Termux

pkg update && pkg upgrade -y

pkg install -y \
    python \
    python-pip \
    git \
    curl \
    nmap \
    openssl-tool \
    wget \
    termux-api

pip install requests

git clone https://github.com/sqlmapproject/sqlmap.git
echo "alias sqlmap='python ~/sqlmap/sqlmap.py'" >> ~/.bashrc

nano web_hack_kit.py

python web_hack_kit.py
