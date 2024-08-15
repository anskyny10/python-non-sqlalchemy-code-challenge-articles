class Article:
    # SSOT
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if(isinstance(value, str) and 5 <= len(value) <= 50 and not hasattr(self, 'title')):
            self._title = value
        else:
            raise Exception("Title must be a string between 5 and 50 characters.")
    
    # for debugging
    def __repr__(self):
        return f"<Article author={self.author} magazine={self.magazine} title={self.title} />"
        
class Author:
    def __init__(self, name):
        self.name = name

    # list of articles the author has written
    def articles(self):
        return [article for article in Article.all if article.author == self]

    # unique list of magazines the author has contributed to (written)
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
        
    # creates and returns a new article instance associated with this author
    def add_article(self, magazine, title):
        return Article(magazine=magazine, title=title, author=self)

    # unique list of magazine categories this author has contributed to, None if author has no articles
    def topic_areas(self):
        # didn't work I think because None gets uniquified --> return list(set([article.magazine.category if len(self.articles()) > 0 else None for article in self.articles()]))
        if(len(self.articles()) == 0):
            return None
        else:
            return list(set([article.magazine.category for article in self.articles()]))
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if(isinstance(value, str) and len(value) > 0 and not hasattr(self, 'name')):
            self._name = value
        else:
            raise Exception("Author's name must be a string and cannot be changed later.")
    
    # for debugging
    def __repr__(self):
        return f"<Author {self.name}>"

class Magazine:
    # to be all magazines for the class method
    all = []
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    # list of all the articles the magazine has published
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # unique list of authors who have written for this magazine
    def contributors(self):
        return list(set(article.author for article in self.articles()))

    # list of article titles of all articles written for this magazine, None if magazine has no articles
    def article_titles(self):
        if(len(self.articles()) == 0):
            return None
        else:
            return [article.title for article in self.articles()]

    # list of authors who have written more than 2 articles for this magazine, None if magazine has not authors matching that criteria
    def contributing_authors(self):
        if(len(self.articles()) > 2):
            return [article.author for article in self.articles()]
        else:
            return None
    
    # the magazine instance with the most articles, None if no articles 
    @classmethod
    def top_publisher(cls):
        # dictionary to count the articles per magazine publisher
        magazine_article_count = {}
    
        # add all the magazines and their article counts to the dictionary, ignoring any magazines without articles
        for magazine in cls.all:
            article_count = len(magazine.articles())
            if article_count > 0:
                magazine_article_count[magazine] = article_count

        # return None if no articles left in the dictionary
        if len(magazine_article_count) == 0:
            return None
        
        # find and return the magazine publisher with most articles
        top_mag = max(magazine_article_count, key=magazine_article_count.get)
        return top_mag
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if(isinstance(value, str) and 2 <= len(value) <= 16):
            self._name = value
        else:
            raise Exception("Magazine's name must be a string between 2 and 16 characters.")
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if(isinstance(value, str) and len(value) > 0):
            self._category = value
        else:
            raise Exception("Magazine's category must be a string.")
    
    # for debugging
    def __repr__(self):
        return f"<Magazine name={self.name} category={self.category}>"