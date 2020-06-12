def freq_dict(ages):#create the function header
    freq = {}#empty dictionary
    for elem in ages:
        if elem in freq:#checks frequency and adds one to already existing element
            freq[elem] += 1
        else:
            freq[elem] = 1
    return freq
