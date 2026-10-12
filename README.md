# 🛍️ Smart Product Finder — E-commerce Recommendation System

A content-based product recommendation system that matches user search queries with relevant products using TF-IDF and cosine similarity. Built with Python, scikit-learn, pandas, and Streamlit.

## Features

- Natural-language product search
- TF-IDF text feature extraction
- Cosine similarity ranking
- Product recommendations with prices and categories
- Interactive Streamlit interface
- Handles empty searches and searches with no matching products

## How It Works

1. Product names, categories, and descriptions are combined into a single text field.
2. TF-IDF converts product text into numerical feature vectors.
3. A user's search is transformed using the same vectorizer.
4. Cosine similarity measures the textual similarity between the query and each product.
5. Products with positive similarity scores are ranked and displayed.

## Tech Stack

- Python
- Pandas
- scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- Streamlit

## Project Structure

```text
e-commerce_recommendation_system/
├── app/
│   └── app.py
├── data/
│   └── products.csv
├── notebooks/
│   └── 01_data_understanding.ipynb
├── src/
│   ├── __init__.py
│   └── recommender.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

Clone the repository, then navigate to the project directory.

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the application from the project root:

```bash
python -m streamlit run app/app.py
```

## Example Searches

- I need a laptop for coding
- I want a device for fitness tracking
- I need accessories for gaming

## Limitations

- Uses a small sample product dataset.
- Recommendations depend on text overlap, not deep semantic understanding.
- Does not use customer behavior, ratings, purchase history, or collaborative filtering.
- Similarity scores are not probabilities of purchase.

## Future Improvements

- Add a larger, realistic product catalog.
- Improve semantic search using text embeddings.
- Add product images and filters.
- Evaluate recommendation quality on a test set.
- Deploy the application online.

## Author

Developed as a hands-on machine learning project to explore text processing, similarity search, and interactive ML applications.