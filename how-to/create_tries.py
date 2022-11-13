def create_tries_with_list_of_string(words: List[str])
        tries = {}
        for w in words:
            ptr = tries
            for c in w:
                if c not in ptr:
                    ptr[c] = {}
                ptr = ptr[c]
            ptr['$'] = w
        