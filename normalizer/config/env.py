"""Programm settings variables
"""

#### RUN TYPE ####

####DIRECTORIES 

INPUT_DIR  = r'C:\02_dev\AddressNormalizer\data\input'
OUTPUT_DIR  = r'C:\02_dev\AddressNormalizer\data\output'



#### INPUT FILE
INPUT_FILE_NAME = 'test_file.csv'
INPUT_FILE_DELIMITER = ";"
INPUT_FILE_QUOTECHAR = None
INPUT_FILE_TARGET_COLUMN = 'adresse'


#### OUTPUT FILE
OUTPUT_FILE='output_test_file.csv'


#### UNWANTED CHARACTERS
UNWANTED_CHARACTERS = ',;."/\\()*'

#### REPETITION

REPETITION = ['bis', 'ter', 'quater']

#### WRONG PREFIX

WRONG_PREFIXS = [ 
    {
        'wrong': ('al','all'),
        'good': 'allée'
    },
    {
        'wrong': ('av','ave'),
        'good': 'avenue'
    },
    {
        'wrong': ('r'),
        'good': 'rue'
    },
    {
        'wrong': ('bd','boul'),
        'good': 'boulevard'
    },
    {
        'wrong': ('i','im','imp'),
        'good': 'impasse'
    },
    {
        'wrong': ('p','pro','prom'),
        'good': 'promenade'
    },
    {
        'wrong': ('q','qu'),
        'good': 'quai'
    },
    {
        'wrong': ('res'),
        'good': 'résidence'
    },
    {
        'wrong': ('sen'),
        'good': 'sente'
    },
    {
        'wrong': ('sq', 'squ', 'squa'),
        'good': 'square'
    },
    {
        'wrong': ('vil'),
        'good': 'villa'
    }
]

