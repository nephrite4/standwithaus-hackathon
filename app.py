from flask import Flask,render_template,request,url_for,Response
from model import check_similarity

app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def index():
	print('here')
	if request.method == 'POST':
		description = request.form.get('details-input')
		result = check_similarity(description)
		if result != None:
			return render_template(index)
			Response('', headers={'similarity': result[0], 'match': result[1]})
		else:
			return Response('', headers={'similarity': 0, 'match': None})
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

		