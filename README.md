
# you can access this bot live here:  https://t.me/cryptto_ops_bot 

if you cannot setup, hire a dev to assist you here: https://freelancer.com/u/Beannsofts or you can follow the below steps to setup.  

Access Bybit Documentation here:  https://bybit-exchange.github.io/docs/inverse/#t-introduction

Join our Discord Server https://discord.gg/bwCJTVDbRr for Assistance and Updates

##The app architecture is Python Flask Factory Pattern.  It's ready for production.  


CRYPTTOPS BYBIT BOT INSTALLATION INSTRUCTIONS

Part 1: Installing Python3.8 Environment

Step 1: Install Python Dependencies
Run the following commands in a terminal window
sudo yum -y update
sudo yum -y groupinstall "Development Tools"
sudo yum -y install openssl-devel bzip2-devel libffi-devel sudo yum -y install gcc

Step 2: Download latest Python 3.8 Archive
Now download the latest archive of Python 3.8 release.
sudo yum -y install wget
Wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz
Extract the package.
tar xvf Python-3.8.3.tgz
Change the created directory:
cd Python-3.8*/

Step 3: Install Python 3.8 on CentOS 7
Setup installation by running the configure script.
./configure  --enable-optimizations
Initiate compilation of Python 3.8 on CentOS 7.
sudo make altinstall
If this was successful, you should get a message like below:
Collecting setuptools Collecting pip
Installing collected packages: setuptools, pip Successfully installed pip-19.2.3 setuptools-41.2.0

Step 4: Check Python 3.8 on CentOS
Confirm that the installation of Python 3.8 on CentOS 8 / CentOS 7 was successful.
python3.8 --version
If this was successful, you should get a message like below:
Python 3.8.3
Confirm that Pip is also installed.
pip3.8 --version
If this was successful, you should get a message like below:
pip 19.2.3 from /usr/local/lib/python3.8/site-packages/pip (python 3.8)


Part 2: Installing Postgres Database
Run the following commands on a terminal window to install Step 1: Add PostgreSQL Yum Repository to CentOS 7 Run the following command as a single line
sudo yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-
7-x86_64/pgdg-redhat-repo-latest.noarch.rpm

sudo yum -y update sudo reboot

Step 2: Install PostgreSQL 13 on CentOS 7
After successfully adding the repository, you can proceed to install PostgreSQL 13 on CentOS 7.

Confirm the list of enabled repositories with the following command
sudo yum repolist

Your output should be something similar to this
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
    • base: mirror.alpha-labs.net
    • extras: artfiles.org
    • updates: mirror.plustech.de

pgdg-common/7/x86_64 PostgreSQL common RPMs for RHEL/CentOS 7 - x86_64	
360
pgdg10/7/x86_64
PostgreSQL 10 for RHEL/CentOS 7 - x86_64
789
pgdg11/7/x86_64
PostgreSQL 11 for RHEL/CentOS 7 - x86_64
838
pgdg12/7/x86_64
PostgreSQL 12 for RHEL/CentOS 7 - x86_64
414
pgdg13/7/x86_64
PostgreSQL 13 for RHEL/CentOS 7 - x86_64
140
pgdg95/7/x86_64
PostgreSQL 9.5 for RHEL/CentOS 7 - x86_64
698
pgdg96/7/x86_64
PostgreSQL 9.6 for RHEL/CentOS 7 - x86_64
759
updates/7/x86_64
CentOS-7 - Updates
1,134

repolist: 15,615





Now install PostgreSQL 13 packages on your CentOS 7 VPS using the following command.
sudo yum -y install postgresql13 postgresql13-server

Step 3: Initialize and start database service
After fresh installation of PostgreSQL 13 on CentOS 7 initialization is required.Run this command:
sudo /usr/pgsql-13/bin/postgresql-13-setup initdb

Output should be something similar to this.
Initializing database ... OK

Start the PostgreSQL database service. Run this command.
sudo systemctl start postgresql-13

Check the service status to confirm it is running. Run this command.
systemctl status postgresql-13

Output should be something similar to this. Ensure you see Active(running)

    • postgresql-13.service - PostgreSQL 13 database server
    Loaded: loaded (/usr/lib/systemd/system/postgresql-13.service; enabled; vendor preset: disabled)
    Active: active (running) since Thu 2020-07-09 23:35:30 CEST; 37s ago
 	Docs:  https://www.postgresql.org/docs/13/static/
   Process: 1860 ExecStartPre=/usr/pgsql-13/bin/postgresql-13-check-db-dir ${PGDATA} (code=exited, status=0/SUCCESS)
