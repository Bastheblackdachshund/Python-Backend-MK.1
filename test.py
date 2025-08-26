from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"AAARGH"}




with open('Count2.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    integers = [int(line.strip()) for line in lines]
    for index in range(0,len(integers)):
        integers[index] += 1

with open('Count2.txt', 'w') as file:
    integers = list(map(str, integers))
    result = "\n".join(integers)
    file.writelines(result)
    print(result)