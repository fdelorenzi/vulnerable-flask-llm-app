from flask import Flask, request, render_template
from dotenv import load_dotenv
from models import Summary, session
from utils import extract_text_from_pdf, evaluate_cv

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        text = extract_text_from_pdf(file)
        result = evaluate_cv(text)
        new_summary = Summary(summary=result['summary'], evaluation=result['evaluation'])
        session.add(new_summary)
        session.commit()
        return render_template('upload.html', new_summary=new_summary)
    return render_template('upload.html')

@app.route('/summaries')
def summaries():
    id = request.args.get('id')
    if id:
        summaries = session.query(Summary).filter_by(id=id).all()
        return render_template('summaries.html', summaries=summaries)
    else:
        return "Error: No ID provided", 400

if __name__ == '__main__':
    app.run(debug=True)