Main PID: 1865 (postmaster)
 	Tasks: 8 (limit: 12210)
    Memory: 17.3M
    CGroup: /system.slice/postgresql-13.service
 	├─1865 /usr/pgsql-13/bin/postmaster -D /var/lib/pgsql/13/data/
 	├─1867 postgres: logger
 	├─1869 postgres: checkpointer
 	├─1870 postgres: background writer
 	├─1871 postgres: walwriter
 	├─1872 postgres: autovacuum launcher
 	├─1873 postgres: stats collector
 	└─1874 postgres: logical replication launcher

Jul 09 23:35:30 centos-01.computingforgeeks.com systemd[1]: Starting PostgreSQL 13 database server...
Jul 09 23:35:30 centos-01.computingforgeeks.com postmaster[1865]: 2020-07-09 23:35:30.180 CEST [1865] LOG: redirecting log output to logging collector process Jul 09 23:35:30 centos-01.computingforgeeks.com postmaster[1865]: 2020-07-09 23:35:30.180 CEST [1865] HINT: Future log output will appear in directory "log".
Jul 09 23:35:30 centos-01.computingforgeeks.com systemd[1]: Started PostgreSQL 13 database server.


Enable the service to start when the system is reboted.Run this command
sudo systemctl enable postgresql-13
Output should be something similar to this.
Created symlink from /etc/systemd/system/multi- user.target.wants/postgresql-13.service to
/usr/lib/systemd/system/postgresql-13.service.
Step 5: Enabling remote Database connections.
Edit the file /var/lib/pgsql/13/data/postgresql.conf and set Listen address to your server IP address or “*” for all interfaces. Run the following commands.

cd

sudo nano /var/lib/pgsql/13/data/postgresql.conf

Look for the line that reads listen_address and place your server IP there as shown below. Press Ctrl
+ X to save the changes and exit.
listen_addresses = 'your VPS IP’

Also set PostgreSQL to accept remote connections Run the following command.
sudo nano /var/lib/pgsql/13/data/pg_hba.conf

Also set PostgreSQL to accept remote connections Run the following command. Add the following lines at the end of the file then press Ctrl + x to save and exit.In the second command replace 172.20.11.0 with your server IP.
# Accept from anywhere (not recommended) host all all 0.0.0.0/0 md5

# Accept from trusted subnet (Recommended setting) host all all 172.20.11.0/24 md5

Restart the database service after saving the changes. Run the following command.
sudo systemctl restart postgresql-13













Part 3:Creating the Bot database and Running the bot
Run the following commands on a terminal window to install
sudo -u postgres -i psql

The above command will enter us to postgres prompt. Password is your VPS Password. Run the next command in the postgres prompt to create a database.
CREATE DATABASE flask_api;
 	CREATE USER flask_api WITH PASSWORD ‘flask_api’;
 	GRANT ALL PRIVILEGES ON DATABASE flask_api TO flask_api;
\q

We need to change the telegram token. Head to telegram and search for Botfather. You can access bot father through the Link

Create a bot from botfather and obtain the bot token. Copy the bot token. Install visual studio code on your client computer and use it to open the file BinanceSpotAutomated.py located in the project folder you extracted.


NB: VIsual Studio can be installed from the link: https://code.visualstudio.com/download

























Locate line 481 like the image above and highlight the bot token. Press ctrl + F to find all instances of the bot Token. Then press ctrl + H to replace all the instances of that token with the token you just created from the telegram bot father.

We now copy the project files into the server using FileZilla. You need to install fileZilla to your computer. The links to installing fileZilla on windows operating system is below:

https://filezilla-project.org/download.php?platform=win64

Once you have installed fileZilla to your computer, Extract the project files to a folder. With Filezilla, Enter VPS IP, Password, Port of the Like in image below:









Click QuickConnect and you will see files on the VPS on the right and files on your computer on the left.
On the left, locate where you extracted the project. Right click on it and Click, Upload to upload the file to the server. If a replace popup appears , Click, Continue to proceed replacing file on the VPS server. That’s it. You have uploaded the project.

Login to the server through on a terminal and type the following command to change the directory into the uploaded code files.


VPS.
N/B: Replace <Folder of the project> with the name of the folder you just uploaded to the

cd <FOLDER OF THE PROJECT>
Run the following command on the terminal to create the required database tables for the bot to run
sudo -u postgres -i psql flask_api<bybit
Create a python virtual environment through the following commands and activate the environment
python3.8 -m venv venv source venv/bin/activate
pip3 install -r requirement-final.txt python3.8 bybit.py

The last command runs your bot. Head over to the telegram bot you created and start the bot with the start command.



