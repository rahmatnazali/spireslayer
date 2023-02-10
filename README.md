[Slay the Spire](https://store.steampowered.com/app/646570/Slay_the_Spire/) _faster_ by editing the save file! If done right, this will keep the fun while avoiding 
too much time to be wasted.

![](assets/result-2.jpg)
![](assets/result-1.jpg)

## How the script works
- It starts by finding the obfuscated autosave file that named with this format: `<Name of the character>.autosave`. For example, see [DEFECT.autosave](example/DEFECT.autosave).
- The `SaveEditor` object will decrypt the save data and convert it to an editable JSON object format [like this](example/readable_save_file.json).
- You can edit the json object as needed.
- Call the `SaveEditor.write_json_to_file()` and the script will write the modified save file back to the obfuscated save file format and replace the old one

## How to use the package

Install the package with `pip install spireslayer`.

### 1. Creating your own save file editor

Create your own script as needed, for example:

```python
from spireslayer.save_editor import SaveEditor
from spireslayer.decks import Deck
from spireslayer.card import Card
from spireslayer.templates.defect_card import GLACIER, DEFRAGMENT, BLIZZARD

# Declare a valid path to the save folder
save_file_path = "C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\saves"

# Declare a save editor that points to the save_file path
save_editor = SaveEditor(save_file_path)

# Edit whatever you want.
# here we are making our custom powerful deck for our Defect
save_editor.set_deck(Deck([
    Card(GLACIER),
    Card(GLACIER),
    Card(GLACIER),
    Card(DEFRAGMENT),
    Card(DEFRAGMENT),
    Card(DEFRAGMENT),
    Card(BLIZZARD),
    Card(BLIZZARD),
    Card(BLIZZARD),
    Card(BLIZZARD),
    Card(BLIZZARD),
]))

# or maybe increase our Defect's max orb
save_editor.update_max_orbs(15)

# or anything that can be adjustable to your need
save_editor.update_current_health(400)
save_editor.update_max_health(500)
save_editor.update_hand_size(10)
save_editor.update_energy_per_turn(20)

# After customization is finished, call this method to rewrite the save data back to the original place. The old save file will be replaced.
save_editor.write_json_to_file()
```

### 2. Running the save file editor

- Open the game. You can create a new game or continue your session. 
- On the first encounter after loading the game, hit the menu and choose `Save & Quit`.
- From the main menu, switch back to your script and run it. You don't need to close the game.
- Back to your game and click `Continue`. Enjoy the game!

## Note

Currently, the package only supports The Defect.
For other character, you can create the method yourself (PR is greatly appreciated!) or alternatively use the provided API `SaveEditor.get_json()` to get the JSON formatted save file,  change the JSON directly, and assign it back with the provided API `SaveEditor.set_json()`. For example:

```python
from spireslayer.save_editor import SaveEditor

editor = SaveEditor(...)

save_file = editor.get_json()
save_file['current_health'] = 1000
editor.set_json(save_file)
```

Refer to the [readable save file example](example/readable_save_file.json) for more example.

## Disclaimer

I got the save file encryption logic from [Kirill89's gist](https://gist.github.com/Kirill89/514edad0ac80af7dfc036871ccf0f877) written in JS. What I did was only re-write it in python and added some feature so that the save data can be programmatically edited.
