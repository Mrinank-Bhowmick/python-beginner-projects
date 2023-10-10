from whispercpp import Whisper

w = Whisper('tiny')

result = w.transcribe("audio.wav")
text = w.extract_text(result)
def process_general_transcription(transcription):
    formatted_transcription = []
    
    for line in transcription:
        # Check if the line contains a marker (starts and ends with [])
        if line.startswith('[') and line.endswith(']'):
            formatted_transcription.append(f'\n--- {line[1:-1].upper()} ---\n')
        else:
            formatted_transcription.append(line)

    # Convert list to string
    transcript_str = "\n".join(formatted_transcription)
    
    return transcript_str
print(process_general_transcription(text))