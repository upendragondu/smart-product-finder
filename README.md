# 🛍️ Smart Product Finder — Content-Based Recommendation System

A machine learning-powered product discovery application that recommends relevant products based on a user's search query. Built with Python, Pandas, Scikit-learn, and Streamlit.

The application uses **TF-IDF vectorization and cosine similarity** to match user queries with product names, categories, and descriptions.

## 🚀 Live Demo

- **Live Application:** [Add your Render deployment URL here]
- **GitHub Repository:** https://github.com/upendragondu/smart-product-finder

## ✨ Features

- 🔎 **Intelligent Product Search** — Find products using natural-language search queries.
- 🤖 **Content-Based Recommendations** — Match user queries against product information using machine learning.
- 📊 **Similarity Scores** — Display how closely each product matches the search query.
- 🛍️ **Product Catalog** — Search across 115 products in multiple categories.
- 🗂️ **Multiple Categories** — Electronics, Accessories, Furniture, Fashion, and Home & Kitchen.
- 💰 **Product Prices** — Display prices for recommended products.
- 🧪 **Synthetic Data Generation** — Generate additional fictional product records for experimentation.
- 🔄 **Data Merging and Validation** — Combine original and synthetic products while checking product IDs, missing values, and invalid prices.
- 🌐 **Interactive Web Interface** — Use the application through a Streamlit interface.
- ☁️ **Cloud Deployment** — Deploy the application using Render.

## 🧠 How It Works

The application follows a content-based recommendation pipeline.

1. **Data Loading:** Load product information from a CSV dataset.
2. **Data Cleaning:** Handle missing text values and standardize product information.
3. **Feature Construction:** Combine each product's name, category, and description into a single text field.
4. **TF-IDF Vectorization:** Convert product text into numerical feature vectors based on word importance.
5. **Query Processing:** Transform the user's search query into a vector using the same fitted TF-IDF vectorizer.
6. **Similarity Calculation:** Calculate cosine similarity between the query vector and product vectors.
7. **Ranking:** Sort products by similarity score and return the highest-ranked matches.
8. **Display Results:** Show recommended product names, categories, prices, and similarity scores in the Streamlit application.

### Recommendation Pipeline

```text
User Search Query
       |
       v
Text Preprocessing
       |
       v
TF-IDF Vectorization
       |
       v
Cosine Similarity
       |
       v
Rank Products by Score
       |
       v
Display Top Recommendations
```

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading, cleaning, and manipulation |
| Scikit-learn | TF-IDF vectorization and cosine similarity |
| NumPy | Numerical operations used in data processing |
| Streamlit | Interactive web application |
| Jupyter Notebook | Data exploration and experimentation |
| Git | Version control |
| GitHub | Source code hosting |
| Render | Cloud deployment |

## 📁 Project Structure

```text
smart-product-finder/
│
├── app/
│   └── app.py
│
├── data/
│   ├── products.csv
│   ├── synthetic_products.csv
│   └── products_updated.csv
│
├── notebooks/
│   └── 01_data_understanding.ipynb
│
├── src/
│   ├── __init__.py
│   ├── recommender.py
│   ├── generate_synthetic_data.py
│   └── merge_products.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

### File Descriptions

- `app/app.py` — Streamlit user interface.
- `data/products.csv` — Original product dataset containing 15 products.
- `data/synthetic_products.csv` — 100 additional fictional product records.
- `data/products_updated.csv` — Combined catalog containing 115 products.
- `notebooks/01_data_understanding.ipynb` — Data exploration and recommendation experiments.
- `src/recommender.py` — Loads the combined dataset and implements the recommendation algorithm.
- `src/generate_synthetic_data.py` — Generates synthetic product data.
- `src/merge_products.py` — Merges the original and synthetic datasets and validates the combined catalog.
- `requirements.txt` — Python package dependencies.
- `.gitignore` — Excludes virtual environments, cache files, and local environment files from version control.

## 📊 Dataset Information

The project uses a small product catalog designed for learning and experimentation.

| Property | Details |
|---|---|
| Original products | 15 |
| Synthetic products | 100 |
| Combined products | 115 |
| Product categories | 5 |
| Data format | CSV |
| Recommendation approach | Content-based filtering |
| Text representation | TF-IDF |
| Similarity metric | Cosine similarity |

### Product Categories

- Electronics
- Accessories
- Furniture
- Fashion
- Home & Kitchen

**Data note:** The 100 generated products and their prices are fictional synthetic data. They are not verified real-world product listings or market prices.

## ⚙️ Installation and Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/upendragondu/smart-product-finder.git
cd smart-product-finder
```

