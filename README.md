
# Audio Encoder/Decoder

This Python script allows you to encode files into audio and decode audio back into files. It provides a user-friendly interface for selecting between encoding a file to audio or decoding audio to a file.

## Features

- Encode any file into audio format (WAV)
- Decode audio from microphone input or WAV file back into the original file format
- User-friendly menu for easy navigation
- Progress tracking with loading bars
- Color-coded output for enhanced readability
- Error handling for file not found and other exceptions

## Requirements

- Python 3.x
- `pyaudio` library
- `tqdm` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/audio-encoder-decoder.git
   ```

2. Install the required libraries:

   ```bash
   pip install pyaudio tqdm
   ```

## Usage

1. Run the script:

   ```bash
   python audio_encoder_decoder.py
   ```

2. Choose an option from the menu:

   - Option 1: Encode file to audio
     - Enter the path of the file to encode
     - Enter the output path for the encoded audio
   - Option 2: Decode audio to file
     - Enter the output path for the decoded file
     - Choose whether to use the microphone or a WAV file for audio input
       - If using a WAV file, enter the path of the WAV file to decode
   - Option 3: Exit the script

3. Follow the prompts and wait for the encoding/decoding process to complete.

4. The encoded audio or decoded file will be saved to the specified output path.

## Examples

Encode a file to audio:

```
Enter your choice (1-3): 1
Enter the path of the file to encode: /path/to/file.txt
Enter the output path for the encoded audio: /path/to/encoded_audio.wav
```

Decode audio from a WAV file:

```
Enter your choice (1-3): 2
Enter the output path for the decoded file: /path/to/decoded_file.txt
Use microphone for audio input? (y/n): n
Enter the path of the WAV file to decode: /path/to/audio.wav
```

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The `pyaudio` library for audio input/output functionality.
- The `tqdm` library for progress tracking.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
