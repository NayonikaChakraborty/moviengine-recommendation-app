# Importing necessary libraries and actions
from streamlit_lottie import st_lottie
import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit_option_menu import option_menu


def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")


# Setting page layout to cover full page width
st.set_page_config(page_title="Moviengine", page_icon=":clapper:", layout="wide")


# Hidding In-Built streamlit hamburger menu button and streamlit footer content
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Creating a horizontal nav bar
selected = option_menu(
    menu_title=None,
    options=["Hollywood", "Personalised-Anime Recommendation", "About Page"],
    icons=["house", "star-fill", "person-bounding-box"],
    default_index=0,
    orientation="horizontal",
     )

# Coding the Hollywood recommendation page
if selected == "Hollywood":
    def load_lottieur(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # -----LOAD ASSETS (adding lottie animation file links)-----
    lottie_clapper = load_lottieur("https://assets8.lottiefiles.com/private_files/lf30_bb9bkg1h.json")
    lottie_mixed = load_lottieur("https://assets5.lottiefiles.com/packages/lf20_CTaizi.json")
    lottie_holly = load_lottieur("https://assets3.lottiefiles.com/packages/lf20_vwcugezu.json")
    lottie_footer = load_lottieur("https://assets2.lottiefiles.com/private_files/lf30_iojccx08.json")

    # Fetching Movie poster using API
    def fetch_poster(movie_id):
        response = requests.get(
            'https://api.themoviedb.org/3/movie/{}?api_key=2c87933a97a577c9a861145ca7caf195&language=en-US'.format(
                movie_id))
        data = response.json()
        if response.status_code != 200:
            return None
        print(data)
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

    # Declaring required variables for recommending movie
    recommended_movies_names = []
    recommended_movies_genres = []
    recommended_movies_cast = []
    recommended_movies_synopsis = []
    recommended_movies_director = []
    recommended_movies_posters = []
    recommended_movies_ratings = []
    recommended_movies_duration = []
    recommended_movies_dor = []

    # Defining recommend movie function
    def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:10]

        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies_names.append(movies.iloc[i[0]].title)
            recommended_movies_synopsis.append(movies.iloc[i[0]].overview)
            recommended_movies_director.append(movies.iloc[i[0]].crew)
            recommended_movies_cast.append(movies.iloc[i[0]].cast)
            recommended_movies_genres.append(movies.iloc[i[0]].genres)
            recommended_movies_ratings.append(movies.iloc[i[0]].vote_average)
            recommended_movies_duration.append(movies.iloc[i[0]].runtime)
            recommended_movies_dor.append(movies.iloc[i[0]].release_date)

            # fetch poster from api
            recommended_movies_posters.append(fetch_poster(movie_id))
            st.snow()
        return recommended_movies_names, recommended_movies_synopsis, recommended_movies_genres, recommended_movies_director, recommended_movies_cast, recommended_movies_posters, recommended_movies_ratings, recommended_movies_duration, recommended_movies_dor

    # Loading processed dataset
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    left_col, mid_col, right_col = st.columns([1, 2, 1])
    with left_col:
        st_lottie(lottie_holly, height=300, key="hollywood")
    with mid_col:
        # -----Header section------
        st.title(":clapper:MOVIENGINE")
        st.subheader("--->Content Based Recommendation Model:sparkles:")
        selected_movie_name = st.selectbox('Select any Hollywood movie you want to get recommendation on:',
                                           movies['title'].values)
    with right_col:
        st_lottie(lottie_clapper, height=300, key="clapper")

    # Inserting recommend button
    if st.button('Recommend'):
        recommended_movies_names, recommended_movies_synopsis, recommended_movies_genres, recommended_movies_director, recommended_movies_cast, recommended_movies_posters, recommended_movies_ratings, recommended_movies_duration, recommended_movies_dor = recommend(
            selected_movie_name)

        # Displaying details of the movie searched
        st.header("The movie you searched for is:")
        st.header(recommended_movies_names[0])

        poster_col, data_col1, data_col2 = st.columns([1, 2, 2])
        with poster_col:
            st.image(recommended_movies_posters[0])
        with data_col1:
            st.subheader(":mortar_board:Director:")
            st.write(recommended_movies_director[0])
            st.subheader(" :family:Cast:")
            st.write(recommended_movies_cast[0])
            st.subheader(":performing_arts:Genres:-")
            st.write(recommended_movies_genres[0])
            st.subheader(":hourglass:Runtime:-")
            st.write(recommended_movies_duration[0], "minutes")
        with data_col2:
            st.subheader(":star2:IMDB Ratings:-")
            st.write(recommended_movies_ratings[0], "/10")
            st.subheader(":date:Date of Release:")
            st.write(recommended_movies_dor[0], "(yyyy/mm/dd)")
            st.subheader(":black_nib:Synopsis:-")
            st.write(recommended_movies_synopsis[0] + ".........")

        # Displaying top 6 recommended movie with respective details
        st.header("Our top recommendations based on your search....")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.image(recommended_movies_posters[1])
        with col2:
            st.header(recommended_movies_names[1])
            st.subheader(":performing_arts:Genres:-")
            st.write(recommended_movies_genres[1])
            st.subheader("Date of Release:")
            st.write(recommended_movies_dor[1], "(yyyy/mm/dd)")
            st.subheader(":star2:Ratings:-")
            st.write(recommended_movies_ratings[1], "/10")
            st.subheader(":hourglass:Runtime:-")
            st.write(recommended_movies_duration[1], "mins")

        with col3:
            st.image(recommended_movies_posters[2])

        with col4:
            st.header(recommended_movies_names[2])
            st.subheader(":performing_arts:Genres:-")
            st.write(recommended_movies_genres[2])
            st.subheader("Date of Release:")
            st.write(recommended_movies_dor[2], "(yyyy/mm/dd)")
            st.subheader(":star2:Ratings:-")
            st.write(recommended_movies_ratings[2], "/10")
            st.subheader(":hourglass:Runtime:-")
            st.write(recommended_movies_duration[2], "mins")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.image(recommended_movies_posters[3])
        with col2:
            st.header(recommended_movies_names[3])
            st.subheader(":performing_arts:Genres:-")
            st.write(recommended_movies_genres[3])
            st.subheader("Date of Release:")
            st.write(recommended_movies_dor[3], "(yyyy/mm/dd)")
            st.subheader(":star2:Ratings:-")
            st.write(recommended_movies_ratings[3], "/10")
            st.subheader(":hourglass:Runtime:-")
            st.write(recommended_movies_duration[3], "mins")

        with col3:
            st.image(recommended_movies_posters[4])
        with col4:
            st.header(recommended_movies_names[4])
            st.subheader(":performing_arts:Genres:-")
            st.write(recommended_movies_genres[4])
            st.subheader("Date of Release:")
            st.write(recommended_movies_dor[4], "(yyyy/mm/dd)")
            st.subheader(":star2:Ratings:-")
            st.write(recommended_movies_ratings[4], "/10")
            st.subheader(":hourglass:Runtime:-")
            st.write(recommended_movies_duration[4], "mins")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.image(recommended_movies_posters[5])
        with col2:
            st.header(recommended_movies_names[5])
            st.subheader(":performing_arts:Genres:-")
            st.write(recommended_movies_genres[5])
            st.subheader("Date of Release:")
            st.write(recommended_movies_dor[5], "(yyyy/mm/dd)")
            st.subheader(":star2:Ratings:-")
            st.write(recommended_movies_ratings[5], "/10")
            st.subheader(":hourglass:Runtime:-")
            st.write(recommended_movies_duration[5], "mins")

        with col3:
            st.image(recommended_movies_posters[6])
        with col4:
            st.header(recommended_movies_names[6])
            st.subheader(":performing_arts:Genres:-")
            st.write(recommended_movies_genres[6])
            st.subheader("Date of Release:")
            st.write(recommended_movies_dor[6], "(yyyy/mm/dd)")
            st.subheader(":star2:Ratings:-")
            st.write(recommended_movies_ratings[6], "/10")
            st.subheader(":hourglass:Runtime:-")
            st.write(recommended_movies_duration[6], "mins")

        left_col, right_col = st.columns([1, 3])
        with left_col:
            st_lottie(lottie_footer, height=250, key="finished")

        with right_col:
            # Footer
            st.title("Hope you liked it here... :sparkles: ")
            st.header("Stay tuned for further developments :-)")

    else:
        st.write("Click Recommend to view possible recommendations..")

