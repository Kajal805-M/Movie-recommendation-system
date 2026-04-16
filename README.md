# 🎬 Hollywood Movie Recommendation System
## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Future Improvements](#future-improvements)

---

## 📖 About the Project

This project recommends movies similar to a user-selected title by analyzing movie metadata such as genres, keywords, cast, crew, and overview. It applies **Natural Language Processing (NLP)** techniques and **cosine similarity** to find the top 5 most similar movies.

---

## 🚀 Features

- 🎯 Recommends top 5 similar movies instantly
- 🧠 Content-based filtering approach
- 📊 Cosine similarity for accurate recommendations
- 🎥 Clean and interactive UI using Streamlit
- ⚡ Fast and efficient performance

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas & NumPy | Data manipulation and processing |
| Scikit-learn | CountVectorizer & Cosine Similarity |
| Pickle | Model serialization |
| Matplotlib & Seaborn | Data visualization (EDA) |
| Streamlit | 

---

## 📂 Dataset

This project uses the **TMDB 5000 Movies Dataset**, which includes:

- `tmdb_5000_movies.csv` — Movie metadata (genres, keywords, overview, etc.)
- `tmdb_5000_credits.csv` — Cast and crew information

> Dataset available on [Kaggle - TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

## ⚙️ How It Works

1. **Data Merging** — Movies and credits datasets are merged on the `title` column.
2. **Feature Engineering** — Selected features: `genres`, `keywords`, `cast` (top 3), `crew` (director), and `overview`.
3. **Tag Creation** — All selected features are combined into a single `tags` column per movie.
4. **Vectorization** — `CountVectorizer` converts tags into a bag-of-words matrix (top 5000 features, English stop words removed).
5. **Similarity Computation** — Cosine similarity is calculated between all movie vectors.
6. **Recommendation** — Given a movie title, the top 5 most similar movies are returned based on cosine similarity scores.
7. **Deployment** — The model and data are serialized using Pickle and served via a Streamlit app.

---

## 🗂️ Project Structure

```
Movie-recommendation-system/
│
├── kiki.py                # Main script: data preprocessing, model building & Streamlit app
├── movies_list.pkl        # Pickled movie dataframe
├── movie_list.pkl         # Pickled movie list (alternate)
└── README.md              # Project documentation
```

> **Note:** The TMDB dataset CSV files (`tmdb_5000_movies.csv`, `tmdb_5000_credits.csv`) and `similarity.pkl` are not included in the repository due to file size. Download them separately (see Dataset section).

---
## 🚀 Live Demo

👉 Click here to try the app:  
https://movie-recommendation-system-jappijxxwzrx27f9utgbnmp.streamlit.app/
---

## 🔮 Future Improvements

- 🖼️ Add movie posters using the TMDB API
- ⭐ Incorporate collaborative filtering for hybrid recommendations
- 🔍 Add a search bar with autocomplete
- 📱 Make the UI mobile-responsive

## 🏁 Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kajal805-M/Movie-recommendation-system.git
   cd Movie-recommendation-system
   ```

2. **Install dependencies**
   ```bash
   pip install pandas numpy scikit-learn streamlit matplotlib seaborn
   ```

3. **Download the dataset** from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) and place the CSV files in the appropriate folders:
   ```
   Movies/tmdb_5000_movies.csv
   Credits/tmdb_5000_credits.csv
   ```

4. **Run the preprocessing and model building script**
   ```bash
   python kiki.py
   ```
   This will generate `movies_list.pkl` and `similarity.pkl`.


---

## 👩‍💻 Author

**Kajal** — [@Kajal805-M](https://github.com/Kajal805-M)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
