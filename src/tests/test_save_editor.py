from spireslayer.save_editor import SaveEditor


def test_initialization():
    save_editor = SaveEditor(save_file_path="tests")
    original_save_file = save_editor.get_json()
    assert len(original_save_file) == 112
    assert save_editor.key == "key"


def test_set_json():
    save_editor = SaveEditor(save_file_path="tests")
    original_save_file = save_editor.get_json()
    new_save_file = {}
    save_editor.set_json(new_save_file)

    assert save_editor.get_json() != original_save_file
    assert save_editor.get_json() == new_save_file
