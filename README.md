# Python Quiz Game
A simple quiz game built with python
## Table of Contents


- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirments](#requirments)
- [Installation](#installation)
- [Enviorement](#enviorement)
- [Usage](#usage)
- [Example Output](#example-output)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)




## Features
- Quiz System
  - Asks the player multiple questions
  - Checks answers automatically
  - Calculates the final score
- Result storage
  - Saves quiz results in `results.txt`
- Admin Mode
  - Asks for the admin password
  - Checks if the password is correct
  - keeps the private informations outside the main python file
  - Loads the password from `.env`


## Project Structure
```text
python_quiz_game/
│   main.py
│   question.py
|   requirements.txt
│   .env.example
│   .gitignore
|   README.md
```

### File description
- `main.py` - main file used to run quiz game
- `question.py` - stores questions and answers
- `requirements.txt` - reads the python packages needed for the projects
- `env.example` - shows the envoirment variables needed by the project
- `.gitignore` - shows git which files and folders should be tracked
- `README.md` - contains the project documentation


## Requirments
Before running the project make sure you have:
- `python 3` 
- `python-dotenv`

## Installation
1. open a terminal in the project folder.
2. chech that python is installed:
```bash
python --version
```
3. install the python packages:
```bash
pip install -r requirements.txt
```
## Enviorement Setup
1. Create a `.env` file from `.env.example`:
```bash
cp .env.example .env
```
2. Open the new `.env` file
3. Replace the example value with your own password:
```txt
QUIZ_ADMIN_PASSWORD=enter_your_password_here
```
4. Save the file.
   
> Do not commit your `.env` file because it may contain your private information.

## Usage
1. open a terminal in the project folder.
2. chech that python is installed:
```bash
python main.py
```
3. Choose `yes` or `no` for admin mode.
4. If you choose `yes`, enter the password from your `.env` file.
5. Enter your name.
6. Answer the questions.
7. See your final score and message.
8. Your results are saved in `results.txt`.
## Example Output

## Roadmap
- [x] add multiple quiz questions
- [x] calculate the final score
- [x] save results to a file
- [x] add admin mode
- [ ] add more quiz questions
- [ ] add difficulty levels
- [ ] add a timer
## Contributing

## License

## Author
created by [Mojtaba Tamimi](https://github.com/mj-tamimi)