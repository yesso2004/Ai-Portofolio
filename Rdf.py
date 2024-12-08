from rdflib import Graph, URIRef, Literal, Namespace, RDF


graph = Graph()

# Namespace 
ex = Namespace("http://Movies.org/")

# Movies with relationship to author and genre 

MovieOne = URIRef("http://Movies.org/MovieOne")
MovieTwo = URIRef("http://Movies.org/MovieTwo")
MovieThree = URIRef("http://Movies.org/MovieThree")
MovieFour = URIRef("http://Movies.org/MovieFour")

AuthorOne = URIRef("http://Movies.org/Author/Christopher_Nolan")
AuthorTwo = URIRef("http://Movies.org/Author/Francis_Ford")
AuthorThree = URIRef("http://Movies.org/Author/Parker_Finn")
AuthorFour = URIRef("http://Movies.org/Author/Jon_Watts")

Genre_Science_Fiction = URIRef("http://Movies.org/Genre/Science_Fiction")
Genre_Crime = URIRef("http://Movies.org/Genre/Crime")
Genre_Horror = URIRef("http://Movies.org/Genre/Horror")
Genre_Action = URIRef("http://Movies.org/Genre/Action")

# Triplets for Movie One

graph.add((MovieOne,RDF.type,ex.Movie))
graph.add((MovieOne, ex.title ,Literal("Inception")))
graph.add((MovieOne,ex.hasAuthor,AuthorOne))
graph.add((MovieOne,ex.hasGenre,Genre_Science_Fiction))

# Triplets for Movie Two

graph.add((MovieTwo,RDF.type,ex.Movie))
graph.add((MovieTwo,ex.title,Literal("The godfather")))
graph.add((MovieTwo,ex.hasAuthor,AuthorTwo))
graph.add((MovieTwo,ex.hasGenre,Genre_Crime))

# Triplets for Movie Three

graph.add((MovieThree,RDF.type,ex.Movie))
graph.add((MovieThree,ex.title,Literal("Smile")))
graph.add((MovieThree,ex.hasAuthor,AuthorThree))
graph.add((MovieThree,ex.hasGenre,Genre_Horror))

# Triplets for Movie Four

graph.add((MovieFour,RDF.type,ex.Movie))
graph.add((MovieFour,ex.title,Literal("Spider-man")))
graph.add((MovieFour,ex.hasAuthor,AuthorFour))
graph.add((MovieFour,ex.hasGenre,Genre_Action))

# Triplets for Authors

graph.add((AuthorOne,RDF.type,ex.Author))
graph.add((AuthorOne,ex.name,Literal("Christopher Nolan")))

graph.add((AuthorTwo,RDF.type,ex.Author))
graph.add((AuthorTwo,ex.name,Literal("Francis Ford")))

graph.add((AuthorThree,RDF.type,ex.Author))
graph.add((AuthorThree,ex.name,Literal("Parker Finn")))

graph.add((AuthorFour,RDF.type,ex.Author))
graph.add((AuthorFour,ex.name,Literal("Jon Watts")))

# Triplets for Genre

graph.add((Genre_Science_Fiction,RDF.type,ex.Genre))
graph.add((Genre_Science_Fiction,ex.name,Literal("Science Fiction")))

graph.add((Genre_Crime,RDF.type,ex.Genre))
graph.add((Genre_Crime,ex.name,Literal("Crime")))

graph.add((Genre_Horror,RDF.type,ex.Genre))
graph.add((Genre_Horror,ex.name,Literal("Horror")))

graph.add((Genre_Action,RDF.type,ex.Genre))
graph.add((Genre_Action,ex.name,Literal("Action")))

# Printing graph in turtle format
print(graph.serialize(format="turtle"))

# Creating query

query = """PREFIX ns1: <http://Movies.org/>

SELECT ?MovieTitle ?AuthorName ?GenreName
WHERE {
    ?Movie ns1:title ?MovieTitle .
    ?Movie ns1:hasAuthor ?Author .
    ?Author ns1:name ?AuthorName .
    ?Movie ns1:hasGenre ?Genre .
    ?Genre ns1:name ?GenreName .
}
 """
for row in graph.query(query):
    print(f"Movie: {row.MovieTitle}, Author: {row.AuthorName}, Genre: {row.GenreName}")
