# Print books that whiches prices are over 500

books = [
   {"Title":"Angels and Demons", "Author":"Dan Brown", "Price":500},
   {"Title":"Gone Girl", "Author":"Gillian Flynn", "Price":730},
   {"Title":"The Silent Patient", "Author":"Alex Michaelidis", "Price":945},
   {"Title":"Before I Go To Sleep", "Author":"S.J Watson", "Price":400}
   ]


def func(n):
    for i in range(len(n)):
        if n[i]["Price"] > 500:
            print(f"{n[i]['Title']}"
                  
