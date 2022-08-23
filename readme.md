Autosave editor for [Slay the Spire](https://store.steampowered.com/app/646570/Slay_the_Spire/).

The code has been written as modular as possible for easy customization.

Use with caution, as it can really ruin the fun. But for me, sometimes I prefer to extract all the fun as fast as possible and then begone with my life.

## How to
- Install python3 
- Inside `main.py`, Change the `save_file_path` according to your game installation so that it points to the autosave file. 
  - The autosave file is named with this format: `<Name of the character>.autosave`, for example `DEFECT.autosave`
  - By default it will be inside the default steam folder `..../Steam/steamapps/common/SlayTheSpire/saves`
  - I used Linux, so if you use Windows you will need to change the path and make sure it is absolute path
- Edit the `main.py` as you need. You can change your health, build your own deck, etc
- Go inside the game, pick your prefered character, then on the first encounter, choose `Save & Quit`
- From the main menu (no need to close the game), just run `main.py`, `python3 main.py`
- After that, click `Continue`, and enjoy!

## Disclaimer

I got the logic from [Kirill89's gist](https://gist.github.com/Kirill89/514edad0ac80af7dfc036871ccf0f877) by sawing his code written with JS. I only re-write it in python and added some feature so that the save data can be programmatically edited.
