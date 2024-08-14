[Slay the Spire](https://store.steampowered.com/app/646570/Slay_the_Spire/) _faster_ by editing the save file! If done right, this will keep the fun while avoiding 
too much time to be wasted.

![](assets/result-2.jpg)
![](assets/result-1.jpg)

## How the script works
- It starts by finding the obfuscated autosave file that named with this format: `<Name of the character>.autosave`. For example, see [DEFECT.autosave](example/DEFECT.autosave).
- The `SaveEditor` object will decrypt the save data and convert it to an editable [JSON object format](example/readable_save_file.json).
- At this point, you can edit the json object as needed.
- Finally, call the `SaveEditor.write_json_to_file()` and the script will write the modified save file back to the obfuscated save file format, replacing the old one

## How to use the package

Install the package with `pip install spireslayer`.

### 1. Creating your own save file editor

Create your own script as needed, for example:

```python
from spireslayer.save_editor import SaveEditor
from spireslayer.decks import Deck
from spireslayer.card import Card
from spireslayer.templates.defect_card import GLACIER, DEFRAGMENT, BLIZZARD

# Declare a save editor that points to the path of your root game installation
save_editor = SaveEditor(
    installation_path="C:\\Program Files (x86)\\Steam\\steamapps\\common\\SlayTheSpire",
)

# Edit whatever you want.
# here we are making custom powerful deck for our Defect
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

# or anything that can be adjusted to your need
save_editor.update_current_health(400)
save_editor.update_max_health(500)
save_editor.update_hand_size(10)
save_editor.update_energy_per_turn(20)

# for attributes that are not yet provided within the package, you can use the generic update_attribute method
# you can find the key for each attribute in the example JSON save file provided in  this project
save_editor.update_attribute('current_health', 90)
save_editor.update_attribute('hand_size', 10)

# After customization is finished, call this method to rewrite the save data back to the original place.
# WARNING: The old save file will be replaced.
save_editor.write_json_to_file()
```

### 2. Running the save file editor

- Open the game. Create a new game or continue any session. 
- On the first encounter after loading the game, hit the menu and choose `Save & Quit`.
- From the main menu, switch back to the script and run it. Closing the game is unnecessary.
- Switch back to the game and click `Continue`. Enjoy the game!

## Notes
- This package now supports Colorless Card, and nearly all 4 playable hero's cards (thanks [@gabrekt](https://github.com/gabrekt)!).
- There is a [know issue](https://github.com/rahmatnazali/spireslayer/issues/13) with the Watcher's Rushdown Card not being correctly recognized.
- For any change that are not yet supported within the package, please use the provided API `SaveEditor.get_json()` and 
change it directly.
For example:

    ```python3
    from spireslayer.save_editor import SaveEditor
    
    save_editor = SaveEditor()
    
    save_file = save_editor.get_json()
    save_file['current_health'] = 1000
    save_file['...'] = 'something-something'
    
    # don't forget to give it back to the save_editor
    save_editor.set_json(save_file)
    
    save_editor.write_json_to_file()
    ```

    Refer to the [readable save file example](example/readable_save_file.json) for more available keys.

- PR is always appreciated!

## Disclaimer

I got the save file encryption logic from [Kirill89's gist](https://gist.github.com/Kirill89/514edad0ac80af7dfc036871ccf0f877) written in JS. What I did was only rewriting it in python and adding features so that the save data can be programmatically edited.
