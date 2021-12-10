from billy_bass_controller.device import Device


def test_get_mac():
    mac = Device.get_device_id()
    assert mac is not None