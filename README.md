# Assistive AI Companion

An AI companion that learns and grows with you, controlling your smart home ecosystem while interacting based on your emotions and context. This project aims to create an AI companion that is so personalized that it evolves and adapts like a pet. It can recognize emotions, personalize its voice interactions, learn over time, and integrate with a smart home system.

## Features

1. **Emotional Recognition**: Understands and responds to your emotional state through facial expressions and tone of voice.
2. **Voice Personalization**: Adapts to and recognizes your voice, creating a more personalized interaction.
3. **Self-Learning**: Learns from every interaction to provide more relevant responses over time.
4. **Smart Home Integration**: Seamlessly controls smart home devices based on voice commands or contextual understanding.

## Project Structure

```bash
AssistiveAICompanion/
├── main.py                      # Main entry point for the AI companion
├── assistant.py                 # Core assistant logic to handle commands
├── voice_assistant.py           # Handles voice recognition and speech synthesis
├── nlp_processing.py            # Natural language processing and OpenAI API interaction
├── smart_home.py                # Placeholder for smart home integration logic (future feature)
├── utils/
│   ├── speech_utils.py          # Utility for text-to-speech functions
│   └── openai_utils.py          # Utility for interacting with OpenAI's GPT model
├── models/
│   └── custom_model.h5          # Pre-trained or custom models (for emotion recognition, voice, etc.)
├── data/
│   ├── voice_samples/           # Folder for storing voice sample files
│   │   └── user1_sample.wav
│   ├── training_data.txt        # Example text file for training data
│   └── image_data/              # Folder for storing images used for emotion recognition
│       └── sample_image.png
├── requirements.txt             # Dependencies and packages for the project
└── README.md                    # Project description and instructions
```


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

1. **Python 3.7 or higher**: Ensure you have Python installed on your machine.
2. **Pip**: Install the required libraries using `pip`.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/AssistiveAICompanion.git
   ```
2. **Navigate into the project directory**
   ```bash
   cd AssistiveAICompanion
   ```
3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Running The Application

1. **Once the dependencies are installed, you can run the AI Companion**
   ```bash
   python main.py
   ```
2. **The AI Companion will start listening for commands. Say 'stop' to exit the program.**

## Usage

***Speech Recognition:*** The companion listens for voice input through a microphone.
***OpenAI Integration:*** The assistant can provide intelligent responses using the GPT model.
***Voice Personalization:*** It speaks responses using Google Text-to-Speech (gTTS).
***Smart Home Commands:*** Future integration to control smart home devices (e.g., lights, thermostat) is planned.


## Example Interactions:

***Greeting:***
```bash
User: Hello
AI: Hello! How can I help you today?
```

***Requesting the Weather:***

```bash
User: What's the weather like?
AI: It's a sunny day with a high of 75 degrees.
```

***Writing Notes:***

```bash
User: Write down the meeting notes for today.
AI: (Provides the requested information and stores it.)
```

## Customization
You can easily customize and extend the project by:

Adding new commands and intents in the nlp_processing.py file.
Training custom machine learning models and adding them to the models/ directory.
Expanding the smart home integration by creating more functionalities in the smart_home.py file.


## Project Files Overview
1. main.py
The main entry point that starts the AI companion, listens for commands, and handles interactions.

2. assistant.py
Central logic that coordinates between voice recognition, natural language processing, and response generation.

3. voice_assistant.py
Handles voice input (listening and transcribing) using Google's speech recognition and text-to-speech functionalities.

4. nlp_processing.py
Processes text input using SpaCy for intent recognition and integrates with OpenAI to generate intelligent responses.

5. utils/ directory
Contains utility modules:

speech_utils.py: Functions for text-to-speech playback using Pygame and gTTS.
openai_utils.py: Functions for interacting with OpenAI’s GPT models, maintaining conversation history.


## Dependencies
The following packages are required to run the project and are listed in requirements.txt:

***SpeechRecognition:*** For speech-to-text functionality.
***gTTS:*** For converting text to speech.
***Pygame:*** For playing back audio.
***SpaCy:*** For natural language processing.
***OpenAI:*** For using GPT models to generate responses.

You can install them using:

```bash
pip install -r requirements.txt
```

## Future Enhancements

***Emotional Recognition:*** Add emotional detection using facial expression analysis.
***Smart Home Integration:*** Implement more advanced control of smart home devices like lights, thermostats, and alarms.
***Custom Voice Models:*** Enable personalized voice models based on individual users.

## Contributing
Feel free to fork the repository and submit pull requests if you wish to contribute to this project. Your contributions are what make the open-source community a wonderful place to learn, inspire, and create.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

### How to Use the README:

- Replace `yourusername` in the Git clone command with your GitHub username or the actual repository URL.
- The `models/custom_model.h5` is a placeholder, and you can replace it once you train any custom models for the project.
- For smart home integration, make sure to implement the necessary logic in `smart_home.py` or any API-specific scripts for device control.

Let me know if you need any further adjustments!