import base64
import datetime
import json
import os

from card import Card


class SaveEditor():
    def __init__(self, root_path) -> None:
        super().__init__()
        self.root_path = root_path
        self.key = "key"
        self.save_file_path = self.find_autosave_file()
        self.encoded_save_data: str = self.load_encoded_save_data_from_file()
        self.json_save_data = self.save_to_json()

        # backup current save file data
        with open(f"backups/{datetime.datetime.now()}.json", "w") as current_save_file:
            current_save_file.write(json.dumps(self.json_save_data, indent=2, sort_keys=True))

    @property
    def json(self):
        return self.json_save_data

    def find_autosave_file(self):
        assert self.root_path is not None, "Root path is None"
        possible_save_files = os.listdir((self.root_path))
        for filename in possible_save_files:
            if filename.endswith('.autosave'):
                return os.path.join(self.root_path, filename)
        raise ValueError("No .autosave file found")

    def load_encoded_save_data_from_file(self):
        with open(self.save_file_path, 'r') as save_file:
            content = save_file.readline()
            assert content is not None, "Encoded save data is None"
            return content

    def write_json_to_file(self):
        with open(self.save_file_path, 'wb') as save_file:
            new_save_data = self.json_to_save()
            save_file.write(new_save_data)

    def base64_encode(self, string):
        return base64.b64encode(string)

    def base64_decode(self, string) -> bytes:
        return base64.b64decode(string)

    def save_to_json(self):
        data: bytes = self.base64_decode(self.encoded_save_data)
        json_char_list: list = list()

        for i, value in enumerate(data):
            modulus_index: int = i % len(self.key)
            xor_result: int = data[i] ^ ord(self.key[modulus_index])
            char_result: str = chr(xor_result)
            json_char_list.append(char_result)

        plain_json = ''.join(json_char_list)
        return json.loads(plain_json)

    def json_to_save(self):
        assert self.json_save_data is not None, "JSON save data is None"
        plain_json = json.dumps(self.json_save_data)
        assert isinstance(plain_json, str)

        encoded_char_list: list = list()
        for i, value in enumerate(plain_json):
            modulus_index: int = i % len(self.key)
            xor_result: int = ord(value) ^ ord(self.key[modulus_index])
            encoded_char_list.append(xor_result)

        final_data = self.base64_encode(bytes(encoded_char_list))

        return final_data

    def update_current_health(self, health: int = 500):
        self.json_save_data['current_health'] = health
        assert self.json.get('current_health') == health

    def update_max_health(self, health: int = 500):
        self.json_save_data['max_health'] = health
        assert self.json.get('max_health') == health

    def update_max_orbs(self, max_orbs: int = 10):
        self.json_save_data['max_orbs'] = max_orbs
        assert self.json.get('max_orbs') == max_orbs

    def set_deck(self, deck):
        self.json_save_data["cards"] = deck.to_json()

    def add_card(self, card: Card):
        self.json_save_data["cards"].append(card.to_json())
