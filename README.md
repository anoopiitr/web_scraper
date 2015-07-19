# web_scraper
Python script for web scraping

Assumptions:
    File name to store each paste is taken from its download url.

Steps to run the script and check the output:
    1- Open console and change directory to location from where the script is supposed to be run.
    2- Clone this repo by running the command : git clone git@github.com:anoopiitr/web_scraper.git
    3- Change directory to web_scraper by running: cd web_scraper 
    4- Run the script web_scraper.py like below-
         python web_scraper.py [paste_dir_path]

       If paste_dir_path is supplied as a param and is a valid directory path in local file system
       this is where the pastes will be stored

       If paste_dir_path is not provided the default directory for storing pastes will be 'pastes_dump_dir'
       and this will be located where the script is placed before running.
    5- Nevigate to the appropriate directory to check the paste data. 

