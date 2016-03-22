from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def moby():
	particpants = (
		'malte',
		'hien',
		'marc',
		'tino',
		'sascha',
		'janis',
		'willi',
		'fabian',
		'michael',
	)

	return random.choice(particpants)

if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')