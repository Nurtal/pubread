import pyttsx3


def tell_from_text(text:str)->None:
    """Use speaker to output text
    Args:
        text (str) : text to tell
    """

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



if __name__ == "__main__":

    speek_from_text("Hello World !")
