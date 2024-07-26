class News:
    def __init__(self, source, title, urlToImage, publishedAt, url):
        self.source = source
        self.title = title
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.url = url

    def to_dict(self):
        return {
            'source': self.source,
            'title': self.title,
            'urlToImage': self.urlToImage,
            'publishedAt': self.publishedAt,
            'url': self.url
        }