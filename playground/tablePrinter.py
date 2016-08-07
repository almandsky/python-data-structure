def printTable(inputdata):
    colWidths = [0] * len(inputdata)
    for i in range(len(inputdata)):
        max_width = 0;
        for j in range(len(inputdata[i])):
            if len(inputdata[i][j]) > max_width:
                max_width = len(inputdata[i][j])
            # print(inputdata[i][j] + ' width is ' + str(max_width))
        colWidths[i] = max_width

    for j in range(len(inputdata[0])):
        for i in range(len(inputdata)):
            print(inputdata[i][j].rjust(colWidths[i] + 1), end="")
        print()
    
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

    