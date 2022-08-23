from decks import defect_frost_deck
from editor import SaveEditor

if __name__ == '__main__':
    save_file_path = "/home/rahmat/.steam/debian-installation/steamapps/common/SlayTheSpire/saves"
    save_editor = SaveEditor(save_file_path)

    # to debug current file, just exit. The file will be written inside `backups` folder
    # exit()

    # example
    save_editor.update_current_health()
    save_editor.update_max_health()
    save_editor.update_hand_size()
    save_editor.update_energy_per_turn()

    # For The Defect
    save_editor.update_max_orbs()
    save_editor.set_deck(defect_frost_deck)

    save_editor.write_json_to_file()
