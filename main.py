import cv2
from flask import Flask, render_template, Response


video = cv2.VideoCapture(0)#0 - integrated camera

def get_frame():
    while True:
        success, frame = video.read()
        #encode
        _, encoded_image = cv2.imencode('.jpg', frame)
        frame = encoded_image.tobytes()
        yield(b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed_url')
def video_feed():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    #local deployment
    app.run(debug=True)
    ##public internet deployment
    #app.run(debug=True, host = '0.0.0.0', port=5001)