# Tic Tac Toe Game

#### Video Demo:  https://youtu.be/SOEP5D4d_uo

#### Description:
Welcome to the Tic Tac Toe Game, a modern web-based implementation of the classic strategy game. This project brings the timeless game of Tic Tac Toe into the digital age with an interactive web interface, multiple difficulty levels, and intelligent AI opponents. Built using Flask for the backend and vanilla JavaScript for the frontend, this application offers a seamless gaming experience right in your browser.

The game allows players to engage in the traditional 3x3 grid Tic Tac Toe, but with added depth through varying AI difficulties. Whether you're looking for a casual play or a challenging opponent, this game adapts to your skill level. The dark-themed UI provides a sleek, modern look that's easy on the eyes, and the responsive design ensures it works well on different screen sizes.

At its core, Tic Tac Toe is a game of strategy and foresight. Players take turns marking spaces in a 3x3 grid, aiming to get three of their marks in a row, column, or diagonal. The first to achieve this wins the game. If all nine spaces are filled without a winner, it's a draw. While the rules are simple, mastering the game requires understanding patterns, blocking opponents, and creating winning opportunities.

This implementation goes beyond the basic game by incorporating different AI strategies for each difficulty level. The Easy mode uses random moves, providing a relaxed experience. Medium mode implements basic blocking and winning strategies, offering a moderate challenge. Hard mode employs the minimax algorithm, making it nearly unbeatable and providing a true test of skill.

The application also includes game statistics tracking, allowing players to monitor their performance across multiple games. This feature adds a layer of progression and motivation, as players can see their improvement over time.

## Features

### Difficulty Levels
- **Easy**: AI makes random moves, perfect for beginners or casual play
- **Medium**: AI blocks winning moves and takes winning opportunities, providing a balanced challenge
- **Hard**: AI uses the minimax algorithm for optimal play, this is expert-level difficulty

### User Interface
- Dark theme
- Design that works on desktop and mobile devices
- Form-based difficulty selection
- Game state updates

### Statistics Tracking
- Win/loss/draw counters
- Persistent statistics across game sessions (within the same browser session)

### Technical Features
- Server-side rendering with Flask templates
- Client-side game logic with JavaScript
- Session-based user management (basic)

## Technologies Used

### Backend
- **Flask**: A lightweight WSGI web application framework in Python. Flask handles routing, template rendering, and session management for this project.
- **Python**: The core programming language used for the server-side logic.

### Frontend
- **HTML5**: Provides the structure and semantic markup for the web pages.
- **CSS3**: Handles all styling, including the dark theme, grid layout, and responsive design.
- **JavaScript (ES6+)**: Manages game logic, AI algorithms, user interactions, and DOM manipulation.

### Development Tools
- **Flask-Session**: For server-side session management.
- **Google Fonts**: Specifically the "Itim" font for a playful, handwritten look.

## Usage

### Playing the Game
- You play as X, the AI plays as O
- Click on any empty square to make your move
- The AI will automatically make its move after yours
- The game ends when someone wins or when it's a draw
- Use the "Reset" button to start a new game on the same difficulty

### Understanding Difficulty Levels
- **Easy**: The AI chooses moves randomly. This is great for learning the game or playing casually.
- **Medium**: The AI will block your winning moves and take its own winning opportunities. It provides a good challenge without being overwhelming.
- **Hard**: The AI uses advanced algorithms to play optimally. It's very difficult to beat, making it suitable for experienced players looking for a real challenge.

### Viewing Statistics
- Your win/loss/draw record is displayed below the game board
- Statistics persist for the duration of your browser session
- Resetting the game doesn't clear your statistics

### Winning Conditions
- Three marks in a horizontal row
- Three marks in a vertical column
- Three marks in a diagonal (top-left to bottom-right or top-right to bottom-left)

### Draw Condition
If all nine squares are filled without either player achieving three in a row, the game is a draw.


### File Descriptions

- **app.py**: Contains the Flask application logic, including routes for the home page and different difficulty levels. It handles form submissions and renders the appropriate templates.

- **templates/layout.html**: The base template that other pages extend. It includes the HTML head, common CSS, and the overall page structure.

- **templates/index.html**: The landing page where users enter their username and select a difficulty level.

- **templates/easy.html**: The game page for easy mode, including the game board, JavaScript for random AI moves, and statistics tracking.

- **templates/medium.html**: Similar to easy.html but with improved AI that can block and win.

- **templates/hard.html**: The most advanced game page with minimax AI implementation.
