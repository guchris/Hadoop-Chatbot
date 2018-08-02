# Operating Guide

## Prerequisites 

First, make sure you have Python 3.6 or greater installed.
Run the following commands in the Command Prompt window.

## Install Rasa Core
The recommended way to install Rasa Core is uing pip:

`pip install rasa_core`

If you already have rasa_core installed and want to udpate it, run:

`pip install -U rasa_core`

If you want to use the bleeding edge version of Rasa, use github + setup.py:

`git clone https://github.com/RasaHQ/rasa_core.git`

`cd rasa_core`

`pip install -r requirements.txt`

`pip install -e .`

## Add Natural Language Understanding

We used Rasa NLU for intent classification & entity extraction. To get it, run

`pip install rasa_nlu[tensorflow]`

If you want to use the bleeding edge verion, use github + setup.py:

`git clone https://github.com/RasaHQ/rasa_nlu.git`

`cd rasa_nlu`

`pip install -r requirements.txt`

`pip install -e .`

## Setup the Backend

The processing pipeline we used with rasa NLU is a combination of spaCy and scikit-learn.

Installing spacy just requires:

`pip install rasa_nlu[spacy]`

`python -m spacy download en_core_web_md`

`python -m spacy link en_core_web_md en`

## Clone Repo

Next, you need to clone the Github repository:

`git clone https://github.com/Gooey101/Hadoop-Chatbot.git`

You can now go into that directory and access all the files.

## Training
Once you have successfully installed Rasa and cloned the repo, you can now begin training. In the Command Prompt, run this command:

`python bot.py train`

This will run NLU and Dialogue training. If you only want to run one of these, you can use the `train-nlu` or `train-dialogue` command instead.
Note: Dialogue training will take longer than NLU training.

## Running the website
First, you need to install rasa-addons:

`pip install rasa-addons`

While in the directory, launching the website requires this command:

`python website.py`

The website will take a few moments to load. You can access it by clicking on the index.html file to open it in your browser. The backend will continue running until the window is closed.

## Generate training data

Inside the Chatito folder, you will find text files that contain the settings for [Chatito](https://github.com/rodrigopivi/Chatito). Using these files on Chatito will generate the training data we used.

## Extra info

This is not something we looked into, but may be useful in the future if not using Rasa's paid-for platform: [Rasa Dashboard](https://github.com/paschmann/rasa-ui).