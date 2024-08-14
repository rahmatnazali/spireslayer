[Slay the Spire](https://store.steampowered.com/app/646570/Slay_the_Spire/) _faster_ by editing the save file! If done right, this will keep the fun while avoiding 
too much time to be wasted.

![](assets/result-2.jpg)
![](assets/result-1.jpg)

## How the script works
- It starts by finding the obfuscated autosave file that named with this format: `<Name of the character>.autosave`. For example, see [DEFECT.autosave](example/DEFECT.autosave).
- The `SaveEditor` object will decrypt the save data and convert it to an editable [JSON object format](example/readable_save_file.json).
- At this point, you can edit the json object as needed.
- Finally, call the `SaveEditor.write_json_to_file()` and the script will write the modified save file back to the obfuscated save file format, replacing the old one.

## How to use the package

### 1. Install & Identify

Install the package with `pip install spireslayer`.

Identify your game installation path.

This package assumes the Steam default installation on Windows: `C:\\Program Files (x86)\\Steam\\steamapps\\common\\SlayTheSpire`.

If your installation happened to be using the default, then you don't need to pass any arguments when calling the `SaveEditor`. 
The package will handle it for you:

```python3
from spireslayer.save_editor import SaveEditor

save_editor = SaveEditor()
```

For any custom path (e.g. other marketplace or OS), please specify the installation path when initializing the `SaveEditor` class:

```python3
from spireslayer.save_editor import SaveEditor

# custom Windows path
save_editor = SaveEditor(
    installation_path="D:\\MyGames\\SlayTheSpire",
)

# or linux path
save_editor = SaveEditor(
    installation_path="/home/rahmat/.steam/debian-installation/steamapps/common/SlayTheSpire",
)
```

### 2. Creating your own save file editor

Create your own editor behavior by importing the `SaveEditor` to your python script:

```python
# defect_editor.py

from spireslayer.save_editor import SaveEditor
from spireslayer.decks import Deck
from spireslayer.card import Card
from spireslayer.templates.defect_card import GLACIER, DEFRAGMENT, BLIZZARD

save_editor = SaveEditor()

# let's start by creating a custom powerful deck for our Defect
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

# or basically anything you need
save_editor.update_current_health(400)
save_editor.update_max_health(500)
save_editor.update_hand_size(10)
save_editor.update_energy_per_turn(20)

# for attributes that are not yet provided within the package's method, you can use the generic update_attribute method
# you can find the key for each attribute in the example JSON save file provided in this project
save_editor.update_attribute('current_health', 90)
save_editor.update_attribute('hand_size', 10)

# After customization is finished, call this method to rewrite the save data back to the original place.
# WARNING: The old save file will be replaced.
save_editor.write_json_to_file()
```

### 3. Running the save file editor

- Open the game. Create a new game or continue any session. 
- On the first encounter after loading the game, hit the menu and choose `Save & Quit`.
- From the main menu, switch to the script and run it. Closing the game is actually unnecessary.
- Switch back to the game and click `Continue`. 
- Enjoy the game!

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
    save_file['some-key'] = 'something-something'
    
    # don't forget to give it back to the save_editor
    save_editor.set_json(save_file)
    
    save_editor.write_json_to_file()
    ```

    Refer to the [readable save file example](example/readable_save_file.json) for more available keys.

- PR is always appreciated!

## Disclaimer

I got the save file encryption logic from [Kirill89's gist](https://gist.github.com/Kirill89/514edad0ac80af7dfc036871ccf0f877) written in JS. 
What I did was only rewriting it in python and adding modularity of the save editor.
