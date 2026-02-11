with open("test.txt", 'r') as rf:
    with open("test_copy.txt", 'w') as wf:
        for line in rf:    #for every line in text.txt, write it into test_copy line
            wf.write(line)








