class Movies:

    def movies(self,movie):
        print('The movie name is',movie)
        self.movie=movie
    def new_movies(self,movie):
        print('The new movie is',movie)
        self.movie=movie

m=Movies()
m.movies("OG")
print(m.__dict__)

m1=Movies()
m1.new_movies("MAD")
print(m1.__dict__)