def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {
        'A' : [1] * k,
        'G' : [1] * k,
        'C' : [1] * k,
        'T' : [1] * k
    }
    for i in range(0, t):
        for j in range(0,k) :
            count[ Motifs[i][j] ][j] += 1
    return count

def ProfileWithPseudocounts(Motifs) :
    t = len(Motifs)
    k = len(Motifs[0])
    count = CountWithPseudocounts(Motifs)
    totalCounter = [0] * k
    for key in count:
        for i in range(0,k) :
            totalCounter[i] += count[key][i]
            
    profile = {
        'A' : [0] * k,
        'G' : [0] * k,
        'C' : [0] * k,
        'T' : [0] * k
    }
    for key in count:
        for i in range(0,k) :
            profile[key][i] = count[key][i] / totalCounter[i]
    return profile

Motifs = ["AACGTA","CCCGTT","CACCTT","GGATTA","TTCCGG"]

print(ProfileWithPseudocounts(Motifs))