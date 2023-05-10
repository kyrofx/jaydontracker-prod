from flask import Flask, jsonify
import subprocess

app = Flask(__name__)


@app.route('/check_jaydon')
def check_jaydon():
    process = subprocess.Popen(['scrapy', 'runspider', 'jaydonscraper.py'], stdout=subprocess.PIPE)
    output, error = process.communicate()
    output = output.decode('utf-8')

    if "True" in output:
        result = {'jaydon': True}
    else:
        result = {'jaydon': False}

    return result


if __name__ == '__main__':
    app.run()
