#! /usr/bin/python
import io
import os
import json

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


class GoogleApi:
    """
    Google api
    """

    def run(self):
        """
        Run google api
        :return:
        """
        # Instantiates a client
        client = vision.ImageAnnotatorClient()

        # The name of the image file to annotate
        file_name = os.path.join(
            os.path.dirname(__file__),
            'resources/wakeupcat.jpg')

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        print('Texts:')

        text_in_image = []

        for text in texts:
            print('\n"{}"'.format(text.description.encode('utf-8')))

            text_in_image.append(('\n"{}"'.format(text.description.encode('utf-8'))))


            # vertices = (['({},{})'.format(vertex.x, vertex.y)
            #              for vertex in text.bounding_poly.vertices])

            # print('bounds: {}'.format(','.join(vertices)))
            # text_in_image.append(('bounds: {}'.format(','.join(vertices))))

            return json.dumps(text_in_image)

if __name__ == '__main__':
    GoogleApi().run()