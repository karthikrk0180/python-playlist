def calculate_friendship(name1, name2):
    
    name1 = name1.lower()
    name2 = name2.lower()
    
    set1 = set(name1)
    set2 = set(name2)
    
    normal_score = set1 & set2
    intersection_score = len(normal_score) * 5
    
    vowels = set('aeiou')
    
    normal_vowels_score = normal_score & vowels
    intersection_score_vowel = len(normal_vowels_score) * 10
    
    sum_score = intersection_score + intersection_score_vowel
    
    final_sum_score = min(sum_score,100)
    
    return sum_score

def main():
    print("Friendship Calculator\n")
    
    name1 = input("Enter the name of first friend: ").strip()
    name2 = input("Enter the name of Second friend: ").strip()
    
    score = calculate_friendship(name1, name2)
    
    
    print(f"Score: {score}")
    

if __name__ == "__main__":
    main()