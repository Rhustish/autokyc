import boto3
import requests

def download_video(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename

def analyze_video(video_file):
    client = boto3.client('rekognition')
    with open(video_file, 'rb') as video:
        response = client.get_face_liveness_session_results(
            SessionId="8bac8d44-0b0e-4883-93c8-e5e5469061d5"
        )
    return response

def main():
    url = 'https://openai.com/sora?video=mitten-astronaut'
    video_file = download_video(url, 'local_video.mp4')
    response = analyze_video(video_file)
    print(response)

main()