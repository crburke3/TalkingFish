import audioread
from .globals import AUDIO_SHORTENING


class FishCommand:

    commands: [str]
    song_url: str
    speech_text: str
    local_song_url: str
    audio_start_offset = 0.0
    _expected_prescaler = None

    def validate(self):
        assert self.local_song_url is not None
        assert len(self.commands) > 0
        # self.get_expected_prescaler()

    def get_expected_prescaler(self) -> float:
        if not self._expected_prescaler:
            total_units = self.command_unit_length()
            song_time_s = self.song_length_seconds()
            return float(song_time_s - self.audio_start_offset / total_units)
        else:
            return self._expected_prescaler

    def command_unit_length(self) -> int:
        total_cmd_length = 0
        for cmd in self.commands:
            length = int(cmd[1:])
            total_cmd_length += length
        return total_cmd_length

    def song_length_seconds(self) -> float:
        with audioread.audio_open(self.local_song_url) as f:
            totalsec = f.duration
            min, sec = divmod(totalsec, 60)
            return sec

