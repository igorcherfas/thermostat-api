from flask import (
    render_template,
    jsonify
)
import connexion

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')



@app.route('/')
def home():
    """
    This function responds to /

    :return: the renedered template 'index.html'
    """

    return jsonify(message='Im still alive here, thanks for asking!',status='200')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
