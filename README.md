# WikiCLI
A little program that gives you a wikipedia summary of a chosen topic. If you need to provide a disambiguation, a list of options will be printed and all you need to do is search again using a more specific query.

# Usage
You can download the repo either as a zip through the browser or by cloning it through git (the preferred option).

## ZIP Download
Click the "Download as ZIP" button to the right and then navigate to the folder in which the file was downloaded (thriugh the terminal) and execute the following command
```
unzip WikiCLI.zip
```

## Git clone
Execute the following command
```
git clone https://github.com/SamTebbs33/WikiCLI.git
```

In the future, you will be able to download updates by executing
```
git pull
```
from the cloned directory.

## Installing the python script
Navigate into the downloaded folder (or unzipped folder if you downloaded the zip) and execute
```
python setup.py install
```
(You may need to prefix the command with `sudo`).

Now you can execute the script by typing `wiki.py`, followed by a search query. This query can either consist of one word, or several separated by spaces.
```
wiki.py Linus Torvalds
=====
Linus Benedict Torvalds (/ˈlaɪnəsˈtɔrvɔːldz/; Swedish: [ˈliːn.ɵs ˈtuːr.valds]; born December 28, 1969) is a Finnish American software engineer, 
who was the principal creator behind the development of the Linux kernel; that became the kernel for several other operating systems, 
such as GNU and years later Android and Chrome OS. He also created the distributed revision control system git. ...
=====
```
