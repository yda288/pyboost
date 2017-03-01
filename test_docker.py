import DockerManager
import unittest
from unittest.mock import  Mock, patch
from nose.tools import *

class DockerManagerTests(unittest.TestCase):

    @patch('DockerManager.DockerManager.build_image')
    def test_docker_build(self, mock_build):
        docker_manager = DockerManager.DockerManager()
        mock_build.return_value ='hello'

        build_response = docker_manager.build_image()

        assert_equals(build_response, mock_build.return_value)




