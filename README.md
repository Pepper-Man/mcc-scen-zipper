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

You may wish to edit line 10 of the file to add/remove folder paths to include or exclude extra tags from the zip