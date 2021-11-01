import os

directory_to_search = input("enter directory to search in: ")
word_to_search = input("enter word to search: ")
paths_to_files_found = []
print()
print("---------------   Logs    ------------------") 
print()
for root, directory, files in os.walk(directory_to_search):
        for item in os.listdir(root):
            if os.path.isfile(os.path.join(root, item)):
                    filepath = os.path.join(root, item) 
                    opened_file = open(filepath, 'r')
                    try:
                        reader =opened_file.read()
                        if word_to_search in reader:
                            paths_to_files_found.append(filepath)      
                    except:
                        print(f"Reading failed for file: {item}")
                    print(f"Reading successful for {item}")
                    opened_file.close()
                    print(f"Open and closing file - {filepath} - successful")
print()        
print("---------------   Results ------------------")
print()
print("Following files have been found: ")
for file_path in paths_to_files_found:
    x=repr(file_path)
    print((x.split('\\')[-1]).split("'")[0])

