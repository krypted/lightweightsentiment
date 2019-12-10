# lightweightsentiment
lightweightsentiment is a Lightweight Sentiment Analysis Tool built using python. 

## Requirements
It was written to conform to python 2 or 3 and requires the following modules installed (newer versions may work):

nltk==3.4.5

textblob==0.15.3

## Usage

python input.py --text "Gosh, I hate this feature"

The output would then be a number between -1.0 and 1.0. For example:

-0.8

## Microservice

This service could be hosted as a lambda or google cloud function. If it were then it could be called from another application by simply sending the text in a standard json format with a response of the same floating point integer. 
