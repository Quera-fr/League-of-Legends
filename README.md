

# League of Legends Streamlit App

## Description

This Streamlit application collects data from the League of Legends website and allows users to interact with an expert bot about the game. The collected data includes information about different champions in the game.

## Installation

1. Clone the repository:

   ```
   bash https://github.com/Mickevin/League-of_legends.git
   ```
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Set up your OpenAI API key in either Streamlit Secrets or as an environment variable:

   - Streamlit Secrets:

     Create a `secrets.toml` file in the same directory as your Streamlit app with the following content:

     ```toml
     [openai]
     openai_api_key = "your-api-key"
     ```
   - Environment variable:

     Set your OpenAI API key as an environment variable:

     ```bash
     export OPENAI_KEY=your-api-key
     ```
2. Run the Streamlit app:

   ```bash
   streamlit run Dashboard.py
   ```
3. Access the app in your web browser.

## Features

- **Champion Information:** View information about League of Legends champions, including their names, roles, descriptions, and images.
- **Database Integration:** The app uses an SQLite database to store champion information.
- **Chat with OpenAI:** Interact with an OpenAI-powered bot to discuss League of Legends. The bot has access to the champion data stored in the database.
- **CSV Download:** Download champion data as a CSV file.

## Screenshots

[Add screenshots or images of your app here]

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

```

Replace "your-api-key" with your actual OpenAI API key, and update any other placeholders as needed. Additionally, consider adding screenshots or images of your app in the "Screenshots" section for a visual representation of your project.
```
