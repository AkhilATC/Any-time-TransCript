from factory import celery
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import uuid



@celery.task()
def add_two(x, y):
    print("cool:::")
    print(x+y)
    return x + y


# a function that splits the audio file into chunks
# and applies speech recognition
@celery.task(bind=True)
def get_large_audio_transcription(self, file_path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    self.update_state(state='PROGRESS', meta={"total": 100, "current": 0, 'status': 'start'})
    r = sr.Recognizer()
    # open the audio file using pydub
    sound = AudioSegment.from_wav(file_path)
    self.update_state(state='PROGRESS', meta={"total": 100, "current": 1, 'status': 'audio file convertion started'})
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = str(uuid.uuid4()).replace('-', '_')
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    self.update_state(state='PROGRESS', meta={"total": 100, "current": 5, 'status': 'fetching..'})
    print(len(chunks))
    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        self.update_state(state='PROGRESS', meta={"total": 100, "current": 20,'status': 'converstion'})
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print(text)
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                # print(chunk_filename, ":", text)
                whole_text += text

    self.update_state(state='PROGRESS', meta={"total": 100, "current": 90,'status': 'done'})
    # return the text for all chunks detected
    try:
        path = os.path.join(folder_name)
        os.rmdir(path)
        print(f"Removing folder {path}")
        if os.path.exists(file_path):
            print(f"Removing folder {file_path}")
            os.remove(file_path)
    except Exception as e:
        print(e)
        print("exception")
    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': whole_text}
