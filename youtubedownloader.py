import yt_dlp
import os

def download_youtube_video(video_url, save_path, cookies_path):
    """
    Downloads a YouTube video using cookies for authentication.

    Parameters:
    - video_url (str): The URL of the YouTube video to download.
    - save_path (str): The directory path where the video will be saved.
    - cookies_path (str): The path to the cookies.txt file.
    """
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),  # Save the video to the specified directory
        'cookiefile': cookies_path  # Use the cookies file for authentication
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
        print(f"Video downloaded successfully and saved to {save_path}")

def main():
    # Prompt the user to input the video URL
    video_url = input("Enter the YouTube video URL: ")

    # Prompt the user to input the save path
    save_path = input("Enter the directory path where the video should be saved: ")

    # Ensure the save path exists
    if not os.path.exists(save_path):
        print("The specified save path does not exist. Please check the path and try again.")
        return

    # Prompt the user to input the path to the cookies.txt file
    cookies_path = input("Enter the path to your cookies.txt file: ")

    # Ensure the cookies.txt file exists
    if not os.path.isfile(cookies_path):
        print("The specified cookies.txt file does not exist. Please check the path and try again.")
        return

    # Download the video
    download_youtube_video(video_url, save_path, cookies_path)

if __name__ == "__main__":
    main()
