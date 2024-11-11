# Command-Line Music Player

A Python-based music player that allows users to manage and play their MP3 songs via the command line. This music player lets you create custom playlists, add songs, play, pause, and stop songs, and provides basic playlist management with an interactive interface.

## Features

- **Custom Playlist**: Add songs or entire folders to create a playlist of MP3 files.
- **Play, Pause, and Stop**: Simple commands to control music playback.
- **Playlist Management**: Add/remove songs, and view your current playlist.
- **Command-Line Interface**: Easy-to-use interface for interacting with the player.

## Key Concepts & Libraries Used

- **Pygame**: Used the Pygame mixer module for handling MP3 files, playing, pausing, and stopping music.
- **File Handling**: Python’s `os` module helps navigate directories and identify MP3 files for batch addition to playlists.
- **Control Structures**: Implemented an interactive command-line interface to manage commands like add, play, pause, stop, and view playlist.
- **Error Handling**: Input validation for commands and playlist indices to prevent crashes and provide smooth user feedback.

## Requirements

- Python 3.x
- Pygame library

## Usage
Use the following commands to interact with the music player:

- **add [song_path]**: Add a song to the playlist.
- **add folder [folder_path]**: Add all MP3 files from a folder to the playlist.
- **play [song_index]**: Play a song from the playlist by its index.
- **pause**: Pause the current song.
- **stop**: Stop the song.
- **view**: View the current playlist.

## How to Run

1. Clone this repository to your local machine.
2. Install the required libraries:
   ```bash
   pip install pygame
3.Run the music player program:
  ```bash
  python musicplayer.py

