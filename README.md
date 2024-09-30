
# Drowsy Driver Project

![Demo video of the project](readme_assets/demo.gif)

## Overview

The **Drowsy Driver** project is a real-time driver fatigue monitoring software designed to enhance road safety. It utilizes facial recognition to detect eye and mouth movements that indicate drowsiness and alerts the driver when signs of fatigue are detected. The system uses Computer Vision techniques to track facial landmarks and detect closed eyes or yawning, providing real-time warnings through visual and auditory alerts.

See our showcase here: https://www.drowsydriver.co/

☝️ Repo for the website [here](https://github.com/javiiicz/drowsydriver-app).

## Features

- **Eye and Mouth Monitoring**: Uses the Eye Aspect Ratio (EAR) and Mouth Aspect Ratio (MAR) to monitor eye closure and yawning.
- **Drowsiness Detection**: Detects prolonged eye closure or yawning that indicates drowsiness and triggers visual and auditory alerts.
- **Speech Alerts**: Utilizes Azure Cognitive Services for speech synthesis to vocally alert the driver when drowsiness is detected.
- **Facial Landmark Detection**: Tracks facial landmarks using `dlib` and OpenCV to calculate EAR and MAR.
- **Flask Backend**: Provides a REST API using Flask to launch the drowsiness detection system.

## Installation

### Prerequisites

1. Python 3.x
2. Required Python packages:
   ```bash
   pip install opencv-python dlib scipy azure-cognitiveservices-speech flask flask-cors
   ```
3. **face_data.dat**: Pre-trained facial landmark model file for detecting facial landmarks. Download it [here](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) and extract it as `face_data.dat` in your project directory.

4. **Azure Speech API Key**: You will need a subscription key and region for the Azure Cognitive Services Speech API. Replace the placeholder values in the Python script with your key and region.

### Usage

1. **Run the Flask API**
   In your terminal, navigate to the project folder and run the Flask server:
   ```bash
   python app.py
   ```
   This will start the Flask backend on `http://localhost:5000`.

2. **Start the Drowsiness Detection**
   To trigger the drowsiness detection GUI, send a POST request to the Flask API:
   ```bash
   curl -X POST http://localhost:5000/execute
   ```

   This will run the `eyechecker.py` script that opens the camera feed and starts monitoring.

### How It Works

1. **Eye Aspect Ratio (EAR)**: 
   The EAR is calculated for both eyes. If the ratio is below a threshold (0.23) for a continuous period, the system determines that the driver's eyes are closed.
   
2. **Mouth Aspect Ratio (MAR)**:
   The MAR is used to detect yawning. If the ratio exceeds 0.6 for a sustained time, yawning is detected.

3. **Alerts**:
   - If the eyes remain closed or yawning is detected for more than a certain duration, a warning message is displayed on the screen.
   - The system triggers a verbal warning using Azure's Text-to-Speech service.

### Customization

- **Adjust EAR/MAR Thresholds**: Fine-tune the drowsiness detection by modifying `EYE_AR_THRESHOLD` and `MOUTH_AR_THRESHOLD` in the `eyechecker.py` script.
- **Azure Speech Configuration**: Replace the placeholder Azure Cognitive Services key and region in the script with your own credentials.
- **Flask API**: The Flask API can be expanded to include additional endpoints for further functionality or monitoring.

## Project Structure

```
.
├── eyechecker.py              # Main drowsiness detection script
├── app.py            # Flask API backend to launch the detection system
├── face_data.dat              # Pre-trained model for facial landmarks detection
└── README.md                  # Project documentation
```

## Acknowledgments

- **OpenCV**: For real-time image processing and webcam feed.
- **dlib**: For detecting facial landmarks.
- **Azure Cognitive Services**: For the text-to-speech API used in the project.
