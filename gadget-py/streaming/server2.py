#!/usr/bin/env python
from flask import Flask, render_template, Response
import cv2
import sys
import numpy

app = Flask(__name__)


def get_frame():
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)  # this makes a web cam object

    while True:
        retval, im = camera.read()
        imgencode = cv2.imencode('.jpg', im)[1]
        stringData = imgencode.tostring()
        yield (b'--frame\r\n'
               b'Content-Type: text/plain\r\n\r\n' + stringData + b'\r\n')

    del (camera)


@app.route('/video')
def vid():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True, threaded=True)
