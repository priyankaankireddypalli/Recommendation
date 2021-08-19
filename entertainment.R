# 2
library(readr)
library(recommenderlab)
library(reshape2)
# Importing the dataset
ent <- read.csv('C:\\Users\\WIN10\\Desktop\\LEARNING\\Entertainment.csv',header = TRUE)
ratinglist <- ent[2:4]
head(ratinglist)
dim(ratinglist)
colnames(ratinglist)
# Converting into matrix
ratingmatrix <- as.matrix(acast(ratinglist,Titles~Category,fun.aggregate = mean))
dim(ratingmatrix)
# recommendarlab realRatingMatrix format
r <- as(ratingmatrix,"realRatingMatrix")
rec1 = Recommender(r,method = 'UBCF')  # User Based Collaborative Filtering
rec2 = Recommender(r,method = 'IBCF')  # Item Based Collaborative Filtering
rec3 = Recommender(r,method = 'POPULAR')
rec4 = Recommender(binarize(r,minRating=2), method="UBCF") ## binarize all 2+ rating to 1
# Create n Recommendations for user
uid = "Balto (1995)"
movies <- subset(ratinglist,ratinglist$user == uid)
print('You have rated: ')
movies
print("recommendations for you:")
prediction <- predict(rec1, r[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec2, r[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec3, r[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec4, r[uid], n=2) ## you may change the model here
as(prediction, "list")

# From the above predictions, Action, Adventure, Comedy, Drama, Sci-Fi, Space, Mecha genre movies are suggested