CRYPTTOPS BYBIT BOT USAGE INSTRUCTIONS
CryptOps Bot Documentation Manual
    1. Access samplebot via the link: https://t.me/cryptto_ops_bot
    2. Get your Bybit Keys : API Key and Secret. Instructions on Bybit Website https://www.bybit.com/app/user/api-management
    3. With API key and secret above, capture them with our Bot and Click Done Button to process the request.
    4. Once Verified, you can go to Verification and Verify those Keys.
    5. You can Either Trade Manually on Telegram or Automatically via Trading-view for symbols: BTCUSD, EOSUSD, XRPUSD and ETHUSD.


        1. Manual Trading.
            1. Click Manual Trading Button on the Bot. There are several options to do that. You can either Buy, Sell, Set Leverage, View your positions as well as close your Bybit Positions using our Bot. Either of the trades can be Market or Limit orders.
                1. Here is an Example Market Order, Buy direction. You can change it to side: is ‘sell’ if you want to place a sell order. The amount is in percentage of your Bybit balance. If you place a Limit Order, you need to place the percentage for takeProfit or stopLoss or trailingStop or new_trailing_active. My token value on this template is Ben1234. Replace it with token given to you by our agents.
                    1. {"type": "Market", "side": "Buy", "amount": "97", "symbol": "BTCUSD","Leverage":"10", "takeProfit" : "None","stopLoss":"None","trailingStop":"None", "new_trailing_active":"None", "token":"Ben1234", "TelegramID":"1093054762"}
                    2. All details are on every button you press on the Bot.
                2. Automated Trading.
                    1. Click Automated Trading Button on the Bot. There are several options to do that. You can either Buy, Sell, Set Leverage, View your positions as well as close your Bybit Positions using our Bot right using TradingView alerts. Just like in manual trading. However, the trading templates you pass them on the message section of TradingView Chart Alert settings.
                    2. Once bot receives this TradingView message, it consequently places respective order on Bybit.
                    3. On Alert settings of tradingview you also need pass the webhook url in the format guided by the bot:
                    4. You will find a webhook url link for every automated process request when you press the respective buttons. E.g. Buy, Sell, Leverage, Close.



##setup python 3.8 on centos 8 redhat:  https://computingforgeeks.com/how-to-install-python-on-3-on-centos/

##Kill proceses in centos: 

sudo netstat -ntlp | grep LISTEN #YOU WILL see the port numbers 

sudo lsof -i:6379  #hAVING gotten the command from above 

sudo kill -9 1005 $ 9 is a glag enforcer. 1005 is PID of the process gotten above
 
##Interacting with Postgres

sudo /usr/pgsql-10/bin/postgresql-10-setup initdb
[sudo] password for mutemia: 
Initializing database ... OK

#su - postgres  or sudo -i -u postgres
This will enter us to postgres prompt
Password is blablabla #caps for this is inverted

#Rstart postgresql service on CentOS RHEL
service postgresql-10 restart

#psql postgres 
Enter into postgres prompt if in root user mode

#vi /var/lib/pgsql/10/data/pg_hba.conf
Location of config file for postgres 10

INteracting With Postgres Dtabase: 
show databases
#\l
SElect a Database: 
#\c flask_api; #Flask_API is the database name :
Display Tables in a Database: 
#\dt
# Our schema is named :public 
	
#List Table Data
SELECT * FROM information_schema.columns WHERE TABLE_NAME = 'asset';
#Display Table Data --- SQL syntax rules apply:  
SELECT * FROM asset;

_________________________________________________________________________________________________________________________________________

###WE Need Start the Project in 4 to 5 CMD windows  
#In All Cases Start virtual environment 
#-_____________________________________

#python3 -m venv python3-virtualenv

# source python3-virtualenv/bin/activate

$ mkvirtualenv -p /path/to/python3 flask_react_spa
$ pip install -r requirements.txt
$ pip install -r requirements-dev.txt  # for tests and sphinx docs

Window 1
___________________________
python manage.py db upgrade
python manage.py db fixtures fixtures.json
python manage.py run #Default ENV = dev 
#FLASK_ENV=prod python manage.py run 
#Above command is for running production env

Window 2
________________________________
npm run start

Window 3
_________________________________________
python manage.py celery worker

Window 4
____________________________________________

python manage.py celery beat

Window 6
___________________________________________

# set up database
$ sudo -u postgres -i psql
postgres=# CREATE USER flask_api WITH PASSWORD 'flask_api';
postgres=# CREATE DATABASE flask_api;
postgres=# GRANT ALL PRIVILEGES ON DATABASE flask_api TO flask_api;
postgres=# \q  # (quit)

Window 7
__________________________________________________

make docs #Documentation on the APp


_____________________________________________________________________________________________________________________________________________________________________________


______________________________________________________________________________________________________________________________________________________________________________________________________________________________________
