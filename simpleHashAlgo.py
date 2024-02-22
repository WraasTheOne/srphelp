import random
import string

def generate_random_string(length):

    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))



def hashing_algo(string):
    hash = 0
    for char in string:
        hash += ord(char)
    return hash % 200

if __name__ == "__main__":
    nums = []
    for i in range(100):
        nums.append(hashing_algo(generate_random_string(10)))
    print(nums)
