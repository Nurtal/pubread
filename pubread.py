import speech_recognition as sr


def extract_text_from_audio(audio_file):
    """Extract text content from audio file
    work with .wav file

    Args:
        audio_file (str) : path to the audio file

    Return:
        (str) : content extracted from audio file
    
    """
    
    r = sr.Recognizer()
    data = sr.AudioFile(audio_file)
    with data as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
    text = r.recognize_google(audio)
    return text



if __name__ == "__main__":

    machin = extract_text_from_audio("data/harvard.wav")
    print(machin)

