#!/usr/bin/env python

import yaml
import sqlite3
import os
import psutil
from pathlib import Path


def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied,
                psutil.ZombieProcess):
            pass
    return False


def main():
    # check if darktable is running
    if checkIfProcessRunning("darktable"):
        raise Exception(
            'Darktable is running, cannot work on database file. Please close darktable and try again.'
        )
    # loda top tag from config.yml
    with open(r'config.yml') as file:
        toptag = yaml.load(file, Loader=yaml.FullLoader)['toptag']
    # load lens dict from lenses.yml file
    with open(r'lenses.yml') as file:
        lenses = yaml.load(file, Loader=yaml.FullLoader)

    # database location
    home = str(Path.home())
    dtconf = ".config/darktable"

    # DB FILE COMES HERE
    dbfile = "library.db"
    tagdb = "data.db"

    # get tag IDs
    tagconn = sqlite3.connect(os.path.join(home, dtconf, tagdb))
    tagc = tagconn.cursor()
    tagc.execute('SELECT id, name FROM tags WHERE name like "' + toptag + '%"')
    t = tagc.fetchall()
    # convert to dict
    tags = {i[1].split('|')[1]: i[0] for i in t}
    # close db file
    tagconn.close()

    # connect to image database
    dbconn = sqlite3.connect(os.path.join(home, dtconf, dbfile))
    dbc = dbconn.cursor()
    # iterate over lenses fro myaml file
    for lens in lenses.keys():
        # get IDs of tagged images
        dbc.execute('SELECT imgid FROM tagged_images WHERE tagid=' +
                    str(tags[lenses[lens]['tag']]))
        img_ids = dbc.fetchall()
        # iterate over images and add lens info
        for img in img_ids:
            # fill in lens
            dbc.execute('UPDATE images SET lens="' +
                        str(lenses[lens]['Model']) + '" WHERE id=' +
                        str(img[0]))
            # fill in focal length
            dbconn.commit()
            dbc.execute('UPDATE images SET focal_length=' +
                        str(lenses[lens]["FocalLength"]) + ' WHERE id=' +
                        str(img[0]))
            dbconn.commit()
            # fill in aperture
            dbc.execute('UPDATE images SET aperture=' +
                        str(lenses[lens]["MaxAperture"]) + ' WHERE id=' +
                        str(img[0]))
            dbconn.commit()
        print(lenses[lens]['Model'] + " done")
    dbconn.close()


if __name__ == "__main__":
    main()
