import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load movies data
movies = pickle.load(open('movies_list.pkl', 'rb'))

# Assuming 'tags' column already exists
# If not, tell me — I’ll fix it for you

# Convert text to vectors
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')

vectors = cv.fit_transform(movies['tags']).toarray()

# Compute similarity
similarity = cosine_similarity(vectors)

# Save similarity.pkl
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("similarity.pkl generated successfully!")