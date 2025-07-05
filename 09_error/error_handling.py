file  = open('youtube.txt','w')

try:
    file.write("Chai aur code")
finally:
    file.close()
    
# # best practices    
with open('youtube.txt','w') as file:
    file.write('Chai aut python')