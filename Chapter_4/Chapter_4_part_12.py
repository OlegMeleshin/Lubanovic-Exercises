'''12. Use Zip function to create 'movies' dictionary which combines following lists:
titles=['Creature of Habit', 'Crewel Fate'] and plots=['A nun turns into a monster',
'A haunted yarn shop'].'''
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
print(movies)