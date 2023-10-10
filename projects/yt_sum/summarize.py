from transformers import pipeline
summarizer = pipeline("summarization", model="knkarthick/MEETING_SUMMARY")
pr_text=""""""
def chunk_to_tokens(text, n):
    tokens = text.split()
    max_chunk_size = min(len(tokens), 512) 
    
    token_size = max(1, int(max_chunk_size * (1 - n / 100)))
    
    chunks = [" ".join(tokens[i:i + token_size]) for i in range(0, len(tokens), token_size)]

    return chunks

valid_tok=chuck_to_tokens(pr_text,12)
res=""
for i in valid_tok:
    res+=summarizer(i)[0]['summary_text']+'\n'


