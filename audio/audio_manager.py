import random
import threading
import time
from typing import Callable

import pygame

from handle_data.data_management import get_audio_info_from_json, write_audio_info_to_json


_audio_source_path = "audio/source/"


def audio_manager() -> (Callable[[], None],
                        Callable[[], float],
                        Callable[[], float],
                        Callable[[float], None],
                        Callable[[float], None],
                        Callable[[], None]):
    music_name = "background_music_{}.mp3"

    musics_count = 5
    last_music_index = -1

    music_switcher = None

    is_music_switcher_running_lock = threading.Lock()
    is_music_switcher_running = True
    need_play_next_music_lock = threading.Lock()
    need_play_next_music = True

    audio_info = get_audio_info_from_json()

    pygame.mixer.init()
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()
    pygame.display.init()

    music_ended = pygame.USEREVENT + 1
    # noinspection PyArgumentList
    pygame.mixer.music.set_endevent(music_ended)

    def get_random_music_file_name() -> str:
        nonlocal last_music_index

        current_music_index = last_music_index
        while current_music_index == last_music_index:
            current_music_index = random.randint(0, musics_count - 1)

        last_music_index = current_music_index

        file_name = _audio_source_path + music_name.format(str(current_music_index))
        return file_name

    def play_random_music() -> None:
        file_name = get_random_music_file_name()

        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play()

    def music_switch() -> None:
        nonlocal is_music_switcher_running

        is_music_switcher_running_lock.acquire()
        while is_music_switcher_running:
            is_music_switcher_running_lock.release()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_music_switcher_running_lock.acquire()
                    is_music_switcher_running = False
                    is_music_switcher_running_lock.release()

                    pygame.quit()

                need_play_next_music_lock.acquire()

                if event.type == music_ended and need_play_next_music:
                    play_random_music()

                need_play_next_music_lock.release()

            time.sleep(0.5)

            is_music_switcher_running_lock.acquire()

        is_music_switcher_running_lock.release()

    def play_finish_notification() -> None:
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(_audio_source_path + "finish_notification.wav"))

    def play_error_notification() -> None:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(_audio_source_path + "error_notification.wav"))

    def get_sound_effect_volume() -> float:
        return audio_info["sound_effect_volume"]

    def get_music_volume() -> float:
        return audio_info["music_volume"]

    def set_sound_effect_volume(volume: float) -> None:
        if volume < 0.0:
            volume = 0.0
        if volume > 1.0:
            volume = 1.0

        pygame.mixer.Channel(1).set_volume(volume)
        pygame.mixer.Channel(2).set_volume(volume)

        audio_info["sound_effect_volume"] = volume
        write_audio_info_to_json(audio_info)

    def set_music_volume(volume: float) -> None:
        if volume < 0.0:
            volume = 0.0
        if volume > 1.0:
            volume = 1.0

        pygame.mixer.music.set_volume(volume)

        audio_info["music_volume"] = volume
        write_audio_info_to_json(audio_info)

    def close_listener() -> None:
        nonlocal need_play_next_music, is_music_switcher_running

        need_play_next_music_lock.acquire()
        need_play_next_music = False
        need_play_next_music_lock.release()

        is_music_switcher_running_lock.acquire()
        is_music_switcher_running = False
        is_music_switcher_running_lock.release()

        music_switcher.join()

    music_switcher = threading.Thread(target=music_switch)
    music_switcher.start()

    play_random_music()

    pygame.mixer.music.set_volume(get_music_volume())
    pygame.mixer.Channel(1).set_volume(get_sound_effect_volume())
    pygame.mixer.Channel(2).set_volume(get_sound_effect_volume())

    return play_finish_notification, play_error_notification, get_sound_effect_volume, get_music_volume,\
        set_sound_effect_volume, set_music_volume, close_listener
