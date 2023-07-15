# JingleDingle

Tool um Jingles zu einem bestimmten Zeitpunkt abzuspielen.


Warntime ist die Zeit, bevor Ende ist.


Benötigt werden `python3` und `venv`.
Jinge am besten in `mp3` im gleichen Ordner wie das Skript platzieren.

Zeiten zu denen abgespielt werden soll wie in der Datei `test_time_file` formatiert speichern.

Für Spotify Kontrolle muss außerdem mit dem Spotify Account eine App angelegt werden auf `https://developer.spotify.com/dashboard`.
Von dort kann die `CLIENT_ID` und `CLIENT_SECRET` kopiert werden.
```
python -m venv .
./bin/venv/active

export SPOTIPY_CLIENT_ID <client_id>
export SPOTIPY_CLIENT_SECRET <secret>
export SPOTIPY_REDIRECT_URI https://localhost

python3 main.py --time-file test_time_file --start-jingle start.mp3 --warn-jingle warn.mp3 --end-jingle end.mp3 [--warn-time 5 --game-duration 30]
```

