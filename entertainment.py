import os
import pandas as pd
# import Dataset 
entertainment = pd.read_csv("C:\\Users\\WIN10\\Desktop\\LEARNING\\Entertainment.csv", encoding = 'utf8')
entertainment.shape # shape
entertainment.columns
entertainment.Category # genre columnsfrom sklearn.feature_extraction.text import TfidfVectorizer #term frequencey- inverse document frequncy is a numerical statistic that is intended to reflect how important a word is to document in a collecion or corpus
# Creating a Tfidf Vectorizer to remove all stop words
tfidf = TfidfVectorizer(stop_words = "english")    # taking stop words from tfid vectorizer 
# replacing the NaN values in overview column with empty string
entertainment["Category"].isnull().sum() 
# Preparing the Tfidf matrix by fitting and transforming
tfidf_matrix = tfidf.fit_transform(entertainment.Category)   #Transform a count matrix to a normalized tf or tf-idf representation
tfidf_matrix.shape 
# with the above matrix we need to find the similarity score
# We use Cosine similarity matrix for finding similarity score
from sklearn.metrics.pairwise import linear_kernel
# Computing the cosine similarity on Tfidf matrix
cosine_sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
# creating a mapping of anime name to index number 
entertainment_index = pd.Series(entertainment.index, index =entertainment['Titles']).drop_duplicates()
entertainment_id = entertainment_index["Lamerica (1994)"]
entertainment_id
def get_recommendations(Name, topN):    
    # topN = 10
    # Getting the movie index using its title 
    entertainment_id = entertainment_index[Name]    
    # Getting the pair wise similarity score for all the anime's with that 
    # anime
    cosine_scores = list(enumerate(cosine_sim_matrix[ entertainment_id]))    
    # Sorting the cosine_similarity scores based on scores 
    cosine_scores = sorted(cosine_scores, key=lambda x:x[1], reverse = True)    
    # Get the scores of top N most similar movies 
    cosine_scores_N = cosine_scores[0: topN+1]    
    # Getting the movie index 
    entertainment_idx  =  [i[0] for i in cosine_scores_N]
    entertainment_scores =  [i[1] for i in cosine_scores_N]    
    # Similar movies and scores
    entertainment_similar_show = pd.DataFrame(columns=["Category", "Reviews"])
    entertainment_similar_show["Category"] = entertainment.loc[entertainment_idx, "Category"]
    entertainment_similar_show["rating"] =entertainment_scores
    entertainment_similar_show.reset_index(inplace = True)  
    # entertainment_similar_show.drop(["index"], axis=1, inplace=True)
    print (entertainment_similar_show)
    # return (entertainment_similar_show) 
# Enter your anime and number of anime's to be recommended 
recommendedfinal = get_recommendations("Lamerica (1994)", topN = 10)
entertainment_index["Lamerica (1994)"]

# From the output "Adventure, Fantasy, Historical, Mystery, Seinen, Supernatural, Slice of Life