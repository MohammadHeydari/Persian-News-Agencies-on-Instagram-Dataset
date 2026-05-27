# Persian-News-Agencies-on-Instagram-Dataset

This repository contains a dataset of scraped Instagram pages from Persian news/media accounts.  
The dataset includes profile metadata and posts information such as captions, engagement metrics, media links, and timestamps.

## Paper

Analysis of Persian News Agencies on Instagram, A Words Co-occurrence Graph-based Approach [arxiv](https://arxiv.org/abs/2402.12272) | [IJWR](https://ijwr.usc.ac.ir/article_186781.html) | [RG](https://www.researchgate.net/publication/373925598_Analysis_of_Persian_News_Agencies_on_Instagram_A_Words_Co-occurrence_Graph-based_Approach)

---

## Dataset Structure

The repository contains multiple JSON files, each representing a single Instagram account:

---

- bbcpersian.json
- fars_news.json
- khabar_fouri.json

---


Each file follows a similar structure:

---

## Data Schema

### Profile Information

Each JSON file includes basic profile metadata:

```

- `alias`: Display name of the account  
- `username`: Instagram username  
- `bio`: Account biography  
- `prof_img`: Profile image URL  
- `num_of_posts`: Total number of posts  
- `followers.count`: Number of followers  
- `following.count`: Number of accounts followed  
- `bio_url`: External link in bio  
- `isprivate`: Privacy status

```

---

### Posts Structure

Each account contains a list of posts under:

```json
"posts": []

---

Paper: Analysis of Persian News Agencies on Instagram, A Words Co-occurrence Graph-based Approach

## Citation

If you find our work useful, please cite our paper:

```bibtex
@article{heydari2024analysis,
  title={Analysis of Persian News Agencies on Instagram, A Words Co-occurrence Graph-based Approach},
  author={Heydari, Mohammad and Teimourpour, Babak},
  journal={arXiv preprint arXiv:2402.12272},
  year={2024}
}

```

Each post includes:

```
caption: Post text (Persian/English mixed content)
location: Location metadata (if available)
imgs: List of image URLs
preview_img: Thumbnail image
date: Post publication date (ISO format)
tags: Hashtags used in the post
likes.count: Number of likes
views: Number of views (if available)
url: Instagram post URL
comments.count: Number of comments
comments.list: Sample comments
mentions: Tagged users
```
Example Record:

```
{
  "username": "bbcpersian",
  "alias": "BBC NEWS فارسی",
  "followers": {
    "count": 6430797
  },
  "posts": [
    {
      "caption": "...",
      "date": "2020-01-05T19:48:02.000Z",
      "likes": {
        "count": 0
      },
      "comments": {
        "count": 33
      },
      "url": "https://www.instagram.com/p/..."
    }
  ]
}
```

Use Cases

This dataset can be used for:

- Persian text analysis (NLP)
- Social media analytics
- Fake news / media comparison studies
- Engagement prediction models
- RAG / embedding-based search systems
- Temporal trend analysis of news content

Notes
- Data is scraped and may contain missing or noisy fields.
- Some posts may have empty captions or media.
- Engagement metrics (likes/views) may not be fully available for all entries.
- URLs are provided as stored at scraping time and may become unavailable over time.

[Analysis of Persian News Agencies on Instagram, A Words Co-occurrence Graph-based Approach](https://arxiv.org/abs/2402.12272)

## Citation

If you find our work useful, please cite our paper:

```bibtex
@article{heydari2024analysis,
  title={Analysis of Persian News Agencies on Instagram, A Words Co-occurrence Graph-based Approach},
  author={Heydari, Mohammad and Teimourpour, Babak},
  journal={arXiv preprint arXiv:2402.12272},
  year={2024}
}
```
