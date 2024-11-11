import os
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

class MusicPlayer:
    def __init__(self):
        self.current_song = None
        self.playlist = []
        self.is_paused = False

    def add_song(self, song_path):
        """Add song or directory of songs to the playlist."""
        if os.path.isdir(song_path):
            # Add all MP3 files from the directory
            for file in os.listdir(song_path):
                if file.endswith(".mp3"):
                    full_path = os.path.join(song_path, file)
                    self.playlist.append(full_path)
                    print(f"Added: {os.path.basename(full_path)}")
        elif os.path.exists(song_path) and song_path.endswith(".mp3"):
            self.playlist.append(song_path)
            print(f"Added: {os.path.basename(song_path)}")
        else:
            print("Invalid file or directory. Please provide a valid MP3 file or directory.")

    def remove_song(self, index):
        """Remove song by index from playlist."""
        if 0 <= index < len(self.playlist):
            removed_song = self.playlist.pop(index)
            print(f"Removed: {os.path.basename(removed_song)}")
        else:
            print("Invalid index.")

    def show_playlist(self):
        """Display the playlist."""
        if self.playlist:
            print("\nPlaylist:")
            for idx, song in enumerate(self.playlist):
                print(f"{idx + 1}. {os.path.basename(song)}")
        else:
            print("\nNo songs in the playlist.")

    def play_song(self, index):
        """Play a song by index from the playlist."""
        if 0 <= index < len(self.playlist):
            song_path = self.playlist[index]
            if song_path != self.current_song:
                pygame.mixer.music.load(song_path)
                pygame.mixer.music.play()
                self.current_song = song_path
                self.is_paused = False
                print(f"Playing: {os.path.basename(song_path)}")
        else:
            print("Invalid index.")

    def pause_song(self):
        """Pause or resume the current song."""
        if pygame.mixer.music.get_busy():
            if self.is_paused:
                pygame.mixer.music.unpause()
                self.is_paused = False
                print("Resumed")
            else:
                pygame.mixer.music.pause()
                self.is_paused = True
                print("Paused")

    def stop_song(self):
        """Stop the current song."""
        pygame.mixer.music.stop()
        self.current_song = None
        self.is_paused = False
        print("Stopped")

# Command-line interface to interact with the music player
def main():
    player = MusicPlayer()
    while True:
        print("\nCommands: add [file/folder], play [index], remove [index], pause, stop, playlist, quit")
        command = input("Enter command: ").strip().lower()

        if command.startswith("add"):
            path = command[4:].strip()
            player.add_song(path)

        elif command.startswith("remove"):
            try:
                index = int(command[7:].strip()) - 1
                player.remove_song(index)
            except ValueError:
                print("Invalid index.")

        elif command.startswith("play"):
            try:
                index = int(command[5:].strip()) - 1
                player.play_song(index)
            except ValueError:
                print("Invalid index.")

        elif command == "pause":
            player.pause_song()

        elif command == "stop":
            player.stop_song()

        elif command == "playlist":
            player.show_playlist()

        elif command == "quit":
            print("Exiting the music player.")
            break

        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
