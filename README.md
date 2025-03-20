# Greek Mythology Explorer

🔱 **Greek Mythology Explorer** is a Streamlit web application that allows users to explore the fascinating world of Greek mythology. Users can learn about various Greek gods, their family trees, interesting facts, and captivating stories.

## Features

- **God Explorer**: Select a Greek god to learn more about them, including their descriptions, images, parents, siblings, spouses, and children.
- **Family Tree**: Explore the divine lineage of Greek mythology with a visual family tree and a text-based family tree.
- **Did You Know**: Discover interesting facts about Greek mythology and learn about its impact on modern culture.
- **Stories**: Read captivating tales from Greek mythology and reflect on their meanings with thought-provoking questions.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/greek-mythology-explorer.git
    cd greek-mythology-explorer
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Install `ffmpeg`:
    - Download the `ffmpeg` zip file for Windows from [ffmpeg.org](https://ffmpeg.org/download.html).
    - Extract the contents of the zip file to a folder, e.g., `C:\ffmpeg`.
    - Add the `ffmpeg` bin directory to your system's PATH:
        - Open the Start Menu and search for "Environment Variables".
        - Click on "Edit the system environment variables".
        - In the System Properties window, click on the "Environment Variables" button.
        - In the Environment Variables window, find the "Path" variable in the "System variables" section and click "Edit".
        - Click "New" and add the path to the `ffmpeg` bin directory, e.g., `C:\ffmpeg\bin`.
        - Click "OK" to close all windows.

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501` to access the app.

## Project Structure

- `app.py`: The main Streamlit application file.
- `requirements.txt`: The list of required Python packages.

## Dependencies

- `streamlit`
- `requests`
- `yt-dlp`
- `ffmpeg`

## Screenshots

![God Explorer](screenshots/god_explorer.png)
*God Explorer page*

![Family Tree](screenshots/family_tree.png)
*Family Tree page*

![Did You Know](screenshots/did_you_know.png)
*Did You Know page*

![Stories](screenshots/stories.png)
*Stories page*

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/)
- [GreekAPI by newsh](https://anfi.tk/greekApi/person/en)

---

*Explore the fascinating world of Greek mythology with Greek Mythology Explorer!*
