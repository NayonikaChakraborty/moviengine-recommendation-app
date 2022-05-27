# moviengine-recommendation-app
Content based Hollywood movie recommender and Collaborative filtering based anime recommender deployed on heroku

Check out the live demo: 

Link to youtube demo:

(CURRENTLY IT WORKS LOCALLY, WORKING ON DEPLOYMENT)

### Table of Contents
**[How to run the project?](#How-to-run-the-project)**<br>
**[Content based Hollywood movie recommender](#Content-based-Hollywood-movie-recommender)**<br>
**[Collaborative filtering based anime recommender](#Collaborative-filtering-based-anime-recommender)**<br>

## How to run the project?

1) Clone or download this repository to your local machine.
2) Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt
3) Open files "anime_cf based_recommender.ipynb" and "movie_recommender_system_content_based.ipynb" in Jupyter Notebook.
4) "Restart and Run all Cells" under kernel of both the files. let all the pkl files be uploaded again in your system.
5) Open "app.py" in virtual environment in PyCharm and run "streamlit run app.py" in terminal.
6) You will be redirected to the webpage in your local server.
Hurray! That's it.

## Content based Hollywood movie recommender

The poster of the movies is fetched using an API by TMDB, https://www.themoviedb.org/documentation/api, and using the IMDB id of the movie in the API. While the title, genre, runtime, rating, etc are traced back from the original dataset itself.

I have implemented it using the TMDB 5000 Movie Dataset , that can be downloaded from Kaggle.

[-> Link to download dataset from Kaggle <-](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

* **Content-based recommenders:** suggest similar items based on a particular item. This system uses item metadata, such as genre, director, description, actors, etc. for movies, to make these recommendations on the basis of items having similar data.

After going through all the possible algorithms that could be used to implemenented for content-based recommendation, I decided to go forward with Cosine-Similarity to achieve optimum execution time to efficiency in the recommendations provided alone cause in this case the final matrix is capable of handling vectorization without making it's execution slow.

## Working of Cosine-Similarity:

Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

(https://github.com/NayonikaChakraborty/moviengine-recommendation-app/blob/main/cosine-similarity.jpg?raw=true)

## Collaborative filtering based anime recommender

* **Collaborative-Filtering-based recommenders:** It uses rating information from all other users to provide predictions for a user-item interaction and, thereby, whittles down the item choices for the users, from the complete item set. There are two classes of Collaborative Filtering:

User-based, which measures the similarity between target users and other users.
Item-based, which measures the similarity between the items that target users rate or interact with and other items.

I have implemented the anime recommendation system as an User-Based recommendation engine using ratings of 320.0000 users on 16.000 animes got from the Anime Recommendation Database 2020 Dataset, that can be downloaded from Kaggle.

[-> Link to download dataset from Kaggle <-](https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020)

## Working of Pearson Correlation:

After going through all the possible algorithms that could be used to implemenented for Collaborative-Filtering-based recommendation, I decided to go forward with Pearson Correlation to achieve optimum execution time to efficiency in the recommendations provided alone cause in this case the final matrix is comprised of user ratings for each and every anime by each of the users, thus making it a huge dataset to deal with. Hence, we look for the similarity by the linearity in the graph among users to provide optimum recommendation in least possible execution time.

![alt text](https://github.com/NayonikaChakraborty/moviengine-recommendation-app/blob/main/pearson_correlation.png)




