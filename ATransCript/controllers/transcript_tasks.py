from factory import celery
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence



@celery.task()
def add_two(x, y):
    print("cool:::")
    print(x+y)
    return x + y

def convert_speech(file_):
    r = sr.Recognizer()
    extention = file_.filename.split('.')[-1].lower()
    if extention == 'mp4':
        AudioSegment.from_file_using_temporary_files(file_)
