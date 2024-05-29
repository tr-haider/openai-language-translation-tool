from flask import Flask, render_template,request
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def translate_text(source_lang,target_lang,text):
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [{"role" : "user","content":f'Translate the following text from {source_lang} to {target_lang}:\n\n{text}'}],
    )
    return response.choices[0].message.content.strip()

@app.route('/', methods=['GET','POST'])
def index():
    translation = ""
    if request.method == 'POST':
        text = request.form['text']
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']
        translation = translate_text(source_lang, target_lang,text)
    return render_template('index.html', translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
