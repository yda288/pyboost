import docker

class DockerManager(object):
    def __init__(self):
        _client = docker.from_env()

    def build_image(self):
        pass