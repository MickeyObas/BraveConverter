# Welcome to the BraveConvert tool :)

> What is this?

I'm glad you asked. This program receives your csv file which is formatted to store NFT entries and their correct fields- *I hope*- and generates a sha-256 hashed JSON file for every single one of them.

> How do I use it?

1. Clone the repository using the command `git clone https://github.com/MickeyObas/BraveConverter.git`
2. Place your csv file inside the forked folder.
3. Open the folder on your command terminal or move into its directory.
4. Create a virtual environment.
```
# Let's install virtualenv!
pip install virtualenv

# Then we create our virtual environment
virtualenv envname
```
5. Now activate the virtual environment.
`envname\scripts\activate`
6. Install the required dependencies by running `pip install -r requirements.py` on your command line.
7. Run `braveconvert.py <filename>` on the command line where- `<filename>` is actually your csv file name in quotes and not angle brackets.

I know right, it's THAT easy. Your files have been generated, hashed and properly recomposed into a new csv file.




