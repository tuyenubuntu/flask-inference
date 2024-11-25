from flask import Flask, render_template, Response, url_for, send_file
from flask_socketio import SocketIO, emit
import stream_webcam 
import stream
import argparse
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("--host", default='0.0.0.0', type=str, help="interface for the webserver to use (default is all interfaces, 0.0.0.0)")
parser.add_argument("--port", default=5000, type=int, help="port used for webserver (default is 8050)")
parser.add_argument("--input", default='webrtc://@:8554/input', type=str, help="input camera stream or video file")
parser.add_argument("--input-webcam", type=int, default=0 , help="Input video source (default is webcam).")
parser.add_argument("--input-usb", type=str, default='/dev/video0' , help="Input video source (default is webcam).")
parser.add_argument("--debug", action='store_true')
parser.add_argument("--detection", default='', type=str, help="load object detection model (see detectNet arguments)")
parser.add_argument("--labels", default='', type=str, help="path to labels.txt for loading a custom model")
parser.add_argument("--colors", default='', type=str, help="path to colors.txt for loading a custom model")
parser.add_argument("--input-layer", default='', type=str, help="name of input layer for loading a custom model")
parser.add_argument("--output-layer", default='', type=str, help="name of output layer(s) for loading a custom model (comma-separated if multiple)")
#boolean
parser.add_argument("--stream-webcam", action='store_true')
parser.add_argument("--stream", action='store_true')
parser.add_argument("--stream-usb", action='store_true')
parser.add_argument("--jetson", action='store_true')
parser.add_argument("--opencv", action='store_true')

args = parser.parse_known_args()[0]

streams = stream_webcam.Stream(args)
if args.stream:
    streams = stream.Stream(args)

streams.start()
app = Flask(__name__)
socketio = SocketIO(app)

# Khởi tạo luồng stream
# stream = Streams()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stream')
def stream_video():
    return render_template('stream.html')


@app.route('/video')
def video():
    """Return the MJPEG stream or a placeholder."""
    if streams.is_streaming:
        return Response(streams.generate(),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    # Return a placeholder image if the stream is not running
    return send_file('static/images/nocap.png', mimetype='image/png')  # Update with your placeholder path

    
    
@app.route('/info')
def info():
    return render_template('info.html')    


@app.route('/start_stream')
def start_stream():
    """Start the video stream."""
    streams.run_stream()
    return "Stream started."

@app.route('/stop_stream')
def stop_stream():
    """Stop the video stream."""
    streams.stop_stream()
    return "Stream stopped."


@socketio.on('navigate')
def handle_navigation(data):
    target = data.get('target')
    if target == 'home':
        emit('redirect', {'target': url_for('index')})
    elif target == 'info':
        emit('redirect', {'target': url_for('info')})
    elif target == 'stream_video':
        emit('redirect', {'target': url_for('stream_video')})


if __name__ == '__main__':
    socketio.run(app, host=args.host, port=args.port, debug=args.debug)