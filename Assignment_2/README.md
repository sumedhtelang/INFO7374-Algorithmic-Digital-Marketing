# INFO7374-Algorithmic-Digital-Marketing

Team 4: - 

1. Samarth Hadawale (NUID: - 001053811)
2. Sumedh Telang    (NUID: - 001059338)

Google Docs Link: - https://docs.google.com/document/d/10okXVTaGggcXejwCrpnts3Xzpfb7Gs1uEKDnE4oGh2s/edit#

CLaaT Link: - https://codelabs-preview.appspot.com/?file_id=10okXVTaGggcXejwCrpnts3Xzpfb7Gs1uEKDnE4oGh2s#0


Folder Information: -

Method 1: - Contains the .ipynb file of 1st method in the assignment and the csv generated using that method.

Method 2(FAISS Method): - Contains the .ipynb file of the implementaion of facebook AI similarity search method and the csv generated using the same method.

Method 3(Spotify - Approximate Nearest Neighbors Oh Yeah): - Contains both the files to run the spotify annoy method which generates the nearest neighbor json file which can be loaded into elasticsearch using bulk API.

Preprocessing: - Contains preprocessing file which is used to extract images to disk from bson.

Streamlit: - Contains all the images used in both method 1 and 2 along with csv files and py file.

finale: - Contains all the sampled images which are used for similarity searches.

How to run the similarity searches: -
Method 1: - Use the images from 'finale' folder and run the SimilaritySearchMethod1.ipynb file from 'Method 1' folder.

Method 2 - FAISS: - Use the images from 'finale' folder and run the faissmethod.ipynb file from 'Method 2 - FAISS' folder(Perfferably run on Google Colab)

Method 3 - Spotify: - First run the get_image_features_vectors.py and store the feature vector(.npz) files. After storing the features run the cluster_image_feature_vector.py which will create the similarity indexes and store in nearest_neighbors.json file. Populate the elasticsearch cluster using bulkAPI and run the flask app in 'elasticsearch folder' to display the nearest neighbor in web app. 