# Add Manual Vintage Lens Information to the Darktable Database #
Quickly hacked together for adding vintage manual lens info to the darktable database.

This can - of course - be solved by using tags, however I wanted to have these lenses and their infos in the "collect image" feature in darktable.

Lens information is stored in `lenses.yml` and can be easily modified to include other lenses.

This little script goes through the darktable library sqlite database and searches for a certain hierarchical tag defined in `config.yml` - in my case this is Altglas| as the top tag. Lenses get tagged as e.g. Altglas|voigtländer35f2
The script looks for files with these tags and adds focal length, maximum aperture value and the lens name to the database, based on information stored in `lenses.yml`.

The workflow would then be:
1. Import images
2. Add hierarchical lens tags to images
3. Close darktable
4. Run script
5. Re-open darktable

## CLOSE DARKTABLE BEFORE USING THIS SCRIPT ##

### Exported Images ###
Upon exporting these informations are not stored in the generated output, since the raw files remain untouched. Adding lens info the output files can be done using tag_output.py If darktable is configured to add tags to the exif data of exported files, the script will find the tag and add the information to the exif data.
