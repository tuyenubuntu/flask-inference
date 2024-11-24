import cv2
import threading

class Stream(threading.Thread):
    def __init__(self, args):
        super().__init__()
        self.args = args
        self.camera = None  # Camera will be initialized when the stream starts
        self.is_streaming = False  # Stream is initially stopped
        self.lock = threading.Lock()  # Thread-safe operations for starting/stopping

    def run_stream(self):
        """Start the stream."""
        with self.lock:
            if not self.is_streaming:
                self.camera = cv2.VideoCapture(self.args.input_webcam)  # Adjust input source if necessary
                self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # Set width
                self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Set height
                self.camera.set(cv2.CAP_PROP_FPS, 60)  # Set FPS
                self.is_streaming = True

    def stop_stream(self):
        """Stop the stream."""
        with self.lock:
            self.is_streaming = False
            if self.camera:
                self.camera.release()
                self.camera = None

    def generate(self):
        """Yield frames for MJPEG streaming."""
        while self.is_streaming:
            ret, frame = self.camera.read()
            if not ret:
                break  # If frame is not read, stop the loop
            ret, jpeg = cv2.imencode('.jpg', frame)
            if ret:
                frame = jpeg.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        # Ensure the camera is released if streaming stops
        self.stop_stream()
