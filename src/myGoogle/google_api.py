import json

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


class GoogleApi:
    """
    Google api
    """

    def run(self, img_data, app):
        """
        Run google api
        :return:
        """
        uri = "https://storage.googleapis.com/images_11_12_17/%s" % img_data
        app.logger.debug(uri)

        # Instantiates a client
        client = vision.ImageAnnotatorClient()

        image = types.Image()
        image.source.image_uri = uri

        response = client.text_detection(image=image)
        texts = response.text_annotations
        print('Texts:')

        text_in_image = []

        for text in texts:

            text_in_image.append(('\n"{}"'.format(text.description.encode('utf-8'))))


            # vertices = (['({},{})'.format(vertex.x, vertex.y)
            #              for vertex in text.bounding_poly.vertices])

            # print('bounds: {}'.format(','.join(vertices)))
            # text_in_image.append(('bounds: {}'.format(','.join(vertices))))

            return json.dumps(text_in_image)

if __name__ == '__main__':
    GoogleApi().run()
