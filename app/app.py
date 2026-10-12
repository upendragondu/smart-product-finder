
import streamlit as st

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.recommender import search_products


st.set_page_config(
    page_title="Smart Product Finder",
    page_icon="🛍️",
    layout="wide",
)

st.title("🛍️ Smart Product Finder")
st.write(
    "Describe what you need, and discover relevant products."
)

search_text = st.text_input(
    "What are you looking for?",
    placeholder="Example: I need a laptop for coding",
)

number_of_recommendations = st.slider(
    "Number of recommendations",
    min_value=1,
    max_value=10,
    value=5,
)

if st.button("Find Products"):
    if not search_text.strip():
        st.warning("Please enter what you are looking for.")
    else:
        results = search_products(
            search_text,
            number_of_recommendations,
        )

        if results.empty:
            st.info(
                "No matching products found. "
                "Try using different words."
            )
        else:
            
           st.subheader("Recommended Products")

           st.caption(f"Found {len(results)} matching products.")

           for _, product in results.iterrows():
             with st.container(border=True):
                 col1, col2 = st.columns([3, 1])

             with col1:
                     st.markdown(f"### {product['product_name']}")
                     st.write(f"Category: {product['category']}")
                     st.caption(
                     f"Text similarity: "
                        f"{product['similarity_score']:.3f}"
            )

             with col2:
                  st.metric(
                   "Price",
                    f"₹{product['price']:,.0f}"
            )
