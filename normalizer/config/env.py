"""Programm settings variables
"""

#### RUN TYPE ####

####DIRECTORIES 

INPUT_DIR  = r'C:\02_dev\AddressNormalizer\data\input'
OUTPUT_DIR  = r'C:\02_dev\AddressNormalizer\data\output'



#### INPUT FILE
INPUT_FILE_NAME = 'adr.csv'
INPUT_FILE_DELIMITER = ';'
INPUT_FILE_QUOTECHAR = None
INPUT_FILE_TARGET_COLUMN = 'Adresses'


#### OUTPUT FILE
OUTPUT_FILE='output_adr.csv'


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

#### DETERMINERS

DETERMINERS = [
    'de', 'du', 'la', 'l', 'des', 'd'
]


WRONG_NAMES = [
    {
        'wrong': ('allée des gros buisson'),
        'good': 'allée des gros buissons'
    },
    {
        'wrong': ('allée des primeveres'),
        'good': 'allée des primevères'
    },
    {
        'wrong': ('allée edgard fournier'),
        'good': 'allée edgar fournier'
    },
    {
        'wrong': ('rue de la fouilleuse'),
        'good': 'avenue de fouilleuse'
    },
    {
        'wrong': ('avenue maréchal juin'),
        'good': 'avenue du maréchal juin'
    },
    {
        'wrong': ('avenue justin godard'),
        'good': 'avenue justin godart'
    },
    {
        'wrong': ('avenue jean jaures'),
        'good': 'avenue jean jaurès'
    },
    {
        'wrong': ('rue des landes'),
        'good': 'avenue des landes'
    },
    {
        'wrong': (
            'boulevard du maréchal de lattre de tassigny',
            'boulevard de lattre de tassigny',
            'avenue du maréchal de lattre de tassigny'
        ),
        'good': 'boulevard maréchal de lattre de tassigny'
    },
    {
        'wrong': ('passage du panorama'),
        'good': 'pas du panorama'
    },
    {
        'wrong': ('place stalingrad'),
        'good': 'place de stalingrad'
    },
    {
        'wrong': ('rue darracq'),
        'good': 'rue alexandre darracq'
    },
    {
        'wrong': ('rue des bassins de richemont'),
        'good': 'rue desbassayns de richemont'
    },
    {
        'wrong': ('boulevard de la république'),
        'good': 'rue de la république'
    },
    {
        'wrong': ('rue locarno'),
        'good': 'rue de locarno'
    },
    {
        'wrong': ('avenue des bas rogers'),
        'good': 'rue des bas rogers'
    },
    {
        'wrong': ('rue émilien colin'),
        'good': 'rue emilien colin'
    },
    {
        'wrong': ('rue étienne dolet'),
        'good': 'rue etienne dolet'
    },
    {
        'wrong': ('rue d\'estiennes d\'orves'),
        'good': 'rue honoré d\'estienne d\'orves'
    },
    {
        'wrong': ('rue du pas saint maurice'),
        'good': 'rue du pas saint-maurice'
    },
    {
        'wrong': ('rue louis rené nougier'),
        'good': 'rue du professeur louis-rené nougier'
    },
    {
        'wrong': ('rue kellog','rue kelog'),
        'good': 'rue kellogg'
    },
    {
        'wrong': ('rue maurice payret-dortail'),
        'good': 'rue maurice payret dortail'
    },
    {
        'wrong': ('rue salomon de rotchild'),
        'good': 'rue salomon de rothschild'
    },  
]

