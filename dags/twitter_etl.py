import pandas as pd
import os
import requests

def fetch_data_from_api(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()  # Assuming the API returns JSON data
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def modify_and_save_csv_from_api():
    api_url = 'https://newserver-s3ci.onrender.com/read-csv'  # Replace with your API endpoint
    output_file = 'modified_tweets_from_api.csv'
    # Fetch data from the API
    data = fetch_data_from_api(api_url)
    print(data)
    if data:
        # Assuming data is a list of dictionaries or similar structure
        df = pd.DataFrame(data)
        print(df)
        # Define the new column names (if needed)
        new_column_names = {
            'author': 'Author',
            'content': 'Content',
            'country': 'Country',
            'date_time': 'DateTime',
            'id': 'ID',
            'language': 'Language',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
            'number_of_likes': 'NumberOfLikes',
            'number_of_shares': 'NumberOfShares'
        }

        # Rename the columns
        df.rename(columns=new_column_names, inplace=True)

        # Get the current working directory
        cwd = os.getcwd()

        # Construct the full output file path in the current working directory
        output_file_path = os.path.join(cwd, output_file)

        # Save the modified DataFrame to a new CSV file
        df.to_csv(output_file_path, index=False)
        print(f"CSV file saved successfully: {output_file_path}")
    else:
        print("No data fetched from the API.")

# Example usage

