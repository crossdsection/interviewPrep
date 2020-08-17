def Count(Motifs):
    motifLen = len(Motifs[0])
    count = {
        'A': [0] * motifLen,
        'C': [0] * motifLen,
        'G': [0] * motifLen,
        'T': [0] * motifLen
    } 
    for i in range(0,len(Motifs)):
        for j in range(0, motifLen):
            count[ Motifs[i][j] ][j] += 1
    return count

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = Count(Motifs)
    # insert your code here
    for key in profile:
        for j in range(0, k):
            profile[ key ][j] = profile[ key ][j] / t
    return profile

def Consensus(Motifs):
    count = Count(Motifs)
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
    print(currentKmer)
    return currentKmer

# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    print( Dna )
    print( BestMotifs )
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            print( Motifs )
            print( "--" )
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
            print( "***" )
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


 
GreedyMotifSearch(["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"], 4, 5)