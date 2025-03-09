from backend import main
from _local_resources_.TestClass import TestClass
import requests


def test_bubbles_object_get_success_200():
    post_data = {"Body": "Hello there"}
    fake_post = TestClass(post_data)
    fake_post.path = "post_to_queue"
    fake_post.method = "POST"
    resp = main.hello_world(fake_post)
    assert resp[1] == 201


def test_bubbles_object_get_success_200():
    post_data = {"Body": "local:peter"}
    fake_post = TestClass(post_data)
    fake_post.path = "post_to_queue"
    fake_post.method = "POST"
    resp = main.hello_world(fake_post)
    assert resp[1] == 201

def test_christian_get_success_200():
    url = "https://hello-world-303741259113.us-central1.run.app/post_to_queue"
    # The data to be sent in the request
    data = {
        "Body": "christian set language sv"
    }
    # Send POST request
    response = requests.post(url, data=data)
    # Check the response status and print it
    if response.status_code == 200:
        print("Request successful!")
        print(response.text)  # Print the response body (if needed)
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)