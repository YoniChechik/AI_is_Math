"""
Create or Select a Project in Google Cloud Console:

Go to the Google Cloud Console.
If you haven't already created a project, you will need to create one. Otherwise, select an existing project.

Enable the Google Drive API:
In the dashboard of your project, navigate to the "APIs & Services > Library".
Search for "Google Drive API" and select it.
Click "Enable" to enable the Google Drive API for your project.

Create Credentials:
After enabling the API, go to "APIs & Services > Credentials".
Click "Create Credentials" at the top of the page.
Choose “OAuth client ID”.

Configure the OAuth consent screen:
You'll be prompted to configure the OAuth consent screen before creating credentials. This is the screen that users will see when they authenticate with your application.
Make sure to add a test user that is your mail.

Create OAuth 2.0 Client ID:
After configuring the consent screen, you’ll be taken back to the "Create credentials" screen.
For "Application type", select "Web application" or another type relevant to your application.
Set a name for the OAuth 2.0 client.
Under "Authorized redirect URIs", add http://localhost:8080/.
Click “Create”.
Download the Credentials:

credentials.json
After creating the client ID, you'll see a confirmation screen showing your client ID and client secret.
Click the download button (it looks like a download icon) to download the JSON file containing your credentials.
Rename this file to credentials.json and place it in the directory of your Python script.

Install Required Libraries:
If you haven’t installed the required libraries for the Google API client and OAuth, you can install them via pip:

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
"""


import io
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload


def get_credentials():
    scopes = ["https://www.googleapis.com/auth/drive"]

    creds = None
    # The file token.json stores the user's access and refresh tokens.
    if os.path.exists("secrets/token.json"):
        creds = Credentials.from_authorized_user_file("secrets/token.json", scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            assert os.path.isfile(
                "secrets/credentials.json"
            ), "You need secrets/credentials.json. Download it from client secrets in: https://console.cloud.google.com/apis/credentials/oauthclient/385659825496-0123vosqnmabsha0bkdfahktrhqg5d8v.apps.googleusercontent.com?project=slides-to-pdf-412609"
            flow = InstalledAppFlow.from_client_secrets_file(
                "secrets/credentials.json", scopes
            )
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open("secrets/token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def download_as_pdf(service, file_id, output_filename):
    request = service.files().export_media(fileId=file_id, mimeType="application/pdf")
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

    with open(output_filename, "wb") as f:
        f.write(fh.getbuffer())


# Load credentials
creds = Credentials.from_authorized_user_file("secrets/token.json")
service = build("drive", "v3", credentials=creds)


def find_file_id_by_path(service, path):
    folder_id = "root"  # start from the root
    for name in path.split("/"):
        if not name:
            continue
        query = f"name='{name}' and '{folder_id}' in parents"
        response = (
            service.files()
            .list(
                q=query, spaces="drive", fields="files(id, name, mimeType)", pageSize=10
            )
            .execute()
        )

        files = response.get("files", [])

        if not files:
            raise Exception(f"No such file/dir named {name} in path {path}")

        # Assuming the first found file/folder is the correct one
        folder_id = files[0]["id"]

    return folder_id


if __name__ == "__main__":
    path = "CV Course/slides/Intro to Computer Vision"

    creds = get_credentials()
    service = build("drive", "v3", credentials=creds)

    file_id = find_file_id_by_path(service, path)
    download_as_pdf(service, file_id, "output2.pdf")
