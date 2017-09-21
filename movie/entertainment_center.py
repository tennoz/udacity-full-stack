import fresh_tomatoes
import media

slave = media.Movie("12 years a slave",
	"n the antebellum United States, Solomon Northup, a free black man from upstate New York, is abducted and sold into slavery.",
	"http://cityuponahillmedia.com/blog/wp-content/uploads/2014/01/12-years-a-slave-poster.jpg",
	"https://www.youtube.com/watch?v=z02Ie8wKKRg")
incendies = media.Movie("Incendies",
	"Twins journey to the Middle East to discover their family history, and fulfill their mother's last wishes.",
	"https://static1.squarespace.com/static/50d144f6e4b05aff8e5b9c8c/t/53b5dc66e4b07eed85d5b308/1404427368140/",
	"https://www.youtube.com/watch?v=0nycksytL1A")

whiplash = media.Movie("whiplash",
	"A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor who will stop at nothing to realize a student's potential.",
	"https://image.slidesharecdn.com/whiplashbydamienchazelleforeducationalpurposes-150121135747-conversion-gate02/95/whiplash-by-damien-chazelle-for-educational-purposes-1-638.jpg?cb=1421848956",
	"https://www.youtube.com/watch?v=7d_jQycdQGo")

vendetta = media.Movie("V for Vendetta",
	"In a future British tyranny, a shadowy freedom fighter, known only by the alias of \"V\", plots to overthrow it with the help of a young woman.",
	"https://i.pinimg.com/736x/eb/2f/34/eb2f3488745a640216ce124a3c5bc65a--stephen-rea-hugo-weaving.jpg",
	"https://www.youtube.com/watch?v=k_13fFIrhPk")

leon = media.Movie("Leon: The Professional",
	"Mathilda, a 12-year-old girl, is reluctantly taken in by Leon, a professional assassin, after her family is murdered. Leon and Mathilda form an unusual relationship, as she becomes his protegee and learns the assassin's trade.",
	"http://images4.fanpop.com/image/photos/24500000/Leon-movie-poster-leon-1994-movie-24520438-521-755.jpg",
	"https://www.youtube.com/watch?v=DcsirofJrlM")

city = media.Movie("City of God",
	"Two boys growing up in a violent neighborhood of Rio de Janeiro take different paths: one becomes a photographer, the other a drug dealer.",
	"http://media.sinematurk.com/film/7/47/e5aa4f50276f/15244_9.jpg",
	"https://www.youtube.com/watch?v=dcUOO4Itgmw")

# create a list of movies to be passd to the open_movies_page function
movies = [slave, incendies, whiplash, vendetta, leon, city]
fresh_tomatoes.open_movies_page(movies)
