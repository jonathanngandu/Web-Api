import os

from google.cloud import firestore, vision
from google.cloud.vision import types



class GoogleApi:
    """
    Google api
    """

    def __init__(self):
        pass

    def run(self, img_data, app):
        """
        Using the image url provided, we make a request to the google vision api and return the image text
        """
        image_uri = os.environ['IMAGE_URL']
        uri = "%s/%s" % (image_uri, img_data)
        app.logger.debug(uri)

        # Instantiates a client
        storage = firestore.Client()
        client = vision.ImageAnnotatorClient()

        bucket = storage.get_bucket('my-project-1503746529352')
        blob = bucket.blob(img_data)
        public_url = blob.public_url
        app.logger.debug(public_url)

        image = types.Image()
        image.source.image_uri = uri

        response = client.text_detection(image=image)
        texts = response.text_annotations
        print('Texts:')

        text_in_image = []

        for text in texts:

            text_in_image.append(('\n"{}"'.format(text.description.encode('utf-8'))))

        return text_in_image

if __name__ == '__main__':
    GoogleApi().run()
