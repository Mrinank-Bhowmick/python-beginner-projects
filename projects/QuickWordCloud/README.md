## QuickWordCloud
Quick word cloud is a small and interesting project that can quickly create a word cloud out of a text file.
Its a small & helpful project that can be used in websites or for different analysis.  

## Example

1. Place a plain-text file at `./data/test_data.txt` (or update `file_name` in `main.py`).
2. Run `python main.py`. The script reads all words from the file, converts them to lowercase, and generates a 1600x800 word cloud.
3. A matplotlib window opens displaying the word cloud image with a white background. Frequently occurring words appear larger. Close the window to exit.

## Installation

### Install and activate a virtual env
```
pip3 install virtualenv
python -m venv quickwordcloud
source quickwordcloud/bin/activate
```

### Install dependencies
```
pip3 install -r requirements.txt
```

### Formatting
```
black file_name.py
```

### Unit Test
```
pytest
```

### Run
From IDE right click and run.(As per the IDE options)  

From terminal python main.py
