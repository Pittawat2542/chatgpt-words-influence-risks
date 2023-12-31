import uuid


class Story:
    def __init__(self, title: str, story: str, words: list[str], is_positive_words: bool, model: str = None,
                 temperature: float = None):
        self.title = title
        self.story = story
        self.id = str(uuid.uuid4())
        self.model = model
        self.words = words
        self.is_positive_words = is_positive_words
        self.temperature = temperature

    def from_json(self, json_obj: dict):
        self.title = json_obj["title"]
        self.story = json_obj["story"]
        self.id = json_obj["id"]
        self.words = json_obj["words"]
        self.is_positive_words = json_obj["is_positive_words"]
        self.model = json_obj["model"]
        self.temperature = json_obj["temperature"]

    def to_json(self) -> dict:
        return {
            "title": self.title,
            "story": self.story,
            "id": self.id,
            "words": self.words,
            "is_positive_words": self.is_positive_words,
            "model": self.model,
            "temperature": self.temperature
        }

    def __str__(self):
        return f"Title: {self.title}\nStory: {self.story}\nId: {self.id}\nModel: {self.model}\nWords: {self.words}\nIs Positive Words: {self.is_positive_words}\nTemperature: {self.temperature}\n"


class Ending:
    def __init__(self, ending: str, story_id: str, model: str = None, temperature: float = None):
        self.ending = ending
        self.id = str(uuid.uuid4())
        self.story_id = story_id
        self.model = model
        self.temperature = temperature

    def from_json(self, json_obj: dict):
        self.ending = json_obj["ending"]
        self.id = json_obj["id"]
        self.story_id = json_obj["story_id"]
        self.model = json_obj["model"]
        self.temperature = json_obj["temperature"]

    def to_json(self) -> dict:
        return {
            "ending": self.ending,
            "id": self.id,
            "story_id": self.story_id,
            "model": self.model,
            "temperature": self.temperature
        }

    def __str__(self):
        return f"Ending: {self.ending}\nId: {self.id}\nModel: {self.model}\nTemperature: {self.temperature}\n"
