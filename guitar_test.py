from guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922)
other_guitar = Guitar("Another Guitar", 2013)

print("{} get_age() - Expected 98. Got {}".format(guitar.name, guitar.get_age()))
print("{} get_age() - Expected 7. Got {}".format(other_guitar.name, other_guitar.get_age()))
print("{} is_vintage - Expected Ture. Got {}".format(guitar.name, guitar.is_vintage()))
print("{} is_vintage - Expected False. Got {}".format(other_guitar.name, other_guitar.is_vintage()))

