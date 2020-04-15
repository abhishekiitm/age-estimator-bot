
# Age Estimator Bot
This is the code for a Rasa powered chatbot which is connected to Facebook messenger.
A user can talk to this bot and share his or her photo and the bot will try to guess the user's age.
Anyone who wishes to do the following will find this code useful:
1. Customize Rasa to run scripts based on 
2. Write a script that can estimate age given facial image
3. Connect their Rasa chat bot to Facebook messenger

## Facial Age Estimation 
Check out [Shichao Li's Github repository](https://github.com/Nicholasli1995/VisualizingNDF) for the source of the deep learning model that predicts the age given an image. All copyrights belong to them. Thankfully, they have open sourced their code under the MIT License.

## Chat bot Framework 
The chatbot is powered by [Rasa, an open source conversational AI framework for building contextual assistants](https://rasa.com/docs/getting-started/)

## Pre-trained Model
Download the pre-trained model [here](https://drive.google.com/drive/folders/1DM6wVSknkYBqGf1UwHQgJNUp40sYDMrv) 
You will need to download the model named CACD_MAE_4.59.pth only as that is the only one relevant for age estimation.
This model belongs to and is trained by Shichao Li. Check out their [Github page](https://github.com/Nicholasli1995/VisualizingNDF) for more details.

## License
MIT

