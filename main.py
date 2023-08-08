import openai
import elevenlabs

# Setting up the OpenAI and ElevenLabs API keys
openai.api_key = 'YOUR KEY'
elevenlabs.set_api_key('YOUR KEY')


def interact_with_assistant():
  while True:
    # Get user input from the console
    user_input = input("You: ")

    # If the user types "quit", end the conversation
    if user_input.lower() == "quit":
      break

    # Create a chat with the GPT-4 model using the OpenAI API
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{
        "role":
        "system",
        "content":
        "You are an advanced AI, similar to the character from the movie 'Her'. Your name is Samantha."
      }, {
        "role": "user",
        "content": user_input
      }])

    # Get the assistant's reply
    assistant_reply = response['choices'][0]['message']['content']
    print("\033[93m" + "Assistant: " + assistant_reply +
          "\033[0m")  # Print the reply in yellow

    # Generate audio from the text using the ElevenLabs API with streaming enabled
    audio_stream = elevenlabs.generate(text=assistant_reply,
                                       voice="Bella",
                                       model="eleven_monolingual_v1",
                                       stream=True)

    # Play the generated audio stream
    elevenlabs.stream(audio_stream)


# Start the conversation
interact_with_assistant()
