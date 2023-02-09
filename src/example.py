from decks import defect_frost_deck
from editor import SaveEditor


if __name__ == '__main__':
    save_editor = SaveEditor(save_file_path=
                             "C:\\Program Files (x86)\\Steam\\steamapps\\common\\SlayTheSpire\\saves")

    # In here, you can do whatever you want on your save file
    save_editor.update_current_health()
    save_editor.update_max_health()
    save_editor.update_hand_size()
    save_editor.update_energy_per_turn()

    # For example, for The Defect, we can maximize the orbs and customize the whole deck
    save_editor.update_max_orbs()
    save_editor.set_deck(defect_frost_deck)

    # After customization is finished, call this method to rewrite the save data back to where it belong
    save_editor.write_json_to_file()
