# Personal Information Manager

## Project Description
This is my first Python project! It's a program that stores and displays personal information. It demonstrates variables, user input handling, and string formatting.

## Features
* Stores static information (name, age, city, hobby)
* Gets dynamic information from user (favorite food, color)
* Displays all information in a formatted way
* Basic input validation (checks for empty input)
* Age calculation in months

## What I Learned
* **Variables:** How to store different types of data (Strings, Integers).
* **Input/Output:** Getting user input via `input()` and displaying results via `print()`.
* **String Formatting:** Using f-strings to create nice, readable output.
* **Error Handling:** Basic validation to ensure the user actually types something.

## Challenges & Solutions
|         Challenge            |                      Solution                                  |
|------------------------------|----------------------------------------------------------------|
| User might enter empty input | Added a `while` loop to check if input is empty and ask again. |
| Formatting the output nicely | Used f-strings with separators (`=` and `-`) for a clean look. |

## How to Run This Program
1.  Make sure you have Python installed.
2.  Open your terminal or command prompt.
3.  Navigate to the project folder: `week1-personal-info`
4.  Run the command: 
    ```bash
    python personal_info.py
    ```
5.  Follow the prompts to enter your information.

## Sample Output
```text
Please enter your favorite food: Pizza
Please enter your favorite color: Red

===================================
     PERSONAL INFORMATION
===================================
Name: Vidhi Kathiriya 
Age: 20 (240 months old)
City: New York
Hobby: Reading Novels

Favorite Food: Pizza
Favorite Color: Red
===================================
Thank you for using the program!







