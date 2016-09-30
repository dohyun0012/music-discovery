# Music Discovery
For large scale recommendation systems, collaborative filtering has been one of the industry standard algorithms for quite some time. In music, this algorithm will recommend you songs that other people with similar tastes as you are enjoying. This works very well for music with existing usage data. However, this algorithm fails to recommend brand new songs or newer songs that only a few people have listened to. Also known as a cold start problem, this is a major weakness of the collaborative filtering algorithm. There are a lot of great new songs which people may want to check out.

One way to address this problem, as introduced by Aäron van den Oord, Sander Dieleman, and Benjamin Schrauwen in their paper titled "Deep content-based music recommendation" is to use a convolutional neural network to listen to a clip of the new song to predict what the collaboritive filtering algorithm would have done. This model takes in as its input the actual audio content of the songs! In a sense, the model is "listening" to the song. So what is this convolutional neural network trying to predict? It turns out that the collaborative filtering algorithm (specifically weighted matrix factorization) will make a vector representation of each song. This vector has numbers called latent features which measures a certain "direction" of the sound in the space of music. For instance, the first number may tell you how "rock" the song is (recall that this is all based on user behavior and not the actual audio content).

I trained a convolutional neural network and can now predict the vector representation of new songs and unpopular songs so that we can recommend them! To demonstrate that the model actually learned and is outputting something reasonable, I plotted the vector representation of 10,000 new songs that the model has not heard previously onto a 2-dimensional TSNE graph. You can check out the map here?

## Files
`hdf5_getters.py` helper function to retrieve data from Million Song Dataset
`X.ipynb` retrieve features from the Million Song Dataset
`Y.ipynb` retrieve vector representation of songs via collaborative filtering on data from the Echo Nest API
`data.ipynb` combine and preprocess the data
`model.ipynb` train the convolutional neural network
`model.h5` the trained model saved
`predictions.ipynb` feed songs from test set to the convnet and get predictions
`tsne.ipynb` map the 10-dimensional song vectors to 2-dimensional tsne vectors
`recommendation.ipynb` recommend songs based on the convnet model
`app` d3 interactive TSNE graph with ability to input song names

## Citation
https://papers.nips.cc/paper/5004-deep-content-based-music-recommendation.pdf
