# Load pre-trained data and save it before running an API server.
import gensim.downloader

model = gensim.downloader.load('glove-twitter-25')
model.save('glove.model')
