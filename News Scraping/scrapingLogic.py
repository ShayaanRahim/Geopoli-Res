import newsScraper_functions as newf

#This will be the part to set up the database
newf.setup_database("NewsArticles")

#This inserts the articles into the database
newf.articleToDB()