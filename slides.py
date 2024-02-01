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
import json
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload


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


def download_as_pdf(service, file_id, output_file_path):
    request = service.files().export_media(fileId=file_id, mimeType="application/pdf")
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False

    print(f"Download PDF to {output_file_path}...")
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

    with open(output_file_path, "wb") as f:
        f.write(fh.getbuffer())


def find_item_id_by_path(service, path):
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
            print(f"No such file/dir named {name} in path {path}")
            return None

        # Assuming the first found file/folder is the correct one
        folder_id = files[0]["id"]

    return folder_id


def generate_current_slides_info(service, folder_path):
    """
    Retrieves all Google Slides files along with their last modified times within a specified directory on Google Drive.

    :param service: Authorized Google Drive service instance.
    :param folder_path: The path of the directory to search in, e.g., "CV Course/slides".
    :return: A list of dictionaries containing file IDs, names, and last modified times of the Google Slides files.
    """
    folder_id = find_item_id_by_path(service, folder_path)
    slides_mime_type = "application/vnd.google-apps.presentation"
    query = f"'{folder_id}' in parents and mimeType='{slides_mime_type}'"
    response = (
        service.files()
        .list(
            q=query,
            spaces="drive",
            fields="files(id, name, modifiedTime)",
            pageSize=100,  # Adjust pageSize as needed
        )
        .execute()
    )

    slides_info = response.get("files", [])
    slides_info_dict = {item["id"]: item for item in slides_info}

    return slides_info_dict


def write_slides_info_to_drive(service, folder_path, slides_files, json_filename):
    """
    Writes data about Google Slides files to a JSON file and updates or uploads it to a specified directory on Google Drive.
    """
    # Write the data to a JSON file locally
    with open(json_filename, "w") as json_file:
        json.dump(slides_files, json_file, indent=4)

    # Check if the JSON file already exists in the specified folder
    drive_json_id = find_item_id_by_path(
        service, os.path.join(folder_path, json_filename)
    )

    file_metadata = {
        "name": json_filename,
        "parents": [find_item_id_by_path(service, folder_path)],
    }
    media = MediaFileUpload(json_filename, mimetype="application/json")

    if drive_json_id is None:
        # File doesn't exist, create a new one
        file_metadata = {
            "name": json_filename,
            "parents": [find_item_id_by_path(service, folder_path)],
        }
        created_file = (
            service.files()
            .create(body=file_metadata, media_body=media, fields="id")
            .execute()
        )
        print(
            f"Uploaded {json_filename} to Google Drive with ID: {created_file.get('id')}"
        )
    else:
        # File exists, update it
        # Note: Removed 'parents' from file_metadata as it's not needed for update
        file_metadata = {
            "name": json_filename,
            # Do not include 'parents' here for the update operation
        }
        updated_file = (
            service.files()
            .update(
                fileId=drive_json_id, body=file_metadata, media_body=media, fields="id"
            )
            .execute()
        )
        print(
            f"Updated {json_filename} in Google Drive with ID: {updated_file.get('id')}"
        )

    # Clean up the local file
    os.remove(json_filename)


def read_json_from_drive(service, file_id):
    """
    Reads data from a JSON file stored on Google Drive.

    :param service: Authorized Google Drive service instance.
    :param file_id: The ID of the JSON file to read data from.
    :return: The data read from the JSON file.
    """
    # Step 1: Download the file
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()

    fh.seek(0)

    # Step 2: Read the JSON data from the file
    json_data = json.load(fh)

    return json_data


def has_file_changed(old_info, new_info):
    """
    Check if the file's modified time in the new info is more recent than in the old info.
    """
    old_modified_time = old_info.get("modifiedTime")
    new_modified_time = new_info.get("modifiedTime")
    return new_modified_time > old_modified_time


def get_old_slides_info(folder_path, json_filename, service):
    drive_json_id = find_item_id_by_path(
        service, os.path.join(folder_path, json_filename)
    )
    if drive_json_id is None:
        return {}

    slides_info_dict = read_json_from_drive(service, drive_json_id)

    # Convert json_data into a dict for easier comparison
    return slides_info_dict


def generate_changed_slides_as_pdfs(
    service, last_slides_info, slides_info, out_folder_path
):
    for slide_id, slide_data in slides_info.items():
        slides_info[slide_id]
        if (
            slide_id in last_slides_info
            and has_file_changed(last_slides_info[slide_id], slide_data)
        ) or (slide_id not in last_slides_info):
            output_filename = f"{slide_data['name']}.pdf"
            download_as_pdf(
                service, slide_id, os.path.join(out_folder_path, output_filename)
            )
            print(f"Updated slide downloaded as PDF: {output_filename}")


def connect_to_google_drive_service():
    creds = get_credentials()
    service = build("drive", "v3", credentials=creds)
    return service


if __name__ == "__main__":
    GOOGLE_DRIVE_SLIDES_FOLDER_PATH = "CV Course/slides"
    JSON_FILENAME = "last_slides_info.json"
    PDF_OUT_FOLDER_PATH = "/home/yoni/Desktop/AI_is_Math/lectures"

    service = connect_to_google_drive_service()

    last_slides_info = get_old_slides_info(
        GOOGLE_DRIVE_SLIDES_FOLDER_PATH, JSON_FILENAME, service
    )

    slides_info = generate_current_slides_info(service, GOOGLE_DRIVE_SLIDES_FOLDER_PATH)

    generate_changed_slides_as_pdfs(
        service, last_slides_info, slides_info, PDF_OUT_FOLDER_PATH
    )

    write_slides_info_to_drive(
        service, GOOGLE_DRIVE_SLIDES_FOLDER_PATH, slides_info, JSON_FILENAME
    )
