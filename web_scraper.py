# -*- coding: UTF-8 -*-

import os
import sys
import io
import codecs
import urllib2
from bs4 import BeautifulSoup

TARGET_DATA_DIR = 'pastes_dump_dir'
BASE_URL = 'http://pastebin.com'
DOWNLOAD_LINK_PARTIAL= '/download.php?i='


def get_paste_store_loc(target_data_dir):
    """
    This function computes the location of pastes based on param passed
    If no valid location in local file system is found, default location
    is pastes_dump_dir where the script is located

    @param target_data_dir: Name of the paste dump directory (configurable)

    Returns: Absolute path of paste storage
    """
    #Validating and returning the pastes download directory path
    #if supplied by user as parameter while running the script
    if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):
        return sys.argv[1]

    #If preffered download location is not provided, default location
    #will be scrap_data_dir in same location from where script is run
    default_target_dir = os.path.join(os.getcwd(), target_data_dir)
    if not os.path.exists(default_target_dir):
        os.makedirs(default_target_dir)

    return default_target_dir


def write_to_file(paste_store_loc, file_name, paste_content):
    """
    This function writes the content of a paste to a given file and
    its location if file not already present, its created

    @param paste_store_loc: Location of the file where all pastes stored
    @param file_name: Name of the file where paste will be saves
    @param paste_content: Actual paste content
    """
    #Formulating absolute path to write each paste content
    absolute_paste_loc = os.path.join(paste_store_loc, file_name)

    #Writing paste content into file
    with io.open(absolute_paste_loc,
                    encoding='utf-8',
                    mode='w+') as file_obj:
        file_obj.write(unicode(paste_content, encoding='utf-8'))


def paste_downloader(paste_store_loc):
    """
    This function does the actual job of downloading the paste content
    @Param paste_store_loc: Location of dir where all downloaded pastes
        are supposed to be stored
    """
    soup = BeautifulSoup(urllib2.urlopen(BASE_URL + '/archive').read())
    list_of_tr = soup('table', {'class' : 'maintable'})[0].find_all('tr')

    for paste_item in list_of_tr :
        a_tag = paste_item.find('a')
        link = a_tag and a_tag['href'].strip('/')
        if link:
            download_url = BASE_URL + DOWNLOAD_LINK_PARTIAL + link
            paste_content = urllib2.urlopen(download_url).read()
            write_to_file(paste_store_loc, link, paste_content=paste_content)


if __name__ == '__main__':

    #Getting the download directory where where pastes will be stored
    paste_download_dir = get_paste_store_loc(target_data_dir=TARGET_DATA_DIR)

    #Downloads and store all the pastes listed on given page
    paste_downloader(paste_store_loc=paste_download_dir)
