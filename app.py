from flask import Flask,render_template,request,url_for,Response,jsonify, redirect
from model import check_similarity

app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def index():
	print('here')
	if request.method == 'POST':
		description = request.form.get('details')
		result = check_similarity(description)
		if result[0] > 0.99:
			return jsonify(similarity= str(result[0]), match= result[1])
		else:
			return jsonify(similarity= str(0), match= None)
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

		