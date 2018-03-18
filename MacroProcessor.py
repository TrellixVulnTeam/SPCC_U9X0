# Macro Processor Implementation
# The input is being read from macro-input.txt file
# Please make sure that if there is a blank space, just a single space is used to signify it.
# Make sure that all the words are separated by single spaces
# *********************************************************************************************
# Functions Here


def macro_found(current_index):
    macro_name = macro_code_tokenized_by_word[current_index + 1][0]  # Getting Name of the Macro
    global mntc
    global mdt
    global mnt
    global mdtc
    global ala
    global alac
    start = current_index
    mnt.append([mdtc, macro_name])
    mntc = mntc+1
    to_append = ''
    try:
        if macro_code_tokenized_by_word[current_index + 1][1]:
            to_append = str(macro_code_tokenized_by_line[current_index + 1])
            arguments_split = macro_code_tokenized_by_word[current_index + 1][1].split(',')
            for x in range(0, len(arguments_split)):
                ala.append([alac, arguments_split[x]])
                to_append = to_append.replace(arguments_split[x], '#'+str(alac))
                alac += 1
        mdt.append([mdtc, to_append])
        mdtc += 1
        flag = ' '
        indexval = current_index + 1
        while flag != 'MEND':
            if 'MEND' in macro_code_tokenized_by_word[indexval][0]:
                flag = 'MEND'
                indexval += 1
            else:
                loop_append = str(macro_code_tokenized_by_line[indexval + 1])
                for x in range(0, len(ala)):
                    loop_append = loop_append.replace(ala[x][1], '#'+str(ala[x][0]))
                mdt.insert(mdtc, [mdtc, loop_append])
                mdtc = mdtc + 1
                indexval = indexval + 1
        end = indexval
    except IndexError:
        pass
    return start, end

# *********************************************************************************************
# Macro Data Table
mdt = []
# Macro Data Table Counter
mdtc = 1
# Macro Name Table
mnt = []
# Macro Name Table Counter
mntc = 1
# Argument List Array
ala = []
# Argument List Array Counter
alac =1
# Macro Start
m_start = 0
# Macro End
m_end = 0
# Output of Pass 1
pass_1_list = []
# *********************************************************************************************
# Reading Input
macro_input_code = open('macro-input.txt', 'r').read()
macro_code_tokenized_by_line = macro_input_code.split('\n')  # Split by line
macro_code_tokenized_by_word = list(macro_code_tokenized_by_line)
pass_1_list = list(macro_code_tokenized_by_line)
for i in range(0,len(macro_code_tokenized_by_line)-1):
    macro_code_tokenized_by_word[i] = macro_code_tokenized_by_line[i].split(' ') # Pslit by word

for i in range(0, len(macro_code_tokenized_by_line)-1):
    if 'MACRO' in macro_code_tokenized_by_word[i][0]:
        m_start, m_end = macro_found(i)
        for x in range(m_start, m_end):
            pass_1_list.remove(macro_code_tokenized_by_line[x])
output_pass_1 = '\n'.join(pass_1_list)

print('Macro Data Table:')
print(mdt)
print('Macro Name Table:')
print(mnt)
print('Output Code of Pass1')
print(output_pass_1)
