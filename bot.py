import os, time, random, tweepy

images_path = 'images'

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')


def get_api():
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)


def post_image(api: tweepy.API, image_path: str = None):
    api.update_status_with_media(None, image_path)

    print(f'Posted tweet with image {image_path}')


def get_images_path():
    curr_dir = os.path.dirname(__file__)
    real_path = os.path.join(curr_dir, images_path)
    return real_path


def get_random_image(path: str):
    return os.path.join(path, random.choice(os.listdir(path)))


if __name__ == '__main__':
    api = get_api()
    images_absolute_path = get_images_path()

    image = get_random_image(images_absolute_path)
    post_image(api, image)
