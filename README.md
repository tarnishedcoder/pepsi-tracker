

# Pepsi Consumption Calculator

## Description

This is a simple GUI-based application built with Tkinter that calculates and tracks the total amount spent on Pepsi consumption. The program allows users to input the number of cans consumed per day and the cost per can, then calculates the total amount spent over time.

## Features

- Input the number of Pepsi cans consumed per day.
- Input the cost per Pepsi can in SEK.
- Calculate and display the total amount spent.
- Save and load total spending from a file (`total_spent.txt`).
- Delete saved spending data.
- Dynamic background resizing.
- Animated background using a GIF.
- Added a reset function to clear the input fields.

## Requirements

- Python 3.x

### Required Python libraries:

- `tkinter`
- `Pillow (PIL)`
- `imageio`
- `os`

## Installation

1. Clone or download the repository:
   ```sh
   git clone https://github.com/yourusername/pepsi-consumption-calculator.git
   cd pepsi-consumption-calculator
   ```
2. Install the required dependencies:
   ```sh
   pip install pillow imageio
   ```
3. Run the script:
   ```sh
   python main.py
   ```

## Usage

1. Enter the number of Pepsi cans you consume per day.
2. Enter the cost per can in SEK.
3. Click the **Calculate Total Spent** button to compute your total spending.
4. The total spent will be displayed and saved in `total_spent.txt`.
5. To reset the saved data, click the **Delete Saved Data** button.
6. Use the **Reset** button to clear input fields.

## Notes

- The animated background is loaded from `pepsimanola.gif`. Ensure the file is available in the same directory as the script.
- The `total_spent.txt` file is used to store accumulated spending and is automatically created if it does not exist.

## License

This project is for educational and personal use. No official affiliation with PepsiCo.



[malek <3]

