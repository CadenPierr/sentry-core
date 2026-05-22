def gender(person):
    for names in person:
            print(names)

names = { "Male": ["Matthew", "Luke", "John", "David", "Moses"], "Female": ["Beth", "Sarah", "Rachel", "Mary", "Michelle"],
          "25+": ["Luke", "John", "Beth", "Rachel"] }

gender(names["Male"])