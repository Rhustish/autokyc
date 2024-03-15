import boto3
import requests

def compare_faces_from_urls(url1, url2):
    session = boto3.Session()
    client = boto3.client('rekognition')

    # Download image data from URLs
    img1_response = requests.get(url1)
    img1_bytes = img1_response.content

    img2_response = requests.get(url2)
    img2_bytes = img2_response.content

    response = client.compare_faces(
        SourceImage={'Bytes': img1_bytes},
        TargetImage={'Bytes': img2_bytes}
    )

    for face_match in response['FaceMatches']:
        position = face_match['Face']['BoundingBox']
        similarity = face_match['Similarity']
        if similarity > 90:  # You can adjust this value based on your requirement
            return True

    return False
