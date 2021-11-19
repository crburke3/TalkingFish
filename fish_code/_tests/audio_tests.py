from billy_bass_controller.audio_driver import AudioDriver



def test_mp3():
    file_path = "../_resources/man-scream-01.mp3"
    driver = AudioDriver()
    driver.play_mp3_file(file_path)

def test_get_mp3_length():
    file_path = "../_resources/man-scream-01.mp3"
    driver = AudioDriver()
    print(driver.get_mp3_length(file_path))