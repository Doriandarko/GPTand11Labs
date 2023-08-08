# Chat Assistant Application
This is a Python script that allows you to interact with an AI assistant in the console. The assistant uses the OpenAI GPT-3 model for generating text responses, and the ElevenLabs API for converting these responses into audio. The assistant is designed to simulate the character Samantha from the movie 'Her'.
## Getting Started
### Prerequisites
- Python 3.6+
- OpenAI Python v0.27.0
- ElevenLabs Python SDK
### Installation
- Clone the repository
- Install the required packages using pip:
    - openai
    - elevenlabs
- Replace 'YOUR KEY' in the script with your actual API keys provided by OpenAI and ElevenLabs.
## Usage
Run the script using Python.
Once the script is running, you can interact with the assistant by typing your messages into the console. The assistant will respond with both text (printed to the console) and audio.
To end the conversation, type "quit".
## Customization
You can customize the assistant's behavior by modifying the system message in the script. This message sets the assistant's "persona". For example, the default persona is Samantha from the movie 'Her'.
You can also change the voice of the assistant by modifying the voice parameter in the script.
## License
This project is licensed under the terms of the MIT license.