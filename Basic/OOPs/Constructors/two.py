class movie:
    def __init__(self,name,year):
        self.movie_name=name
        self.movie_year=year
        print("show any one movie in 2023:",name)

    def new_movies(self,name,year):
        self.movie_name=name
        self.movie_year=year
        print("show the upcoming movie in 2024:",name)

    def old_movies(self,name):
        print("show any old movie name:",name)

m1=movie('Salaar',2023)
print(m1.__dict__)

m1.new_movies('OG',2024)
print(m1.__dict__)

m1.old_movies('Mirchi')

