# Kdrama_Recommendation_System

The KDrama Recommendation system is a Content-Based Filtering Korean Drama Recommender. This is built using Python programming language and open source app framework Streamlit. In Content Based Recommender System, the system uses your features and likes in order to recommend you with things that you might like. It uses the information provided by you over the internet and the ones they are able to gather and then they curate recommendations according to that.  

## Description

The project uses ***content based filtering algorithm*** where feature extraction method is use for calculating similarity between each item available. Also the project uses cosine similarity algorithm as distance metric. This computes the similarity of items by measuring the cosine of the angle between two vectors projected in a multidimensional vector space. The python code in ***app.py*** will generate a list of Kdrama recommendations when the user enters a Kdrama name.

### Cosine Similarity Algorithm

To understand this algorithm we need to first know about similarity score. It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, ***similarity score*** is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

***Cosine similarity*** is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

## Getting Started

### Dependencies

* Libraries: Streamlit, Pandas, Pickle and Requests.
* Check the requirements.txt file in PyCharm folder for the same.

### Dataset

* The details of the K-Dramas(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB [https://www.themoviedb.org/documentation/api](https://api.themoviedb.org/3/tv/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US)

### How to get the API key?

* Create an account in https://www.themoviedb.org/, click on the API link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your API sidebar once your request is approved OR Use the api key already present in the app.py file.

### Installing

* Clone or download this repository to your local machine.
* Activate the virtual environment in cmd or IDE like PyCharm.
* Install all the libraries mentioned in the requirements.txt file.
* Move the folder PyCharm to your favourite IDE and run streamlit. 

### Executing program

* Open your terminal/command prompt from your project directory and run the file app.py by executing the command 
```
streamlit run app.py
```
* Go to your browser and type the URL 
  Local URL: http://localhost:8501
  in the address bar.
* Yay!! Now you can run your program and get recommended some cool K-Dramas. ENJOY ^-^

## Contributor

Nupur Parikh
