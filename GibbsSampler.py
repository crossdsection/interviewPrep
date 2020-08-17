import random

def RandomMotifs(Dna, k, t):
    motifs = []
    n = len(Dna[0])
    for i in range(0,t):
        initialIndex = random.randint(0, n-k)
        motifs.append(Dna[i][initialIndex:initialIndex+k])
    return motifs

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

def Consensus(Motifs):
    count = CountWithPseudocounts(Motifs)
    k = len(Motifs[0])
    consensus = ''
    for i in range(0, k):
        max = 0
        maxChar = ''
        for key in count:
            if count[key][i] > max:
                max = count[key][i]
                maxChar = key
        consensus += maxChar
    
    finalResponse = {
        'count' : count,
        'consensus': consensus
    }
    return finalResponse

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

def Score(Motifs):
    motifLen = len(Motifs[0])
    data = Consensus(Motifs)
    count = data['count']
    consensus = data['consensus']
    score = 0
    for key in count:
        for i in range(0,motifLen):
            if key != consensus[i]:
                score += count[ key ][i]
    return score


def Motifs(Profile, Dna):
    motifs = []
    t = len(Dna)
    k = len(Profile['A'])
    for i in range(t):
        motif = ProfileMostProbablePattern(Dna[i], k, Profile)
        motifs.append(motif)
    return motifs

def Pr(Text, Profile):
    prob = 1
    for i in range(0,len(Text)):
        prob *= Profile[ Text[i] ][i]
    return prob

def ProfileMostProbablePattern(text, k, profile):
    m = -1
    currentKmer = ''
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        prob = Pr(pattern, profile)
        if m < prob:
            m = prob
            currentKmer = pattern
    return currentKmer

def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs 

def callRandomMotifSearchNTimes(Dna, k, t, n):
    M = RandomizedMotifSearch(Dna, k, t)
    bestM = M
    for i in range(0,n-1):
        M = RandomizedMotifSearch(Dna, k, t)
        if Score(M) < Score(bestM):
            bestM = M
    return best

def WeightedDie(Probabilities):
    n = random.uniform(0, 1)
    for p in Probabilities:
        n -= Probabilities[p]
        if n <= 0:
            return p

def Normalize(Probabilities):
    sum = 0
    for i in Probabilities:
        sum += Probabilities[i]
    constant = 1/sum
    for i in Probabilities:
        Probabilities[i] = Probabilities[i] * constant
    return Probabilities

def Pr(Text, Profile):
    prob = 1
    for i in range(0,len(Text)):
        prob *= Profile[ Text[i] ][i]
    return prob

def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {} 
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)       
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)

def removeIndex(l, i):
    newArr = []
    for x in range(0,len(l)):
        if x != i:
            newArr.append(l[x])
    return newArr

def GibbsSampler(Dna, k, t, N):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    for i in range(0,N):
        randomIndex = random.randint(0,t-1)
        profile = ProfileWithPseudocounts(removeIndex(M, randomIndex))
        M[randomIndex] = ProfileGeneratedString(Dna[randomIndex], profile, k)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
    return BestMotifs

def callGibbsSamplerUTimes(Dna, k, t, n, u):
    M = GibbsSampler(Dna, k, t, n)
    bestM = M
    for i in range(0,u-1):
        M = GibbsSampler(Dna, k, t, n)
        if Score(M) < Score(bestM):
            bestM = M
    return bestM

# Dna = ["GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC","CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG","ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC","GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC","GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG","CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA","GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA","GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG","GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG","TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC"]

# t= len(Dna)
# k= 15
# N= 100

# BM = callGibbsSamplerUTimes(Dna, k, t, N, 20)

# print(BM)
# print(Score(BM))

print(Motifs(ProfileWithPseudocounts(["CCA","CCT","CTT","TTG"]),["AAGCCAAA","AATCCTGG","GCTACTTG","ATGTTTTG"]))

def NormalizeInt(Probabilities):
    sum = 0
    for i in range(0,len(Probabilities)):
        sum += Probabilities[i]
    constant = 1/sum
    for i in range(0,len(Probabilities)):
        Probabilities[i] = Probabilities[i] * constant
    return Probabilities

print(NormalizeInt([0.22, 0.54, 0.58, 0.36, 0.3]))

