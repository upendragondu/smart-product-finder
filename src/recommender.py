
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Find the project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Load the product dataset
DATA_PATH = PROJECT_ROOT / "data" / "products.csv"

df = pd.read_csv(DATA_PATH)

# Remove extra spaces from text columns
for column in ["product_name", "category", "description"]:
    df[column] = df[column].fillna("").astype(str).str.strip()

# Combine product information into one text column
df["content"] = (
    df["product_name"] + " " +
    df["category"] + " " +
    df["description"]
)

# Convert product text into TF-IDF vectors
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["content"])


def search_products(search_text, number_of_recommendations=5):
    """Return products that match a user's text search."""

    if not search_text or not search_text.strip():
        return pd.DataFrame(
            columns=[
                "product_name",
                "category",
                "price",
                "similarity_score",
            ]
        )

    # Convert the user's search into the same TF-IDF space
    search_vector = tfidf.transform([search_text.strip()])

    # Calculate similarity with all products
    scores = cosine_similarity(
        search_vector, tfidf_matrix
    ).flatten()

    # Rank products from most to least relevant
    ranked_indices = scores.argsort()[::-1]

    results = df.iloc[ranked_indices].copy()
    results["similarity_score"] = scores[ranked_indices]

    # Exclude products with zero similarity
    results = results[results["similarity_score"] > 0]

    # Return the requested number of recommendations
    return results[
        [
            "product_name",
            "category",
            "price",
            "similarity_score",
        ]
    ].head(max(0, number_of_recommendations)).reset_index(drop=True)
