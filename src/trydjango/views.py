from django.shortcuts import render, redirect
from src.csvapp.forms import CSVFileForm
import pandas as pd
from sklearn.cluster import KMeans

def upload_file(request): #a fct that handles uploading the csv file and process it
    if request.method == 'POST': #post=the form is submitted
        form = CSVFileForm(request.POST, request.FILES) #.post contient normal data ,.files uploaded files
        if form.is_valid():
            csv_file = form.save()
            df = pd.read_csv(csv_file.file.path)
            df.dropna(inplace=True)   # Data cleaning
            # KMeans Clustering just tessst
            kmeans = KMeans(n_clusters=3)
            df['cluster'] = kmeans.fit_predict(df)  
            # Display the dataframe as HTML (for simplicity)
            return render(request, 'result.html', {'df': df.to_html()})
    else: #get=the form is not submitted yet
        form = CSVFileForm()
    return render(request, 'upload.html', {'form': form})

