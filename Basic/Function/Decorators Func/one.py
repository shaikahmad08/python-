def movie_star(func):
    def inner(name):
        if name==('prabhas','rc'):
            print('most collection movie in day one')
        else:
            func(name)
    return inner

@movie_star
def famous(name):
    print('not upto the mark of opening in day one')
famous('ntr')
famous('prabhas')
famous('rc')
