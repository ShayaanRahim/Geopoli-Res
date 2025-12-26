# Geopoli-Res

A news aggregation and analysis application that scrapes news articles from various sources, stores them in a database, and provides a Flask web interface for accessing the data.

## Features

- **News Scraping**: Automatically fetches news articles from Finnhub API
- **Full Text Extraction**: Extracts complete article text using the Newspaper library
- **Database Storage**: Stores articles in SQLite database with metadata
- **Web Interface**: Flask-based web application for accessing news data
- **RSS Feed Support**: RSS feed parsing functionality (in development)
- **ML Analysis**: Machine learning analysis capabilities (in development)

## Project Structure

```
Geopoli-Res/
├── mainApp.py                 # Flask web application
├── mlAnalysis.py              # Machine learning analysis module
├── NewsArticles.db            # SQLite database for storing articles
├── News Scraping/
│   ├── newsScraper_functions.py  # Core scraping functions
│   ├── rssfeed.py             # RSS feed parser
│   └── scrapingLogic.py       # Main scraping logic
└── Testing Files/
    ├── test.py                # Test files
    └── trydata.py             # Test files
```

## Prerequisites

- Python 3.x
- Finnhub API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Geopoli-Res
```

2. Install required dependencies:
```bash
pip install flask finnhub python-dotenv newspaper3k feedparser
```

3. Create a `.env` file in the root directory and add your Finnhub API key:
```
FINNHUB_KEY=your_api_key_here
```

## Usage

### Setting Up the Database

Run the scraping logic to initialize the database and populate it with articles:

```bash
python "News Scraping/scrapingLogic.py"
```

This will:
- Create the SQLite database (`NewsArticles.db`)
- Fetch news articles from Finnhub
- Extract full text from articles
- Store articles in the database

### Running the Web Application

Start the Flask application:

```bash
python mainApp.py
```

The application will be available at `http://localhost:5000/main`

## Database Schema

The `articles` table contains the following fields:
- `id`: Primary key (auto-increment)
- `article_id`: Unique article ID from Finnhub
- `category`: Article category
- `datetime`: Publication timestamp
- `headline`: Article headline
- `related`: Related topics
- `source`: News source
- `summary`: Article summary
- `full_text`: Full article text
- `url`: Article URL
- `inserted_at`: Timestamp when article was inserted

## Dependencies

- `flask`: Web framework
- `finnhub`: Finnhub API client
- `python-dotenv`: Environment variable management
- `newspaper3k`: Article extraction library
- `feedparser`: RSS feed parsing
- `sqlite3`: Database (built-in Python module)

## Configuration

The application uses environment variables for configuration. Create a `.env` file with:

```
FINNHUB_KEY=your_finnhub_api_key
```

## Development Status

- ✅ News scraping from Finnhub
- ✅ Database storage
- ✅ Full text extraction
- 🚧 Flask web interface (basic implementation)
- 🚧 RSS feed integration
- 🚧 ML analysis features

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]

