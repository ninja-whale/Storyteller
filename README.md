# Storyteller

Storyteller is an AI-powered web application that generates creative stories from images. Upload an image, and the app will describe the content and generate a unique story based on the image. The story can also be converted to audio using text-to-speech technology.

## Features

- **Image to Text**: Uses an AI model to describe the content of an uploaded image.
- **Text Generation**: Generates a creative story based on the image description.
- **Text-to-Speech**: Converts the generated story into audio.
- **Web Interface**: Easy-to-use web interface for uploading images and reading/listening to stories.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask, Python
- **AI Models**: 
  - [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base) for image captioning.
  - [GPT-2](https://huggingface.co/gpt2) for story generation.
- **Text-to-Speech**: Google Text-to-Speech (gTTS)

## Project Structure

```
Storyteller/
│
├── static/
│   ├── audio.mp3          # Generated audio file
│   └── input_image.jpg    # Uploaded image file
│
├── templates/
│   └── index.html         # HTML template for the web interface
│
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Setup and Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/ninja-whale/storyteller.git
    cd storyteller
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the necessary models:**
    - You will need the `Salesforce/blip-image-captioning-base` and `gpt2` models from Hugging Face. They will be downloaded automatically the first time you run the app.

5. **Run the Flask application:**
    ```bash
    python app.py
    ```

6. **Open your browser and navigate to:**
    ```
    http://127.0.0.1:5000/
    ```

## Usage

1. **Upload an Image**: Choose an image from your device to upload.
2. **Generate Story**: Click the "Generate Story" button. The app will process the image, generate a story, and display it on the screen.
3. **Listen to the Story**: The story will be converted to audio, and you can listen to it directly on the webpage.

## Example

1. **Input**: An image of a cat sitting on a windowsill.
2. **Generated Story**: "The curious cat sat by the window, watching the world go by. It dreamed of adventures beyond the glass, chasing birds and exploring the unknown..."
3. **Audio**: The story is narrated using the text-to-speech feature.

## Contributing

Contributions are welcome! If you have any ideas or suggestions, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Hugging Face](https://huggingface.co/) for providing the image captioning and text generation models.
- [Google Text-to-Speech (gTTS)](https://gtts.readthedocs.io/) for text-to-speech conversion.

