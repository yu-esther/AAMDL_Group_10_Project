# Age Detection Classifier.

The application uses [Streamlit](https://streamlit.io/) to deploy a computer vision application.

### Experiments
1. A simple architecture with 1 hidden dense layer of 500 neuron and output layer of 3 neuron since the prediction class is 3.
2. CNN
A convolutional neural network (CNN) architecture that is well-suited for image-related problems was tried and this immproves the model accuracy from 64.6% to 73.6% which represent 9pp improvement. 
CNNs are particularly effective for tasks like image classification.

A sample image has been provided for testing, it is available in the root directory as `200.jpg`

To run the application, 
- it is recmmended to create a python virtual environment
```sh
python -m venv env
# This works for windows machine
```
- activate the environment
```sh
env\Scripts\activate
# This works for windows cmd/powershell
source env/Scripts/activate # works with git bash
source env/bin/activate # works with linux/wsl
```
- install app dependencies
```sh
pip install -r requirements.txt

```
- run streamlit
```sh
streamlit run app.py
```

The streamlit server will be started and the webpage is opened with a placeholder to upload an image. 
The sample image can be downloaded and uploaded to make predictions with the application.

References:
Streamlit • A faster way to build and share data apps. (n.d.). https://streamlit.io/
