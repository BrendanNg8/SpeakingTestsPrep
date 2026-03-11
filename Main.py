import random
from gtts import gTTS
import os
import platform

questions: list = [
        "¿Has hecho ejercicio con tu amigo?",
        "¿Has tenido un entrenador o un nutricionista?",
        "¿Has corrido en una cinta caminadora?",
        "¿Te has entrenado para un deporte?",
        "¿Has levantado pesas esta semana?",
        "¿Te habías apurado para llegar a esta clase a tiempo?",
        "¿Habías roto un hueso antes de venir a la escuela secundaria?",
        "¿Habías comido una merienda antes de llegar a esta clase?",
        "¿Te habías mantenido en forma durante el invierno?",
        "¿Habías estudiado antes de tomar este examen?"
    ]
def playRandomQuestion(question: list) -> None: 
    question: str = random.choice(questions)
    print(question)

    tts = gTTS(text=question, lang='es', slow=False)  


    audio_file = "question.mp3"
    tts.save(audio_file)

    if platform.system() == "Windows": 
        os.system(f"start {audio_file}")
    elif platform.system() == "Darwin":  
        os.system(f"afplay {audio_file}")
    else:  
        os.system(f"mpg123 {audio_file}")  

playRandomQuestion(questions)


