import gradio as gr
import yt_dlp as ydlp
from transformers import pipeline

from whispercpp import Whisper
summarizer = pipeline("summarization", model="knkarthick/MEETING_SUMMARY")

def download_audio(youtube_url, output_folder='.'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_folder}/audio',
    }

    with ydlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])


w = Whisper('tiny')


def process_general_transcription(transcription):
    formatted_transcription = []
    
    for line in transcription:
        if line.startswith('[') and line.endswith(']'):
            formatted_transcription.append(f'\n--- {line[1:-1].upper()} ---\n')
        else:
            formatted_transcription.append(line)

    transcript_str = "\n".join(formatted_transcription)
    
    return transcript_str
def chunk_to_tokens(text, n):
        tokens = text.split()
        max_chunk_size = min(len(tokens), 512) 
        
        token_size = max(1, int(max_chunk_size * (1 - n / 100)))
        
        chunks = [" ".join(tokens[i:i + token_size]) for i in range(0, len(tokens), token_size)]

        return chunks
def summarizing(text,n):
    valid_tok=chunk_to_tokens(text,n)
    res=""
    for i in valid_tok:
        res+=summarizer(i)[0]['summary_text']+'\n'
    return res
def transcribe_sum_youtube(youtube_url,n):
    download_audio(youtube_url)
    result = w.transcribe("audio.wav")
    text = w.extract_text(result)
    res=process_general_transcription(text)
    return summarizing(res,n)


with gr.Blocks() as demo:
    gr.Markdown(
    """
    # CPP Whisperer - YouTube Videos Summarizer
    
    """)
    with gr.Row():
        with gr.Column():

            inp = gr.Textbox(label="Youtube Url",placeholder="Insert YT Url here")
            inp2 = gr.Slider(label="Summarization Percentage",min_value=0,max_value=100,step_size=1)
            result_button_transcribe = gr.Button('Transcribe and Summarize')

        with gr.Column():
            out = gr.Textbox(label="Transcribed and Summarize Text")
    
    
    result_button_transcribe.click(transcribe_sum_youtube, inputs = [inp,inp2] , outputs = out)


demo.launch()
