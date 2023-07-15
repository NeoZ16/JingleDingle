# This is a sample Python script.
import argparse
import os
import pathlib
import time
from datetime import datetime, timedelta

from apscheduler.schedulers.blocking import BlockingScheduler

from MediaControl import MediaControl
from SoundControl import SoundControl


def setup(args):
    start_jingle_path = args.start_jingle
    warning_jingle_path = args.warn_jingle
    end_jingle_path = args.end_jingle

    time_file_path = args.time_file

    game_end_warn_time = args.warn_time
    game_duration = args.game_duration

    media_control = MediaControl()
    sound_control = SoundControl(start_jingle_path=start_jingle_path,
                                 warning_jingle_path=warning_jingle_path,
                                 end_jingle_path=end_jingle_path,
                                 media_control=media_control)

    scheduler = BlockingScheduler()
    jingle_times = []
    with open(time_file_path, "r") as time_file:
        lines = time_file.read().split(os.linesep)
        for line in lines:
            try:
                time_obj = time.strptime(line, '%H:%M')
                datetime_obj = datetime.today().replace(hour=time_obj.tm_hour,
                                                        minute=time_obj.tm_min,
                                                        second=0,
                                                        microsecond=0)
                if datetime_obj < datetime.now():
                    continue

                scheduler.add_job(func=sound_control.play_jingle,
                                  trigger='date',
                                  run_date=datetime_obj,
                                  args=[SoundControl.START_JINGLE])

                warning_time = datetime_obj + timedelta(minutes=game_duration - game_end_warn_time)
                scheduler.add_job(func=sound_control.play_jingle,
                                  trigger='date',
                                  run_date=warning_time,
                                  args=[SoundControl.WARNING_JINGLE])
                end_time = datetime_obj + timedelta(minutes=game_duration)
                scheduler.add_job(func=sound_control.play_jingle,
                                  trigger='date',
                                  run_date=end_time,
                                  args=[SoundControl.END_JINGLE])

                jingle_times.append(datetime_obj)

            except ValueError:
                print(f'Value Error: could not append {line} to times')

    print(f'[*] Added games {len(jingle_times)} and {len(scheduler.get_jobs())} jobs to the scheduler')
    print(f'[*] Timers set for:')
    for jingle_time in jingle_times:
        print(f'{jingle_time.strftime("%H:%M")}')

    return scheduler


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='JingleDingle',
        description='Jingle',
        epilog='Dingle')

    parser.add_argument('-t', '--time-file', required=True, type=pathlib.Path)
    parser.add_argument('--start-jingle', required=True, type=pathlib.Path)
    parser.add_argument('--warn-jingle', required=True, type=pathlib.Path)
    parser.add_argument('--end-jingle', required=True, type=pathlib.Path)

    parser.add_argument('--warn-time', default=5, type=int)
    parser.add_argument('--game-duration', default=30, type=int)

    print(parser.parse_args())

    scheduler = setup(parser.parse_args())
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
