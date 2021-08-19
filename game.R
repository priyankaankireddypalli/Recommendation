# 1
library(readr)
library(recommenderlab)
library(reshape2)
game <- read.csv('C:\\Users\\WIN10\\Desktop\\LEARNING\\game.csv')
head(game)
dim(game)
# Converting into matrix
ratingmatrix <- as.matrix(acast(game,userId~game,fun.aggregate = mean))
dim(ratingmatrix)
# recommendarlab realRatingMatrix format
r <- as(ratingmatrix,"realRatingMatrix")
rec1 = Recommender(r,method = 'UBCF')  # User Based Collaborative Filtering
rec2 = Recommender(r,method = 'IBCF')  # Item Based Collaborative Filtering
rec3 = Recommender(r,method = 'SVD')
rec4 = Recommender(r,method = 'POPULAR')
rec5 = Recommender(binarize(r,minRating=2), method="UBCF") ## binarize all 2+ rating to 1
# Create n Recommendations for user
uid = 10
games <- subset(game,game['userId'] == uid)
print('You have rated: ')
games

print("recommendations for you:")
prediction <- predict(rec1, r[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec2, r[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec3, r[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec4, r[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec5, r[uid], n=2) ## you may change the model here
as(prediction, "list")

# From the above predictions, 'The Orange Box' game is recommended

