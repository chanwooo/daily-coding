def foo(users):
    friends = []
    for user in users:
        if len(user) == 4:
            friends.append(user)

    return friends


print(foo(["Ryan", "Kieran", "Mark"]))  # => ["Ryan", "Mark"]
print(foo([]))
