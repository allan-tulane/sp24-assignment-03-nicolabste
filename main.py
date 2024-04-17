import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, memo={}):
  # Check for already computed result
  if (S, T) in memo:
      return memo[(S, T)]

  # Base cases when either string is empty
  if not S:
      return len(T)
  if not T:
      return len(S)

  # Recursive cases: matching characters or handling edits
  if S[0] == T[0]:
      result = fast_MED(S[1:], T[1:], memo)
  else:
      result = 1 + min(
          fast_MED(S, T[1:], memo),  # Insertion
          fast_MED(S[1:], T, memo),  # Deletion
          fast_MED(S[1:], T[1:], memo)  # Substitution
      )

  memo[(S, T)] = result
  return result

def fast_align_MED(S, T, memo={}):
  # Check for already computed result
  if (S, T) in memo:
      return memo[(S, T)]

  # Handling base cases when one string is empty
  if not S:
      alignment_S = "-" * len(T)
      alignment_T = T
      return len(T), alignment_S, alignment_T
  if not T:
      alignment_S = S
      alignment_T = "-" * len(S)
      return len(S), alignment_S, alignment_T

  # Handling recursive cases
  insert_cost, insert_alignment_S, insert_alignment_T = fast_align_MED(S, T[1:], memo)
  delete_cost, delete_alignment_S, delete_alignment_T = fast_align_MED(S[1:], T, memo)
  replace_cost, replace_alignment_S, replace_alignment_T = fast_align_MED(S[1:], T[1:], memo)

  # Determining minimum cost edit
  if S[0] == T[0]:
      direct_match_cost, direct_alignment_S, direct_alignment_T = fast_align_MED(S[1:], T[1:], memo)
      direct_cost = direct_match_cost
      if direct_cost <= min(insert_cost, delete_cost, replace_cost):
          alignment_S = S[0] + direct_alignment_S
          alignment_T = T[0] + direct_alignment_T
          result = direct_cost
      else:
          result, alignment_S, alignment_T = determine_minimum(
              insert_cost, insert_alignment_S, insert_alignment_T,
              delete_cost, delete_alignment_S, delete_alignment_T,
              replace_cost, replace_alignment_S, replace_alignment_T,
              S[0], T[0]
          )
  else:
      result, alignment_S, alignment_T = determine_minimum(
          insert_cost, insert_alignment_S, insert_alignment_T,
          delete_cost, delete_alignment_S, delete_alignment_T,
          replace_cost, replace_alignment_S, replace_alignment_T,
          S[0], T[0]
      )

  memo[(S, T)] = result, alignment_S, alignment_T
  return result, alignment_S, alignment_T

def determine_minimum(insert_cost, insert_alignment_S, insert_alignment_T,
                    delete_cost, delete_alignment_S, delete_alignment_T,
                    replace_cost, replace_alignment_S, replace_alignment_T,
                    char_S, char_T):
  if insert_cost <= delete_cost and insert_cost <= replace_cost:
      return 1 + insert_cost, '-' + insert_alignment_S, char_T + insert_alignment_T
  elif delete_cost <= replace_cost:
      return 1 + delete_cost, char_S + delete_alignment_S, '-' + delete_alignment_T
  else:
      return 1 + replace_cost, char_S + replace_alignment_S, char_T + replace_alignment_T