### 2. Create a Virtual Environment

For Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run the following command instead:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Run the Application

From the project root directory:

```powershell
python -m streamlit run app/app.py
```

Streamlit will provide a local URL, typically:

```text
http://localhost:8501
```

Open that URL in your browser.

## 🔄 Reproducing the Data Pipeline

The repository contains scripts for generating and combining the product catalog.

### Step 1: Generate Synthetic Products

```powershell
python src/generate_synthetic_data.py
```

This generates 100 fictional products and saves them to:

```text
data/synthetic_products.csv
```

### Step 2: Merge and Validate the Catalog

```powershell
python src/merge_products.py
```

This combines the original 15 products with the 100 synthetic products and saves the result to:

```text
data/products_updated.csv
```

The merge script checks product ID uniqueness, missing product names, missing prices, and negative prices.

### Step 3: Run the Recommender

The recommender reads `data/products_updated.csv` and uses that dataset to calculate recommendations.

After changing the dataset, restart the Streamlit application if it is already running.

## 🔍 Example Search Queries

Try these queries in the application:

- `I need a laptop for coding`
- `I want something for cooking`
- `I need comfortable clothes for running`
- `I need a device for photography`
- `I am looking for furniture for my home`
- `I need accessories for my computer`

The results depend on the text present in the product catalog and how well the query matches that text.

## 📈 Understanding the Algorithm

### TF-IDF

**Term Frequency–Inverse Document Frequency (TF-IDF)** represents text numerically by considering how frequently terms appear and how informative they are across the product descriptions.

The vectorizer uses English stop-word removal to reduce the influence of common words.

### Cosine Similarity

Cosine similarity measures the similarity between two vectors.

\[
\text{Cosine Similarity}(A,B)
=
\frac{A \cdot B}{\|A\|\|B\|}
\]

A higher score indicates a closer match between the query and the product's text representation.

The score is a measure of textual similarity, **not** a probability that the user will purchase the product.

## ☁️ Deployment on Render

The application can be deployed as a Streamlit web service.

### Configuration

- **Repository:** `upendragondu/smart-product-finder`
- **Branch:** `main`
- **Root Directory:** Leave blank
- **Build Command:**

```bash
pip install -r requirements.txt
```

- **Start Command:**

```bash
streamlit run app/app.py --server.port $PORT --server.address 0.0.0.0
```

After deployment, open the URL provided by Render and test several search queries.

When you push changes to the connected GitHub repository, Render can automatically redeploy the application if automatic deployment is enabled.

**Free-tier note:** Availability and behavior depend on Render's current plan. Free web services may sleep when inactive and take time to wake up.

## ⚠️ Current Limitations

- The product catalog is small and intended for experimentation.
- Synthetic products and prices are fictional.
- Recommendations depend on textual similarity rather than user behavior or purchase history.
- The system does not learn individual user preferences.
- Exact keyword overlap can influence the results.
- There is no product inventory, shopping cart, checkout, or payment integration.
- Similarity scores should not be interpreted as purchase probabilities.
- The project has not been validated for production-scale traffic or commercial recommendation performance.

## 🔮 Future Improvements

- Add category filters and minimum/maximum price filters.
- Improve ranking using category relevance and additional text-processing techniques.
- Add product images and richer product details.
- Build a product-search API using FastAPI.
- Add a database for storing and managing product information.
- Collect user feedback to improve recommendations.
- Explore collaborative filtering when genuine user-interaction data becomes available.
- Add automated tests and recommendation-quality evaluation.
- Improve deployment monitoring and error handling.

## 🎯 Learning Outcomes

Through this project, I practiced:

- Loading, cleaning, and combining datasets using Pandas.
- Generating synthetic data for experimentation.
- Applying TF-IDF to text data.
- Calculating cosine similarity with Scikit-learn.
- Building a content-based recommendation system.
- Separating application code from machine learning logic.
- Creating an interactive Streamlit application.
- Managing code and data files with Git and GitHub.
- Deploying a Python application to a cloud platform.

## 👨‍💻 Author

**Indra Gondu**

B.Tech student specializing in Artificial Intelligence and Machine Learning, interested in practical AI/ML applications and intelligent software systems.

## 📄 License

This project is intended for educational and portfolio purposes. Add a `LICENSE` file to the repository if you want to publish it under a specific open-source license.