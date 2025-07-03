# Wheel of Life

This tool is an interactive life compass that lets you assess various areas of your life. The categories and their options are defined in `wheel_of_life.json`. The app visualizes your selections as a radar chart.

## Features
- Each life category (e.g., Leisure, Finances, Health) has several options with positive or negative weighting.
- You can check what you experienced or achieved for each day or period.
- Points are normalized per category (maximum 10, negative values are subtracted).
- Results are displayed as a clear radar chart.

## Files
- **kompass.py**: Streamlit app providing the user interface and visualization.
- **wheel_of_life.json**: Contains all categories and their options (including emojis and weights).

## Installation
1. Make sure Python 3.8+ is installed.
2. Install the required packages:
   ```
   pip install streamlit plotly
   ```

## Usage
Start the app with:
```
streamlit run kompass.py
```

## Customization
- You can freely adjust the categories and options in `wheel_of_life.json` (e.g., add more categories, change weights, add new emojis).
- The app is designed to automatically adapt to the contents of `wheel_of_life.json`.

## Online Demo
You can also try the tool online:
[https://wheelofday.streamlit.app](https://wheelofday.streamlit.app)

## Example Screenshot
![{5495BB94-1E98-4F90-B6D5-63BC1B98E5BC}](https://github.com/user-attachments/assets/35b2bd89-9644-4805-94fc-da839c3708ae)


---
Enjoy reflecting and visualizing your life compass!

