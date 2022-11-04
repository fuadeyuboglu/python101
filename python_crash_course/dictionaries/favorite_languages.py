favorite_languages = {
    "jen":"python",
    "sarah":"c",
    "edward":"ruby",
    "phil":"python",
}

language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}.")

# Title
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Title
for name in favorite_languages.keys():  # same output as "for name in favorite_languages:"
    print(name.title())

# Title
friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")
    
# sorted() function
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    
# values() method
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
    
# to see each language chosen without repetition > set
for language in set(favorite_languages.values()):
    print(language.title())
    
# more than one favorite
favorite_languages = {
    "jen":["python","ruby"],
    "sarah":"c",
    "edward":["ruby", "go"],
    "phil":["python","haskel"],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
    
        for language in languages:
            print(f"\t{language.title()}")
            
    else:
        print(f"\n{name.title()}'s favorite language is: {language.title()}")
    
