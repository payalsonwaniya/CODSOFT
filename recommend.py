# CodSoft AI Internship – Task 4
# Content-Based Movie Recommendation System
# Created by Payal Sonwaniya

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("movies.csv")

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(data['genre'])

similarity = cosine_similarity(tfidf_matrix)

def recommend_movie(title):
    if title not in data['title'].values:
        return ["❌ Movie not found in database."]
    
    idx = data[data['title'] == title].index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]

    recommendations = [data['title'][i[0]] for i in sim_scores]
    return recommendations

movie_name = input("🎬 Enter a movie name: ")
suggestions = recommend_movie(movie_name)

print("\n🎯 Recommended Movies:")
for m in suggestions:
    print("- " + m)
