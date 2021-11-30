This project aims to translate *Uma Musume Pretty Derby* through (mainly) Unity asset edits.  
Translation progress can be checked on the [overview][tl-progress].

This is based on the DMM version of the game. If you can figure out how to run it on other versions, it may (should) work as well, but no support is provided right now.

# Disclaimer

This tool collection only changes text to translate it and it is *my belief* this is harmless and unlikely to be an issue. [^1]  
**Nonetheless such edits are of course againt cygames/Umamusu TOS so proceed at your own risk!**

[^1]: cygames has a relatively good track record in leaving non-cheating, non-damaging tools and users alone in my experience.

# Install 

### Requirements
1. Install [Python](https://www.python.org/downloads/) 3.6+ and [UnityPy][]
1. (Optional but recommended) Download all game data through the game menu
1. Clone or download this project

### Usage
1. From project root: `python src/import.py -O`
    - If you only want to install specific things, see [id-structure.md](id-structure.md) and use: `python src/import.py -O -g <group> -id <id>`
1. **Dialogue**: Copy `dat` folder to game datafolder and overwrite (Usually `C:\Users\<name>\AppData\LocalLow\Cygames\umamusume`)
1. **UI**: Copy the [localify folder](localify) to your Uma Musume install dir (where the `Umamusume.exe` and *[localify][umamusume-localify]'s `version.dll`* are)
1. **Skills and other variable text**: See the [db-translate project]

If you want to add additional translations through deepl, or contibute your own, see [translating.md](translating.md)

# Script info

All scripts are made to be run from the root dir, i.e: `py src/script.py -opt val`  
Arguments can be given to all and it is recommended you do so, processing the smallest amount of files you're comfortable with at a time.  
For arg info run a script with the `-h` arg or just look at the code. Most are very similar.

## Main / Stories

script | desc
---|---
filecopy | Simply copies files from the game dir to the project dir for backup. These will also be used by some other scripts where useful.
restore-files | Downloads fully fresh files from cygames servers, in case of mess ups
extract | Loads game data and writes relevant data to a local folder, ready to be translated. Creates *Translation Files*
import | The reverse; loads *Translation Files* and writes them back to game assets for importing into the game
machinetl + deepl-translator.user.js | In tandem, provide a way to translate *Translation Files* with deepl. Install the userscript in your browser. Run the python file first, then go to the deepl site and use your userscript manager's menu to connect and wait until python exits. This userscript setup is temporary (famous last words)
names | Simply translates names in *Translation Files* using data from the [db-translate project][]
textprocess | Processes dialogue text in *Translation Files* in various ways. Most immediate manual use is adjusting lengths of lines for newline splits.
common | Not a script. Is used by the other files and holds shared functions and data.

### Common Arguments
Most scripts take these arguments, given as `-arg <opt>`:

arg|desc
---|---
h | Print basic usage information. Use this to see script-specific options
g | Process specific group
id | Process specific id
l | Limit processing to given number of files
O | `extract.py`: overwrite files in extract folder `import.py`: (over)write directly to game dir instead of `dat/`
src | Define umamusu game dir (defaults to the usual location in `LocalLow`)
dst | Define root dir to save output in (defaults to `dat/` for `import.py` and `translations/` for `extract.py`)

For g and id see [id-structure.md](id-structure.md)

> An example to extract Special Week's story: `python src/extract.py -g 04 -id 1001`

## Others

For details run with `-h` or check the code.

script | desc
---|---
static/manage | Small tool to manage localify's data for translating static strings. Requires use of [umamusume-localify][]. Note this is a module-script, run as: `python -m src.static.manage [-opts]`

# Contribute

To contribute translations, see [translating.md](translating.md) (deepl dumps are accepted!)  
For dev contributions, open a PR or Issue.  
**Both are extremely welcome!**

# Thanks to

[UnityPy][]  
[The original umamusume-db-translate](https://github.com/FabulousCupcake/umamusume-db-translate)  
[umamusume-localify][]  
[Unofficial Umamusume Discord server](https://discord.gg/umamusume)  
[All the translators][tl-progress]

[UnityPy]: https://github.com/K0lb3/UnityPy
[umamusume-localify]: https://github.com/GEEKiDoS/umamusume-localify
[db-translate project]: https://github.com/noccu/umamusume-db-translate

[tl-progress]: tl-progress.md