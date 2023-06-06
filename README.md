# h3-scen-zipper
Python script for zipping all tags referenced by H3 scenarios, for easy sharing

# Requirements
[Python](https://www.python.org/) - preferably 3.10.6 or newer, older versions not tested

# Usage
* Place the .py file in your root **H3EK** folder
* Compile your scenario once with **tool build-cache-file**
* Run the .py file from CMD with **py tags_grabber.py**
* Enter the exact name of your scenario tag without extension. For example, **100_citadel** for The Covenant
* Wait a few seconds for the zipping process to complete
* You will find the zip file in your root **H3EK** directory, with the same name as the scenario
* The zip file can now be shared - the contents can simply be extracted into **H3EK\tags**

# Warning
* If you are a recipient of the zip, please be sure to back up your **tags** folder before unzipping

# Notes
* This script ignores any uneditied/bungie-made tags (by checking for a 2007 modified date) to cut down on filesize and unnecessary data transfer
* You may wish to edit line 10 of the file to add/remove folder paths to include or exclude extra tags from the zip
* If a tag referenced by the scenario is missing, it will not be added and you will see output informing you of the missing tag path
