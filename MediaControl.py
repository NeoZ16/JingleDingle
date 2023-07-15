from spotipy import SpotifyOAuth, Spotify


class MediaControl:

    def __init__(self):
        scope = 'app-remote-control user-read-playback-state streaming'
        self.session = Spotify(auth_manager=SpotifyOAuth(scope=scope))
        print(f'[*] Connected to Spotify Account {self.session.current_user()["display_name"]}')

    def start_playback(self):
        if not self.is_playing():
            self.session.start_playback()

    def stop_playback(self):
        if self.is_playing():
            self.session.pause_playback()

    def is_playing(self):
        return self.session.currently_playing()['is_playing']
