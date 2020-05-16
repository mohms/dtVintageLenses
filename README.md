# Add Manual Vintage Lens Information to the Darktable Database #
Quickly hacked together for adding vintage manual lens info to the [darktable](https://github.com/darktable-org/darktable)database.

This can - of course - be solved by just using tags, however I wanted to have these lenses and their infos in the "collect image" feature in darktable. This method uses tags for telling the script which image needs which lens info added.

Lens information is stored in `lenses.yml` and can be easily modified to include other lenses.

This little script goes through the darktable library sqlite database and searches for a certain hierarchical tag defined in `config.yml` - in my case this is `Altglas` as the top tag. Lenses get tagged as e.g. `Altglas|voigtländer35f2`
The script looks for files with these tags and adds focal length, maximum aperture value and the lens name to the database, based on information stored in `lenses.yml`.

The workflow would then be:
1. Import images
2. Add hierarchical lens tags to images
3. Close darktable
4. Run script
5. Re-open darktable

*No changes* are written to the RAW files, everything happens just in darktables database. Database entries for all other files remain unchanged.

Exported images lack lens info, currently working on a script using embedded tags in the exported image to add the proper lens info after exporting.

## CLOSE DARKTABLE BEFORE USING THIS SCRIPT ##

