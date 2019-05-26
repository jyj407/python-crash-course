import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter


# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
   # Make a seperate API call for each submission.
   url = ('https://hacker-news.firebaseio.com/v0/item/' + 
       str(submission_id) + '.json')
   submission_r = requests.get(url)
   response_dict = submission_r.json()

   submission_dict = {
        'title' : response_dict['title'],
        'link' : 'http://news.ycombinataor.com/item?id=' + str(submission_id),
        'comments' : response_dict.get('descendants', 0)
        }
   submission_dicts.append(submission_dict)
   submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                                reverse = True)

   titles, plot_dicts = [], []
   for submission_dict in submission_dicts:
       titles.append(submission_dict['title'])
       plot_dict = {
           'value' : submission_dict['comments'],
           'label' : submission_dict['link'],
           }
       plot_dicts.append(plot_dict)

   # Make visualization.
   my_style = LS('#333366', base_style=LCS)
   chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
   chart.title = 'Most hotly discussed topic on Hacker News'
   chart.x_labels = titles

   chart.add('', plot_dicts)
   chart.render_to_file('hot_topic_on_hacker_news.svg')
    
    
