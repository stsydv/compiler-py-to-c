def tokenize(source):
    token = source.split("\n")

    for i in token:
        if i.startswith("print(") and i.endswith(")"):
            inner = i[6:-1]  # bỏ print( và )

            if inner and inner[0] in ['"', "'"] and inner[-1] in ['"', "'"]:
                print(inner[1:-1])
