import boto3
import sys
BUCKET = "ue-img-id"
KEY = sys.argv[1]
IMAGE_ID = KEY  # S3 key as ImageId
COLLECTION = "Collection"

# Note: you have to create the collection first!
# rekognition.create_collection(CollectionId=COLLECTION)

def index_faces(bucket, key, collection_id, image_id=None, attributes=(), region="us-east-1"):
        rekognition = boto3.client("rekognition", region)
        response = rekognition.index_faces(
                Image={
                        "S3Object": {
                                "Bucket": BUCKET,
                                "Name": key,
                        }
                },
                CollectionId=collection_id,
                ExternalImageId=image_id,
            DetectionAttributes=attributes,
        )
        return response['FaceRecords']

for record in index_faces(BUCKET, KEY, COLLECTION, IMAGE_ID):
        face = record['Face']
        # details = record['FaceDetail']
#       print "Face ({}%)".format(face['Confidence'])
#       print "  FaceId: {}".format(face['FaceId'])
#       print "  ImageId: {}".format(face['ImageId'])
        print("added")
