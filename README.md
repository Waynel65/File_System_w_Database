# File_System_w_Database
This repo is for the purpose of applying for Anubis's TA position

https://www.youtube.com/watch?v=pPSZpCVRbvQ
https://haseebmajid.dev/blog/simple-app-flask-sqlalchemy-and-docker

    Part 1. Set Up the Mysql Database with Docker
    
    0. In the project's root directory, run `docker compose up`
    1. If everything works correctly, you should see something like:
    
        `[System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.30'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.`
        
    2. If not, I am probably screwed

    Part 2. Running the Flask app and connect to the database
    
    0. Ensure you have python3 installed
    1. cd into the `app` folder
    2. Create a virtual environtment with `python3 -m venv file_env`
    3. Acticate the virtual environment with `source file_env/bin/activate`, or `file_env/Scripts/activate` if you are using powershell
    4. Install the dependencies with `pip3 install -r requirements.txt`
    5. Run the server with `flask run`
    6. See the homepage on your browser with the URL: `http://127.0.0.1:5000/` and have fun with the ancient file downloader!
