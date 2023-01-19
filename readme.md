# Autosave editor for [Slay the Spire](https://store.steampowered.com/app/646570/Slay_the_Spire/)

The code has been written as modular as possible for easy customization. Use with caution, as it can really ruin the fun. 

## How the script works
- It starts by finding an autosave file, usually named with this format: `<Name of the character>.autosave`, for example [DEFECT.autosave](saves/DEFECT.autosave).
- It will then try to decrypt the save data and convert it to an editable JSON format [like so](backups/2023-01-19%2007:13:11.270793.json).
- You can then edit the save file as you want via `main.py`
- The script will then write it back to the obfuscated autosave file format

## How to
- Install python3 
- Inside `main.py`, change the `save_file_path` according to your game installation so that it points to the *root path* of the autosave file. On Windows default, it will usually be `C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\saves`
- Edit the `main.py` as you need. You can change your health, build your own deck, etc. For example:

```python
from editor import SaveEditor
from decks import Deck
from card import Card

# Declare a valid path to the save folder
save_file_path = "C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\saves"

# Declare a save editor that points to the save_file path
save_editor = SaveEditor(save_file_path)

# Edit whatever you want.
# here we are making our custom powerful deck for our Defect
save_editor.set_deck(Deck([
    Card(Card.GLACIER),
    Card(Card.GLACIER),
    Card(Card.GLACIER),
    Card(Card.DEFRAGMENT),
    Card(Card.DEFRAGMENT),
    Card(Card.DEFRAGMENT),
    Card(Card.BLIZZARD),
    Card(Card.BLIZZARD),
    Card(Card.BLIZZARD),
    Card(Card.BLIZZARD),
    Card(Card.BLIZZARD),
]))

# or increase our Defect's max orb
save_editor.update_max_orbs()

# or anything that can be adjustable to your need
save_editor.update_current_health()
save_editor.update_max_health()
save_editor.update_hand_size()
save_editor.update_energy_per_turn()

# After customization is finished, don't forget call this method to rewrite the save data back to where it belongs
save_editor.write_json_to_file()
```

- Go inside the game, pick your prefered character, then on the first encounter, choose `Save & Quit`
- From the main menu (no need to close the game), just run `main.py` with the command `python3 main.py`
  - On each script run, the script will dump the original save data BEFORE any modification is happening and save it inside `backups` folder. So just in case you messed up with something, you can revert the save file 
- Back to your game and click `Continue`. Enjoy!

![](assets/result-1.jpg)
![](assets/result-2.jpg)

## Note

Currently, there are only configuration for The Defect. 
But actually if you can already see the save data in JSON you can change anything you want, 
so feel free to modify the code and add your own preference!

Again, refer to the [example of the save file](backups/2023-01-19 07:13:11.270793.json). It is really just a simple JSON edit.

## Disclaimer

I got the save file encryption logic from [Kirill89's gist](https://gist.github.com/Kirill89/514edad0ac80af7dfc036871ccf0f877) written in JS. What I did was only re-write it in python and added some feature so that the save data can be programmatically edited.
