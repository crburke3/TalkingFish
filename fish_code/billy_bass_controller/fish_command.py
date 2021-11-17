import audioread
from .globals import AUDIO_SHORTENING, _parse_movement_and_duration

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
        if not self._expected_prescaler:
            if not self.local_song_url:
                return 0.25
            total_units = self.command_unit_length()
            song_time_s = self.song_length_seconds()
            return float(song_time_s - self.audio_start_offset / total_units)
        else:
            return self._expected_prescaler

    def command_unit_length(self) -> int:
        total_cmd_duration = 0
        for cmd in self.commands:
            movement, duration = _parse_movement_and_duration(cmd)
            total_cmd_duration += duration
        return total_cmd_duration

    def song_length_seconds(self) -> float:
        if not self.local_song_url:
            print("NO SONG AVAILABLE")
            return 0.0
        with audioread.audio_open(self.local_song_url) as f:
            totalsec = f.duration
            min, sec = divmod(totalsec, 60)
            return sec

