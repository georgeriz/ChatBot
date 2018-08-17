from rasa_nlu.model import Interpreter
import json

def chatty(message):
	result = interpreter.parse(unicode(message))
	print(json.dumps(result, indent=2))

interpreter = Interpreter.load("./models/current/nlu")