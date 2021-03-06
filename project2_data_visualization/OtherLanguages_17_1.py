import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

def getlanguageRepoStats(language):
    # Make an API call and store the response.
    url = 'https://api.github.com/search/repositories?q=language:' + language + '&sort=stars'
    r = requests.get(url)
    print("status code:", r.status_code)
    
    # Store API response in a variable
    response_dict = r.json()
    
    print(response_dict.keys())
    print("Total repositories:", response_dict['total_count'])
    
    # Explore information about the repositories.
    repo_dicts = response_dict['items']
    print("Repositories returned:", len(repo_dicts))
    
    # Examine every repository.
    names, plot_dicts = [], []
    count = 0
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        plot_dict = {
            'value' : repo_dict['stargazers_count'],
            'label' : repo_dict['description'],
            'xlink' : repo_dict['html_url']
        }
        plot_dicts.append(plot_dict)
    
        # Only get the 10 items
        if (count > 10):
            break
        count += 1
    
    # Make visualization.
    my_style = LS('#333366', base_style=LCS)
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = 15
    my_config.width = 1000 
    
    
    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-Starred ' + language + ' Projects on GitHub'
    chart.x_labels = names
    
    chart.add('', plot_dicts)
    chart.render_to_file(language + '_repos.svg')

for language in {'python', 'c++', 'c', 'Ruby', 'Java', 'Go'}:
    getlanguageRepoStats(language)
