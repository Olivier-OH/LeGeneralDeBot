from collections import OrderedDict
import itertools
import json
import sys

list_names = ['verbs1','verbs2','verbs3', 'verbs4']
permutations = itertools.permutations(list_names)

template = '''Paris! Paris #{}#! Paris #{}#! Paris #{}#! Mais Paris #{}#!'''
grammar_origin = [template.format(*perm) for perm in permutations]

grammar = OrderedDict()
grammar['origin'] = grammar_origin

with open('./Verbes-Francais-Conjugues/verbes_lowercase.json', encoding='UTF8') as jsonfile:
    all_verbs = json.load(jsonfile)

first_group_verbs = [v for v in all_verbs if 'infinitif' in v and v['infinitif']['présent'][0].endswith('er') and not v['infinitif']['présent'][0] == 'aller']

print('There are {} first group verbs'.format(len(first_group_verbs)))

# write_verbs = None
# while write_verbs not in ('y','n'):
#     if write_verbs is not None: print('I could not understand.')
#     write_verbs = input('Would you like to write the verbs into a file? (y/n)').strip()
#     if write_verbs == 'y':
#         with open('first_group.txt', 'w', encoding='utf8') as outfile:
#             outfile.write('\n'.join(v['infinitif']['présent'][0] for v in first_group_verbs))
#         print('Exiting.')
#         sys.exit(0)
#     elif write_verbs == 'n':
#         break
    
verbs_length = len(first_group_verbs)
chunk_size = verbs_length // 4
remainder = verbs_length - chunk_size * 4

print('Remainding {} verb in last chunk.'.format(remainder))

lists = first_group_verbs[0:chunk_size], first_group_verbs[chunk_size:chunk_size*2], first_group_verbs[chunk_size*2:chunk_size*3], first_group_verbs[chunk_size*3:]

for n,l in enumerate(lists, 1):
    grammar['verbs{}'.format(n)] = [v['infinitif']['passé'][0] for v in l]

with open('grammar.json', 'w', encoding='utf8') as grammar_file:
    json.dump(grammar, grammar_file, indent=1, ensure_ascii=False)

