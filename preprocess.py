import json
import re
from pathlib import Path


def clean_text(text: str) -> str:
    if not text:
        return ""

    text = re.sub(r"http\S+|www\S+", "", text)

    text = re.sub(r"#\S+", "", text)

    text = re.sub(r"[^\u0600-\u06FF\s0-9a-zA-Z]", " ", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text


def process_file(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    username = data.get("username")
    alias = data.get("alias")

    posts = data.get("posts", [])

    processed_posts = []

    for post in posts:
        caption = clean_text(post.get("caption", ""))

        if not caption:
            continue

        processed_posts.append({
            "username": username,
            "alias": alias,
            "text": caption,
            "date": post.get("date"),
            "likes": post.get("likes", {}).get("count", 0),
            "views": post.get("views", 0),
            "url": post.get("url")
        })

    return processed_posts


def load_dataset(dataset_path):
    dataset_path = Path(dataset_path)

    all_data = []

    json_files = list(dataset_path.glob("*.json"))

    if not json_files:
        raise ValueError(f"No JSON files found in: {dataset_path}")

    for file in json_files:
        print(f"Processing file: {file.name}")
        all_data.extend(process_file(file))

    return all_data


def save_output(data, output_path="clean_dataset.json"):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":

    DATASET_FOLDER = "dataset"

    dataset = load_dataset(DATASET_FOLDER)

    print("\n====================")
    print("Total cleaned posts:", len(dataset))
    print("====================\n")

    if dataset:
        print("Sample:\n", dataset[0])

    save_output(dataset, "clean_dataset.json")

    print("\n✅ Saved to clean_dataset.json")