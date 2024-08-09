import pandas as pd
import os
import requests
import re 


def clean_content(text):
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove @mentions and #hashtags
    text = re.sub(r'@\w+|#\w+', '', text)
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    return text
    

def capitalize_first_word(text):
    if isinstance(text, str):
        return text.capitalize()
    return text   

language_mapping = {
    'en': 'English',
    'tl': 'Tagalog',
    'cy': 'Welsh',
    'und': 'Undetermined',
    'in': 'Indonesian',
    'es': 'Spanish',
    'ht': 'Haitian Creole',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'lt': 'Lithuanian',
    'nl': 'Dutch',
    'et': 'Estonian',
    'fr': 'French',
    'de': 'German',
    'ja': 'Japanese',
    'da': 'Danish',
    'sv': 'Swedish',
    'hi': 'Hindi',
    'it': 'Italian',
    'eu': 'Basque',
    'hu': 'Hungarian',
    'fi': 'Finnish',
    'is': 'Icelandic',
    'no': 'Norwegian',
    'tr': 'Turkish',
    'sl': 'Slovenian',
    'pl': 'Polish',
    'cs': 'Czech',
    'ko': 'Korean',
    'ru': 'Russian',
    'ar': 'Arabic',
    'lv': 'Latvian'
}
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
    api_url = 'https://tweets-api-j50p.onrender.com/read-csv'  # Replace with your API endpoint
    output_file = 'modified_tweets_from_api.csv'
    # Fetch data from the API
    data = fetch_data_from_api(api_url)
    print(data)
    if data:
        # Assuming data is a list of dictionaries or similar structure
        df = pd.DataFrame(data)
        print(df)
        print(f"Number of rows in the DataFrame: {len(df)}")
        # Define the new column names (if needed)
        df.drop(columns=['country','latitude', 'longitude'], inplace=True)
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
        df['Language'] = df['Language'].map(language_mapping).fillna(df['Language']) 
        df['Content'] = df['Content'].apply(clean_content)
        df['Author'] = df['Author'].apply(capitalize_first_word)

        # Get the current working directory
        cwd = os.path.dirname(os.path.abspath(__file__))
        print(cwd)

        # Construct the full output file path in the current working directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_file_path = os.path.join(cwd, output_file)

        print(output_file_path)
        # Save the modified DataFrame to a new CSV file
        df.to_csv(output_file_path, index=False)
        print(f"CSV file saved successfully: {output_file_path}")
    else:
        print("No data fetched from the API.")



