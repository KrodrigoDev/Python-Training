import numpy as np
from collections import Counter

# primeira parte pág 4

users = []

for i in range(0, 10):
    users.append({'id': i, 'name': f'user-{i}'})

friendship_pairs = []

for i in range(0, 10):
    friendship_pairs.append(tuple(np.random.choice(9, 2, replace=False)))

# segunda parte pág 5

friendship = {user['id']: [] for user in users}

for i, j in friendship_pairs:
    friendship[i].append(j)
    friendship[j].append(i)


def number_of_friend(user):
    user_id = user['id']
    friend_ids = friendship[user_id]
    return len(friend_ids)


total_connections = sum(number_of_friend(user) for user in users)
num_users = len(users)

avg_connections = total_connections / num_users

num_friend_by_id = [(user['id'], number_of_friend(user)) for user in users]

num_friend_by_id.sort(key=lambda id_and_friend: id_and_friend[1], reverse=True)


# terceira parte pág 6
def foaf_ids_bads(user):
    user_id = user['id']
    return Counter(
        foaf_id
        for friend_id in friendship[user['id']]  # Para cada amigo meu
        for foaf_id in friendship[friend_id]  # Encontre os amigos deles
        if foaf_id != user_id  # que não sejam meus amigos
        and foaf_id not in friendship[user_id]  # e não sejam eu
    )

print(friendship)
a = foaf_ids_bads(users[0]) # vai devolver os id e a qtd de amigos em comum
print(a)

