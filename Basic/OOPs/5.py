class Movies:

    def new_movies(self,new):
        print('The new movie name is:',new)
        self.new_movie=new
    
    def upcoming_movies(self,upc):
        print('The old movie name is:',upc)
        self.upcoming_movie=upc


m=Movies()

m.new_movies('Hi Nanna')

m.upcoming_movies('OG')
