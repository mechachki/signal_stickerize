# Signal Stickerize - prepare images for signal sticker import

A python script to batch edit images so they abide to Signal's sticker guidelines:
1. 512x512px size
1. 16px transparent margins on all sides

# Usage
You have a few options on how to run it:
  * execute it inside your IDE of choice
  * from commandline interface such as cmd - navigate using cd to the folder where you saved the script and run either one of these 2 commands:
    * run ```python signal_stickerize.py``` and follow instructions
    * run ```python signal_stickerize.py [source folder] [target folder]``` (this one just ommits the instructions asking you to enter source and target folder)

When entering source and target folders make sure you use full path, e.g. ```C:/users/my_username/pictures/stickers```
    
# Requirements
* python (tested on 3.8, should work in most 3.* environments) 
* python image library (PIL)
  * run ```pip install pillow``` in cmd to download it
