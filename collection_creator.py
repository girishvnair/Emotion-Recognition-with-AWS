import boto3


from botocore.config import Config

def create_collection(collection_id):
    client = boto3.client('rekognition',region_name='us-east-1')

    # Create a collection
    print('Creating collection:' + collection_id)
    response = client.create_collection(CollectionId=collection_id)
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')


def main():
    collection_id = 'Collection'
    create_collection(collection_id)


if __name__ == "__main__":
    main()
