import json


class Poem:

    def __init__(self, j_poem_meta):
        try:
            j = json.loads(j_poem_meta)
        except TypeError as e:
            print('Poem init // handled exception: variable passed is already JSON')
            j = j_poem_meta

        self.title = j['title']['rendered']

        self.author = j['excerpt']['rendered']

        # remove all text following h6 tag which is author bio
        self.body = str(j['content']['rendered']).split('<h6')[0]

        # get post image URL
        self.image = j['jetpack_featured_media_url']

        # get link to this on website
        self.permalink = j['_links']['self'][0]['href']

    def __str__(self):
        return f"{self.title.upper()} \n{self.author} \n{self.body} \nPath to Featured Image: {self.image} \nLink to Original: {self.permalink}"
