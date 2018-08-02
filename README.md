# Operating Guide

## Prerequisites 

First, make sure you have Python 3.6 or greater installed. Python 3.6.3 can be installed from the [UP IT Services Store](https://home.www.uprr.com/myup/)

## Install Rasa
Run this command in the Command Prompt window:

`pip install rasa_core`

We also need to NLU:

`pip install rasa_nlu[tensorflow]`

Next, you need to clone the Gitlab repository:

`git clone duit999@git-dev.uit.tla.uprr.com:hadoop-chatbot/hadoop-chatbot.git`

You can now go into that directory and access all the files.

## Setup the backend
We are using a combination of spaCy and sklearn for our backend. Here's how to install:

`pip install rasa_nlu[spacy]`

`python -m spacy download en_core_web_md`

Normally, we would also link these files (via `python -m spacy link en_core_web_md en`), however we were unable to do this on our computers. Instead, our current configuration calls upon the files directly. If your setup links the files, the configuration file will need to be updated.
## Training
Once you have successfully installed Rasa and cloned the repo, you can now begin training. In the Command Prompt, run this command:

`python bot.py train`

This will run NLU and Dialogue training. If you only want to run one of these, you can use the `train-nlu` or `train-dialogue` command instead. Dialogue training will take longer than NLU training.
## Running the website
First you need to install rasa-addons:

`pip install rasa-addons`

While in the directory, launching the website requires this command:

`python website.py`

The website will take a minute to load. You can access it by clicking on the index.html file to open it in your browser. The backend will continue running until the window is closed.

## Generate training data

Inside the Chatito folder, you will find text files that contain the settings for [Chatito](https://github.com/rodrigopivi/Chatito). Using these files on Chatito will generate the training data we used.

## Extra info

This is not something we looked into, but may be useful in the future if not using Rasa Platform: [Rasa Dashboard](https://github.com/paschmann/rasa-ui).