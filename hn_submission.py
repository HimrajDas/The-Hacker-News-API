from operator import itemgetter
import requests

url_1 = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r1 = requests.get(url_1)
print(f"Status code: {r1.status_code}")

# Process info about each submission.
submission_ids = r1.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url_2 = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r2 = requests.get(url_2)
    print(f"id: {submission_id}\tstatus: {r2.status_code}")
    response_dict = r2.json()

    # Build a dictionary for each article.
    submission_dict = {
        "title": response_dict["title"],
        "hn_link": f"http://news.ycombintor.com/item?id={submission_id}",
        "comments": response_dict["descendants"]
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

