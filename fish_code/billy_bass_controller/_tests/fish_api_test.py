from billy_bass_controller import FishAPI


api = FishAPI()


def test_information_post():
    api.post_fish_formation()


def test_get_next_queue_item():
    data = api.get_next_item_in_queue()
    print(data)


def test_post_command():
    text = "memae test test test"
    resp = api.post_fish_command(text)
    print(resp)
    assert resp == 201



