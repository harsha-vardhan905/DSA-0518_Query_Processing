import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.bar(languages, popularity)
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title('Programming Language Popularity')
plt.show()
