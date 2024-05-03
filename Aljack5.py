list_of_tuples = [(), ('a', 'b'), (), ('c', 'd'), ('e', 'f'), (), ('g', 'h')]


filtered_list = [tup for tup in list_of_tuples if tup]

print("List of tuples after removing empty tuples:", filtered_list)
