from ValidationException import ValidationException

def validate_file(file_path):
    count = 1
    compressed = ""
    decompressed = ""

    with open(file_path, "r") as file:
        lines = file.read().splitlines()


        for line in lines:
            for char in line:
                if char.isdigit():
                    count += int(char)
                else:
                    compressed += char * count
                    count = 1

            for char in compressed:
                if char.isdigit():
                    count = int(char)
                else:
                    decompressed += char * count
        return decompressed



def test():
    try:
        validate_file("../python-3-quiz/users.txt")

    except ValidationException as ve:
        print(ve)

test()
