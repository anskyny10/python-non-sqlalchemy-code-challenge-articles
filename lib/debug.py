#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
    
    #adding items for testing
    Magazine1 = Magazine("Magazine1", "CategoryA")
    Magazine2 = Magazine("Magazine2", "CategoryA")
    Magazine3 = Magazine("Magazine3", "CategoryB")
    Magazine4 = Magazine("Magazine4", "CategoryC")
    Magazine5 = Magazine("Magazine5", "CategoryD")

    Author1 = Author("Author1")
    Author2 = Author("Author2")
    Author3 = Author("Author3")
    Author4 = Author("Author4")
    Author5 = Author("Author5")

    Article1 = Article(Author1, Magazine1, "TitleA")
    Article2 = Article(Author2, Magazine2, "TitleB")
    Article3 = Article(Author3, Magazine3, "TitleC")
    Article4 = Article(Author4, Magazine4, "TitleD")
    Article5 = Article(Author5, Magazine5, "TitleE")
    Article6 = Article(Author5, Magazine1, "TitleF")
    Article7 = Article(Author5, Magazine2, "TitleG")
    Article8 = Article(Author3, Magazine2, "TitleH")
    Article9 = Article(Author1, Magazine5, "TitleI")
    Article10 = Article(Author1, Magazine5, "TitleJ")

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
