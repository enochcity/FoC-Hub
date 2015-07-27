from configparser import ConfigParser
config = ConfigParser()
config.read("Config.txt")
language = config.get("lang", "language")


if language == "English":
    from .english_lang import *
elif language == "Norsk":
    from .norwegian_lang import *
else:
    from .english_lang import *    
