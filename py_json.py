import requests
import pandas as pd

def fetch_data_from_api(api_url):
    try:
        # Send GET request to the API
        response = requests.get(api_url)
        response.raise_for_status()

        # Parse JSON response
        data = response.json()
        return data['users']  # karena respon ada di dalam key 'users'

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON decode error: {json_err}")

    return None

def save_to_excel(data, filename):
    # Ambil hanya kolom yang dibutuhkan dan susun ke dalam list
    extracted_data = []
    for user in data:
        extracted_data.append({
            'Email': user.get('email'),
            'Alamat Rumah': f"{user['address']['address']}, {user['address']['city']}, {user['address']['state']}",
            'Latitude Kantor': user.get('company', {}).get('address', {}).get('coordinates', {}).get('lat'),
            'Longitude Kantor': user.get('company', {}).get('address', {}).get('coordinates', {}).get('lng')
        })

    # Konversi ke DataFrame dan simpan sebagai Excel
    df = pd.DataFrame(extracted_data)
    df.to_excel(filename, index=False)
    print(f"Data berhasil disimpan ke {filename}")

def main():
    api_url = "https://dummyjson.com/users"
    data = fetch_data_from_api(api_url)

    if data:
        save_to_excel(data, "users_data.xlsx")

if __name__ == "__main__":
    main()
