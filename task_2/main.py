def get_cats_info(path):
    try:
        with open(path,"r", encoding="utf-8") as file:
            cats_info = []
            for line in file:
                line = line.strip()
                each_info = [el.strip() for el in line.split(',')]
                try:
                    if len(each_info) != 3:
                        print(f"Wrong format: {line}")
                        continue
                    if len(each_info[0]) < 24:
                        print(f"Wrong ID :{each_info[0]}")
                        continue
                    if each_info[1].isdigit():
                        print(f"Wrong name :{each_info[1]}")
                        continue
                    if not each_info[2].isdigit():
                        print(f"Wrong age :{each_info[2]}")
                        continue
                    cat ={
                        "id": each_info[0],
                        "name": each_info[1],
                        "age": each_info[2]
                    }
                    cats_info.append(cat)
                except Exception as e:
                    print("Unexpected error")
            
            return cats_info               
    except FileNotFoundError:
        return "File is not found :("
    
print(get_cats_info(r"C:\goit\repositories\goit-algo-hw-04\task_2\cats_info.txt"))
