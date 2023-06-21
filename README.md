# mcc-scen-zipper
Python script for zipping all tags referenced by scenarios, for easy sharing.
Supports all MCC titles except CE

# Requirements
[Python](https://www.python.org/) - preferably 3.10.6 or newer, older versions not tested

# Usage
* Place the .py file somewhere on your pc (don't put it in a protected folder!)
* Compile your scenario once with **tool build-cache-file**
* Run the .py file from CMD with **py tags_grabber.py**
* Click the first **browse** button, and choose the root editing kit directory of the relevant engine, e.g. your **H3EK**, **HREK** folder
* Click the second **browse** button, and simply navigate to and select your **.scenario** file
* Click the third **browse** button, and navigate to a folder of your choice to save the zip file to
* Hit go!
* Wait a few seconds for the zipping process to complete
* You will see an output detailing the success, the number of missing tags, and the file location of the generated zip if you forgot
* The zip file can now be shared - the contents can simply be extracted into **H3EK\tags**
* If you wish to see the details of any missing tags, you will find an **output.txt** in the same folder as the python file

# Warning
* If you are a recipient of the zip, please be sure to back up your **tags** folder before unzipping

# Notes
* This script ignores any unedited (bungie/343-made) tags (by checking for the modified date) to cut down on filesize and unnecessary data transfer
* You may wish to edit line 15 of the file to add/remove folder paths to include or exclude extra tags from the zip