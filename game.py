# 1
import pandas as pd
# Importing the dataset
game = pd.read_csv('C:\\Users\\WIN10\\Desktop\\LEARNING\\game.csv',encoding='utf8')
game.shape
game.columns
from sklearn.feature_extraction.text import TfidfVectorizer
# Creating a TfidVectorizer to remove all stop words
tfidf = TfidfVectorizer(stop_words = 'english')
# Checking for NA values
game['game'].isna().sum()
# There are no NA values
# Preparing tfidf matrix by fitting and transforming
tfidfmatrix = tfidf.fit_transform(game.game)
tfidfmatrix.shape
# With the above matrix we will find similarity score by using cosine similarity matrix
from sklearn.metrics.pairwise import linear_kernel
cosinesimmatrix = linear_kernel(tfidfmatrix,tfidfmatrix)
# Creating a mapping of name to index
gameindex = pd.Series(game.index,index = game['userId']).drop_duplicates()
gameid = gameindex[314]
gameid
def get_recommendations(Name, topN):    
    # topN = 10
    # Getting the movie index using its title 
    gameid = gameindex[Name]
    # Getting the pair wise similarity score for all the games
    cosine_scores = list(enumerate(cosinesimmatrix[gameid]))
    # Sorting the cosine_similarity scores based on scores 
    cosine_scores = sorted(cosine_scores, key=lambda x:x[1], reverse = True)
    # Get the scores of top N most similar movies 
    cosine_scores_N = cosine_scores[0: topN+1]
    # Getting the game index 
    game_idx  =  [i[0] for i in cosine_scores_N]
    game_scores =  [i[1] for i in cosine_scores_N]
    # Similar movies and scores
    game_similar_show = pd.DataFrame(columns=["game", "rating"])
    game_similar_show["game"] = game.loc[game_idx, "game"]
    game_similar_show["rating"] = game_scores
    game_similar_show.reset_index(inplace = True)  
    # game_similar_show.drop(["index"], axis=1, inplace=True)
    print (game_similar_show)
    # return (game_similar_show)
# Enter your game and number of games to be recommended 
get_recommendations(314, topN = 10)
gameindex[314]

# From the output "Burnout 3: Takedown" game is recommended