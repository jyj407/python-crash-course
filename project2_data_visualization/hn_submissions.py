import requests
from operator import itemgetter

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
   # Make a seperate API call for each submission.
   url = ('https://hacker-news.firebaseio.com/v0/item/' + 
       str(submission_id) + '.json')
   submission_r = requests.get(url)
   print("Status code:", submission_r.status_code)
   response_dict = submission_r.json()

   submission_dict = {
        'title' : response_dict['title'],
        'link' : 'http://news.ycombinataor.com/item?id=' + str(submission_id),
        'comments' : response_dict.get('descendants', 0)
        }
   submission_dicts.append(submission_dict)
   submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                                reverse = True)

   for submission_dict in submission_dicts:
       print("\nTitle:", submission_dict['title'])
       print("\nDiscussion:", submission_dict['link'])
       print("\nComments:", submission_dict['comments'])

    
