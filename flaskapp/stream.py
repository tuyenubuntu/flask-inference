import cv2
import sys
import threading
import traceback
import argparse
# from model import Model
#from jetson_utils import videoSource, videoOutput


class Stream(threading.Thread):
    """
    Thread for streaming video and applying DNN inference
    """
    def __init__(self, args):
        """
        Create a stream from input/output video sources, along with DNN models.
        """
        super().__init__()
        
        self.args = args
        self.input = videoSource(args.input, argv=sys.argv)
        self.output = videoOutput(args.output, argv=sys.argv)
        self.frames = None
        self.net = detectNet(model=model, labels=labels, colors=colors,
        input_blob=input_layer, 
        output_cvg=output_layer['scores'], 
        output_bbox=output_layer['bbox'])
        # self.models = {}