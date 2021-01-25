from typing import Optional
from fastapi import FastAPI
from gensim.models import KeyedVectors

model = KeyedVectors.load('glove.model', mmap='r')
app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.get('/similar/glove/{word}')
def read_glove(word: str, n: Optional[int] = 10):
    sims = model.most_similar(word, topn=n)
    return {'most_similar': sims}
