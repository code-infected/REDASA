import boto3
from botocore.config import Config
from pydantic import BaseModel
from typing import List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Data class to represent the S3 object
class S3Object(BaseModel):
    key: str
    size: int
    last_modified: str

# Function to list objects in a given S3 bucket
def list_bucket_objects(bucket_name: str) -> List[S3Object]:
    # Create an S3 client without AWS credentials
    s3_client = boto3.client(
        's3',
        config=Config(signature_version='s3v4'),
        aws_access_key_id=None,
        aws_secret_access_key=None
    )
    
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        objects = response.get('Contents', [])
        
        # Map response to S3Object data class
        s3_objects = [
            S3Object(key=obj['Key'], size=obj['Size'], last_modified=obj['LastModified'].isoformat())
            for obj in objects
        ]
        logger.info(f"Retrieved {len(s3_objects)} objects from bucket '{bucket_name}'")
        return s3_objects
    
    except Exception as e:
        logger.error(f"Error listing bucket {bucket_name}: {e}")
        return []

# Main function to retrieve data from multiple S3 buckets
def main():
    # List of public S3 buckets
    buckets = [
        "pansurg-curation-raw-open-data",
        "pansurg-curation-workflo-kendraqueryresults50d0eb-open-data",
        "pansurg-curation-final-curations-open-data"
    ]
    
    # Dictionary to hold data from all buckets
    all_bucket_data = {}
    
    for bucket in buckets:
        logger.info(f"Processing bucket: {bucket}")
        objects = list_bucket_objects(bucket)
        all_bucket_data[bucket] = objects
    
    # Display retrieved data (could be replaced with further processing)
    for bucket, objects in all_bucket_data.items():
        logger.info(f"Bucket: {bucket}")
        for obj in objects:
            logger.info(f"  - {obj.key} | Size: {obj.size} bytes | Last Modified: {obj.last_modified}")

if __name__ == "__main__":
    main()
