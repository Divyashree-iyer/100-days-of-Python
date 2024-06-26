#define
class User:
    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.followers=0
        self.following=0
        
    def follow(self,user):
        self.following+=1
        user.followers+=1

user_1=User("001","divya")
user_2=User("002","shree")

user_1.follow(user_2)

print(f"{user_1.username} has {user_1.followers} followers")
print(f"{user_2.username} has {user_2.followers} followers")

print(f"{user_1.username} follows {user_1.following} people")
print(f"{user_2.username} follows {user_2.following} people")