# Coding anime recommendation page using collaborative filtering model
if selected == "Personalised-Anime Recommendation":
    def load_lottieur(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    # -----LOAD ASSETS (adding lottie animation file links)-----
    lottie_rocket = load_lottieur("https://assets1.lottiefiles.com/private_files/lf30_g9uulobe.json")
    lottie_falling = load_lottieur("https://assets4.lottiefiles.com/packages/lf20_Bu8wPm.json")
    lottie_floating = load_lottieur("https://assets1.lottiefiles.com/packages/lf20_ZQhQzO.json")
    lottie_watch = load_lottieur("https://assets1.lottiefiles.com/packages/lf20_Ns4TLz.json")
    lottie_finished = load_lottieur("https://assets2.lottiefiles.com/private_files/lf30_iojccx08.json")

    # Loading processed dataset
    details_dict = pickle.load(open('details_dict.pkl', 'rb'))
    animes = pd.DataFrame(details_dict)
    anime_item_similarity = pickle.load(open('anime_item_similarity.pkl', 'rb'))

    # Declaring rating array to store user rating
    rating = []

    left_col, mid_col, right_col = st.columns([1, 2, 1])
    with left_col:
        st_lottie(lottie_watch, height=300, key="watch")
        st_lottie(lottie_rocket, height=300, key="rocket")

    with mid_col:
        # -----Header section------
        st.title(":clapper:Anime Recommender")
        st.subheader("--->Item- Item Collaborative Filtering Based Recommendation Model:sparkles:")
        selected_anime_rated = st.multiselect(
            'Rate the Animes you watched to get recommendations:',
            animes['Name'].values,
            )
        st.subheader("Rate the animes you have wathced out of 10")

        # finding the number of rated animes
        x = len(selected_anime_rated)
        i = 0

        # Taking user input rating of already seen anime
        while i < x:
            st.write(selected_anime_rated[i])
            rating.append(st.slider("Your ratings for "+selected_anime_rated[i], 0, 10, 5))
            i += 1

        # Defining recommend anime function
        def get_similar_anime(name, user_ratings):
            similar_score = anime_item_similarity[name] * (user_ratings - 5)
            similar_score = similar_score.sort_values(ascending=False)

            return similar_score


        with right_col:
            st_lottie(lottie_floating, height=300, key="floating")
            st_lottie(lottie_falling, height=300, key="falling")

    # Recommend anime button
    if st.button('--->Recommend Anime'):
        user_anime_input = []

        # Declaring recommended anime in descending order
        j = 0
        while j < x:
            user_anime_input.append([selected_anime_rated[j], rating[j]])
            j += 1

        similar_anime = pd.DataFrame()

        for anime, rating in user_anime_input:
            similar_anime = similar_anime.append(get_similar_anime(anime, rating), ignore_index=True)

        st.snow()
        st.text(similar_anime.sum().sort_values(ascending=False).head(20))

        left_col, right_col = st.columns([1, 3])
        with left_col:
            st_lottie(lottie_finished, height=250, key="finished_1")

        with right_col:
            # Footer
            st.title("Hope you liked it here... :sparkles: ")
            st.header("Stay tuned for further developments :-)")


if selected == "About Page":
    def load_lottieur(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    # -----LOAD ASSSETS (declaring function)-----
    lottie_project = load_lottieur("https://assets2.lottiefiles.com/packages/lf20_ygiuluqn.json")
    lottie_web = load_lottieur("https://assets2.lottiefiles.com/packages/lf20_hrkmmhjf.json")
    lottie_shine = load_lottieur("https://assets5.lottiefiles.com/packages/lf20_bt5q6j0d.json")
    lottie_magic = load_lottieur("https://assets4.lottiefiles.com/packages/lf20_029tjdgp.json")

    left_col, mid_col, right_col = st.columns([1, 2, 1])
    with left_col:
        st_lottie(lottie_project, key="project")
    with mid_col:
        st.title("Welcome to Moviengine ")
        st.title("<--Recommendation Engine Model-->")
    with right_col:
        st_lottie(lottie_web, height=250, key="web")

    st.header("1.Content Based:-")


st.write("Made with enthusiasm by Nayonika")
