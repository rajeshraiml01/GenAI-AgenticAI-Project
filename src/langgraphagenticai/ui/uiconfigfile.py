from configparser import ConfigParser
from pathlib import Path

class UIConfigFile:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(Path(__file__).parent / 'uiconfigfile.ini')

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")    