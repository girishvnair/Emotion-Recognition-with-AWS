import boto3

BUCKET = "ue-img-id"
fileName='input.JPG'
FEATURES_BLACKLIST = ("Landmarks", "Emotions", "Pose", "Quality", "BoundingBox", "Confidence")

def detect_faces(bucket, filename, attributes=['ALL'], region_name="us-east-1"):
        rekognition = boto3.client("rekognition", region_name)
        response = rekognition.detect_faces(
            Image={
                        "S3Object": {
                                "Bucket": bucket,
                                "Name": filename,
                        }
                },
            Attributes=attributes,
        )
        return response['FaceDetails']

if __name__ == "__main__":
    for face in detect_faces(BUCKET, fileName):
        print ("Face ({Confidence}%)".format(**face))
        # emotions
    for emotion in face['Emotions']:
        print("{Type} : {Confidence}%".format(**emotion))
