''' Executing this function initiates the application of emotion detection
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function.
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    dominant_emotion = response.get('dominant_emotion')
    response.pop('dominant_emotion')
    response_strings = []
    for emotion, score in response.items():
        if emotion != 'sadness':
            response_strings.append(f"'{emotion}': {score}")
    response_string = ', '.join(response_strings)
    response_string += f" and 'sadness': {response['sadness']}"
    return f"For the given statement, the system response is {response_string}. The dominant emotion is {dominant_emotion}"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
