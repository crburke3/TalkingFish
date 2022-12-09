import audioread
from .globals import AUDIO_SHORTENING, _parse_movement_and_duration
from .audio_driver import AudioDriver


class FishCommand:

    commands: [str]
    speech_text: str = None
    song_url: str = None
    local_song_url: str = None
    audio_start_offset = 0.0
    _expected_prescaler = None

    def validate(self):
        assert len(self.commands) > 0
        self.get_expected_prescaler()

    def get_expected_prescaler(self) -> float:
        audio_diver = AudioDriver()
        if not self._expected_prescaler:
            if not self.local_song_url:
                print("Using default prescalar: 0.25")
                self._expected_prescaler = 0.25
                return 0.25
            print("Calculating prescalar...")
            total_units = self.command_unit_length()
            song_time_s = audio_diver.get_audio_length_seconds(self.local_song_url)
            if total_units == 0:
                total_units = 1
            expected_prescalar = float(song_time_s / total_units) - self.audio_start_offset
            self._expected_prescaler = expected_prescalar
            return expected_prescalar
        else:
            print("Prescalar already cached")
            return self._expected_prescaler

    def command_unit_length(self) -> int:
        total_cmd_duration = 0
        for cmd in self.commands:
            try:
                movement, duration, use_ms = _parse_movement_and_duration(cmd)
                if isinstance(duration, float) or use_ms:
                    continue
                total_cmd_duration += duration
            except Exception as e:
                pass
        if total_cmd_duration == 0:
            return 1
        return total_cmd_duration
