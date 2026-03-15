import pygame
import os

# Not even going to use this until I understand it LOL
class AudioManager:
    def __init__(self, music_folder="music", sfx_folder="sfx", volume=0.5):
        pygame.mixer.init()
        self.music_folder = music_folder
        self.sfx_folder = sfx_folder
        self.current_music = None
        self.music_volume = volume
        pygame.mixer.music.set_volume(volume)
        self.sfx_cache = {}  # cache loaded sound effects

    # --------------------------
    # Background music
    # --------------------------
    def play_music(self, filename, loop=True, fade_ms=0):
        path = os.path.join(self.music_folder, filename)
        if not os.path.exists(path):
            print(f"[AudioManager] Music file not found: {path}")
            return

        # Stop current music if any
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

        pygame.mixer.music.load(path)
        loops = -1 if loop else 0
        pygame.mixer.music.play(loops=loops, fade_ms=fade_ms)
        self.current_music = filename

    def stop_music(self, fade_ms=0):
        if fade_ms > 0:
            pygame.mixer.music.fadeout(fade_ms)
        else:
            pygame.mixer.music.stop()
        self.current_music = None

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def set_music_volume(self, volume):
        pygame.mixer.music.set_volume(volume)
        self.music_volume = volume

    # --------------------------
    # Sound effects
    # --------------------------
    def play_sfx(self, filename, volume=1.0):
        if filename not in self.sfx_cache:
            path = os.path.join(self.sfx_folder, filename)
            if not os.path.exists(path):
                print(f"[AudioManager] SFX file not found: {path}")
                return
            self.sfx_cache[filename] = pygame.mixer.Sound(path)

        sound = self.sfx_cache[filename]
        sound.set_volume(volume)
        sound.play()
