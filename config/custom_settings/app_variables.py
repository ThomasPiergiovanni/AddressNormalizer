"""App globals variables
"""

#### INPUT DIR ####

# Work laptop
#INPUT_DIR  = r'C:\02_dev\AddressNormalizer\config\data\input'

# Home laptop
INPUT_DIR  = r'D:\03_suresnes\AddressNormalizer\config\data\input'

#### INPUT FILE
# Input file name
INPUT_FILE = 'bp_ok.csv'

#### REFERENCE_FILE
REF_FILE = 'adresse.csv'

#### TEST ####

# Test INPUT DIR in work laptop
# TEST_INPUT_DIR = r'C:\02_dev\AddressNormalizer\config\data\test_data'

# Test INPUT DIR in home laptop
TEST_INPUT_DIR = r'D:\03_suresnes\AddressNormalizer\config\data\test_data'

TEST_INPUT_FILE = 'bp_ok.csv'
TEST_REF_FILE = 'adresse.csv'


ZIP_CODE_LIST = [
    '92500',
    '92 500',
    '92150',
    '92 150'
]

CITY_NAME_LIST = [
    'suresnes',
    'paris',
    'rueil-malamaison'
]

ALLEE_WORDS = {
    'correct_name': "allee",
    'incomformities': ["ALL", "All", "all"]
}

AVENUE_WORDS = {
    'correct_name': "avenue",
    'incomformities': ["AV", "Av", "av"]
}

BOULEVARD_WORDS = {
    'correct_name': "boulevard",
    'incomformities': ["BD", "Bd", "bd"]
}

CHEMIN_WORDS = {
    'correct_name': "chemin",
    'incomformities': ["CHE", "Che", "che"]
}

COURS_WORDS = {
    'correct_name': "cours",
    'incomformities': ["CRS", "Crs", "crs"]
}

IMPASSE_WORDS = {
    'correct_name': "impasse",
    'incomformities': ["IMP", "Imp", "imp"]
}

PASSAGE_WORDS = {
    'correct_name': "passage",
    'incomformities': ["PAS", "Pas", "pas"]
}

PLACE_WORDS = {
    'correct_name': "place",
    'incomformities': ["PL", "Pl", "pl"]
}

PROMENADE_WORDS = {
    'correct_name': "promenade",
    'incomformities': ["PROM", "Prom", "prom"]
}

QUAI_WORDS = {
    'correct_name': "quai",
    'incomformities': ["QU", "Qu", "qu"]
}

ROUTE_WORDS = {
    'correct_name': "route",
    'incomformities': ["RTE", "Rte", "rte"]
}

RUE_WORDS = {
    'correct_name': "rue",
    'incomformities': ["R", "r"]
}

SENTE_WORDS = {
    'correct_name': "sente",
    'incomformities': ["SEN", "Sen", "sen"]
}
