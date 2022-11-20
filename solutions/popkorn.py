import sys
import math
data = int(input())

ppl_for_group = data / 4
matches_by_group = ppl_for_group * (ppl_for_group - 1)
bags_group_stage = 2 * matches_by_group
result = int(math.ceil(1 + 1 + 2 + bags_group_stage))
print(str(result))