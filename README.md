# Add Manual Vintage Lens Information to the Darktable Database #
Quickly hacked together for adding vintage manual lens info to the darktable database.

Lens information is stored in ```lenses.yml```````´

## CLOSE DARKTABLE BEFORE USING THIS, IT MODIFIES THE DATABASE FILE ##

This little script goes through the darktable library sqlite database and searches for a certain hierarchical tag defined in ````````````config.yml`` - in my case this is Altglas| as the top tag. Lenses get tagged as e.g. Altglas|voigtländer35f28 
The script looks for files with these tags and adds focal length, maximum aperture value and the lens name to the database.
Upon exporting these informations are not stored in the generated output, as the raw files remain untouched. Adding lens info the output files can be done using tag_output.py If darktable is configured to add tags to the exif data of exported files, the script will find the tag and add the information to the exif data.
