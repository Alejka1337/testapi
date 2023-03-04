import string
import random
import hashlib


def create_shortlink(url):
    characters = string.ascii_letters + string.digits
    shortlink = ''.join(random.choice(characters) for i in range(3))
    url_hash = hashlib.sha256(url.encode('utf-8')).hexdigest()[:3]
    return shortlink + url_hash
