# import speech_recognition as sr

# # Create a speech recognition object
# r = sr.Recognizer()

# # Use the microphone as the audio source
# with sr.Microphone() as source:
#     print("Please say something:")
#     print("Adjusting for ambient noise...")
#     r.adjust_for_ambient_noise(source)
#     print("Recording audio...")
#     audio = r.listen(source, timeout=100)  # Adjust the timeout to 10 seconds
#     print("Audio recorded.")

#     try:
#         # Use the Google Speech Recognition API to recognize the audio
#         print("Recognizing audio...")
#         print("You said: " + r.recognize_google(audio))
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand your audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))






# from openai import OpenAI


# client = OpenAI(api_key="AIzaSyB1HnatKme48GvmTf_e28hwzCGyM4LT0cY")

# audio_file= open("C://Users//ashutosh.barwal//Downloads//CAR0001.wav", "rb")


# transcription = client.audio.transcriptions.create(
#   model="whisper-1", 
#   file=audio_file
# )

# print(transcription.text)

# import speech_recognition as sr

# # Create a speech recognition object
# r = sr.Recognizer()

# # Use a WAV file as the audio source
# with sr.AudioFile("path/to/audio.wav") as source:
#     audio = r.record(source)

#     try:
#         # Use the Google Speech Recognition API to recognize the audio
#         print("You said: " + r.recognize_google(audio))
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand your audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))






import pyaudio
import wave

# Set the parameters for the recording
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output.wav"

# Create a PyAudio object
audio = pyaudio.PyAudio()

# Open the stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")
frames = []

# Record for RECORD_SECONDS seconds
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording")

# Close the stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded data as a WAV file
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()