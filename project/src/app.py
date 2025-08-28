from flask import Flask, request, jsonify, render_template_string
import joblib
import matplotlib.pyplot as plt
import io, base64

model = joblib.load('model/model.pkl')
app = Flask(__name__)

def predict(features):
    pred = model.predict([features])[0]
    return pred

@app.route('/predict', methods=['POST'])
def predict_default():
    data = request.get_json()
    features = data.get('features')
    return jsonify({'prediction': float(predict(features))})

@app.route('/predict/<float:input1>')
@app.route('/predict/<float:input1>/<float:input2>')
def predict_path(input1, input2=None):
    if input2 is None:
        features = [input1]
    else:
        features = [input1, input2]
    return jsonify({'prediction': float(predict(features))})

@app.route('/plot')
def plot_page():
    fig, ax = plt.subplots()
    ax.plot([0,1,2,3],[10,20,15,30])
    ax.set_title("Demo Plot")
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    html = f"<html><body><h1>Model Output Plot</h1><img src='data:image/png;base64,{img_base64}'></body></html>"
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=False)