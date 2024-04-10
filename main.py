import os
import wave
import struct
import pyaudio
import time
from tqdm import tqdm

def encode_file_to_audio(file_path, output_path):
    try:
        # Read the file contents
        with open(file_path, 'rb') as file:
            file_data = file.read()

        # Create a new WAV file
        with wave.open(output_path, 'w') as wav_file:
            # Set the WAV file parameters
            wav_file.setnchannels(1)  # Mono
            wav_file.setsampwidth(2)  # 2 bytes per sample
            wav_file.setframerate(44100)  # 44.1 kHz sample rate

            # Encode the file data into audio samples
            print("\033[93mEncoding file to audio...\033[0m")
            for byte in tqdm(file_data, desc="Encoding", unit="byte"):
                sample = struct.pack('<h', byte * 256)
                wav_file.writeframesraw(sample)

        print(f"\033[92mFile encoded to audio successfully. Output: {output_path}\033[0m")
    except FileNotFoundError:
        print(f"\033[91mError: File not found - {file_path}\033[0m")
    except Exception as e:
        print(f"\033[91mError: {str(e)}\033[0m")

def decode_audio_to_file(output_path, use_mic=True, wav_file_path=None):
    try:
        if use_mic:
            # Initialize PyAudio
            audio = pyaudio.PyAudio()

            # Open the default microphone stream
            stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

            print("\033[93mListening for audio...\033[0m")

            # Start recording audio
            frames = []
            while True:
                data = stream.read(1024)
                frames.append(data)

                # Check if the audio has ended (silence detected)
                if len(data) == 0:
                    break

            print("\033[93mAudio recording completed.\033[0m")

            # Stop and close the microphone stream
            stream.stop_stream()
            stream.close()
            audio.terminate()

            # Save the recorded audio as a temporary WAV file
            with wave.open("temp_audio.wav", 'wb') as wav_file:
                wav_file.setnchannels(1)
                wav_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
                wav_file.setframerate(44100)
                wav_file.writeframes(b''.join(frames))

            # Open the temporary WAV file for reading
            with wave.open("temp_audio.wav", 'rb') as wav_file:
                # Read the audio samples
                audio_data = wav_file.readframes(wav_file.getnframes())

            # Clean up the temporary audio file
            os.remove("temp_audio.wav")
        else:
            # Open the selected WAV file for reading
            with wave.open(wav_file_path, 'rb') as wav_file:
                # Read the audio samples
                audio_data = wav_file.readframes(wav_file.getnframes())

        # Decode the audio samples back to file data
        file_data = bytearray()
        print("\033[93mDecoding audio to file...\033[0m")
        for i in tqdm(range(0, len(audio_data), 2), desc="Decoding", unit="sample"):
            sample = struct.unpack('<h', audio_data[i:i+2])[0]
            byte = sample // 256
            file_data.append(byte)

        # Write the decoded file data to the output file
        with open(output_path, 'wb') as file:
            file.write(file_data)

        print(f"\033[92mAudio decoded to file successfully. Output: {output_path}\033[0m")
    except FileNotFoundError:
        print(f"\033[91mError: WAV file not found - {wav_file_path}\033[0m")
    except Exception as e:
        print(f"\033[91mError: {str(e)}\033[0m")

def display_menu():
    print("\033[96m=== Audio Encoder/Decoder ===\033[0m")
    print("1. Encode file to audio")
    print("2. Decode audio to file")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            file_path = input("Enter the path of the file to encode: ")
            encoded_audio_path = input("Enter the output path for the encoded audio: ")
            encode_file_to_audio(file_path, encoded_audio_path)
        elif choice == '2':
            decoded_file_path = input("Enter the output path for the decoded file: ")
            use_mic = input("Use microphone for audio input? (y/n): ").lower() == 'y'
            if not use_mic:
                wav_file_path = input("Enter the path of the WAV file to decode: ")
                decode_audio_to_file(decoded_file_path, use_mic=False, wav_file_path=wav_file_path)
            else:
                decode_audio_to_file(decoded_file_path)
        elif choice == '3':
            print("\033[93mExiting...\033[0m")
            break
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")

        print()

if __name__ == '__main__':
    main()