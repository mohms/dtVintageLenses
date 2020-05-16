# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sqlite3
import subprocess
dbfile = "/home/malte/.config/darktable/library.db"
conn = sqlite3.connect(dbfile)
c = conn.cursor()
#%% get list of files
c.execute('SELECT filename, film_id FROM images WHERE lens="None";')
flist = c.fetchall()
#%%

for e in flist:
    fid = e[1]
    c.execute('SELECT folder FROM film_rolls WHERE id="'+str(fid)+'"')
    folder = c.fetchone()[0]
    # execute 
    fname = e[0]
    f = str(folder+"/"+fname+".xmp")
    print("Working on "+f)
    # call external script
    subprocess.call(["exif_fujinon", f])
print("Done, reload images")