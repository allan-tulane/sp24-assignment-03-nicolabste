import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    if S == "":
        return len(T)
    elif T == "":
        return len(S)
    else:
        if S[0] == T[0]:
            return MED(S[1:], T[1:])
        else:
            return 1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:], T[1:]))



def fast_MED(S, T, MED={}):
    if (S, T) in MED:
        return MED[(S, T)]
    if S == "":
        return len(T)
    elif T == "":
        return len(S)
    else:
        if S[0] == T[0]:
            result = fast_MED(S[1:], T[1:], MED)
        else:
            result = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED), fast_MED(S[1:], T[1:], MED))
        MED[(S, T)] = result
        return result


def fast_align_MED(S, T, MED={}):
    if (S, T) in MED:
        return MED[(S, T)]

    if S == "":
        alignment_S = "-" * len(T)
        alignment_T = T
        return len(T), alignment_S, alignment_T

    elif T == "":
        alignment_S = S
        alignment_T = "-" * len(S)
        return len(S), alignment_S, alignment_T

    else:
        if S[0] == T[0]:
            result, alignment_S, alignment_T = fast_align_MED(S[1:], T[1:], MED)
            alignment_S = S[0] + alignment_S
            alignment_T = T[0] + alignment_T
        else:
            insert_cost, insert_alignment_S, insert_alignment_T = fast_align_MED(S, T[1:], MED)
            delete_cost, delete_alignment_S, delete_alignment_T = fast_align_MED(S[1:], T, MED)
            replace_cost, replace_alignment_S, replace_alignment_T = fast_align_MED(S[1:], T[1:], MED)

            if insert_cost <= delete_cost and insert_cost <= replace_cost:
                result = 1 + insert_cost
                alignment_S = '-' + insert_alignment_S
                alignment_T = T[0] + insert_alignment_T
            elif delete_cost <= insert_cost and delete_cost <= replace_cost:
                result = 1 + delete_cost
                alignment_S = S[0] + delete_alignment_S
                alignment_T = '-' + delete_alignment_T
            else:
                result = 1 + replace_cost
                alignment_S = S[0] + replace_alignment_S
                alignment_T = T[0] + replace_alignment_T

        MED[(S, T)] = result, alignment_S, alignment_T
        return result, alignment_S, alignment_T


