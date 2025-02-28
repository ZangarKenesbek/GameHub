# GameHub

GameHub is a simple Django-based web application for browsing and reviewing games. Users can view a list of games, check their ratings, and read or add reviews.

## Features
- View a list of games with ratings
- See details of each game
- Read reviews for games
- User-friendly UI with filters

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/ZangarKenesbek/GameHub.git
cd GameHub/assignment5
```

### 2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply database migrations
```bash
python manage.py migrate
```

### 5. Run the development server
```bash
python manage.py runserver
```
Then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Project Structure
```
assignment5/
│── gamehub/
│   │── games/
│   │   │── migrations/
│   │   │── templates/games/
│   │   │── static/
│   │   │── admin.py
│   │   │── apps.py
│   │   │── models.py
│   │   │── urls.py
│   │   │── views.py
│   │   └── utils.py
│   │── gamehub/
│   │── static/
│── db.sqlite3
│── manage.py
```

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/games/` | GET | List of games |
| `/game/<id>/` | GET | Game details |

## Contributing
Feel free to fork this repository and submit pull requests. If you find any issues, please open an issue in the repository.

## License
This project is licensed under the MIT License.

