from huggingface_hub import HfApi
import os

api = HfApi()

repo_id = "Rwitobaan/faceforensics-frames-c23"

print(f"Uploading shards to {repo_id}...")

# This will upload the 7 tar files. 
# Because they are large, HF will automatically handle them via LFS.
api.upload_folder(
    folder_path="./ff_shards",
    repo_id=repo_id,
    repo_type="dataset",
    path_in_repo="data" 
)

print("Done!")