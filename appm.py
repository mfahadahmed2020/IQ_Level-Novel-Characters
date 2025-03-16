# import novels_writers
# import novels
# import iq_level
'''
# IQ Level Dictionary with all characters
iq_level = {
    "Salaar Sikander & Imama Hashim": "150+",
    "Major Parmood": "150+",
    "Colonel Faridi": "160+",
    "Ali Imran-M.S.C-D.S.C-(OXEN)-Oxford": "170+",
    # Add IQ level for Ali Imran and Salaar Sikander
    "Ali Imran": "170+",  # Add the IQ Level for Ali Imran here
    "Salaar Sikander": "150+"  # Add the IQ Level for Salaar Sikander here
}

# Main Code to Display Information

characters = {
    "Colonel Faridi": "Jasosi Dunya & Faridi Series",
    "Ali Imran": "Imran Series",
    "Major Parmood": "Parmod Series",
    "Salaar Sikander": "Peer_e_Kamil"
}

# Loop to display all characters with their information
for character, novel_key in characters.items():
    print(f"\nCharacter: {character}")
    print(f"Writer(s): {', '.join(get_writer(novel_key))}") # type: ignore
    print(f"Novel: {get_novel(novel_key)}") # type: ignore
    print(f"IQ Level: {get_iq_level(character)}") # type: ignore
'''

    # IQ Level Dictionary with all characters
iq_level = {
    "Salaar Sikander & Imama Hashim": "150+",
    "Major Parmood": "150+",
    "Colonel Faridi": "160+",
    "Ali Imran-M.S.C-D.S.C-(OXEN)-Oxford": "170+",
    # Add IQ level for Ali Imran and Salaar Sikander
    "Ali Imran": "170+",  # Add the IQ Level for Ali Imran here
    "Salaar Sikander": "150+"  # Add the IQ Level for Salaar Sikander here
}

# Novels Dictionary
novels = {
    "Jasosi Dunya & Faridi Series": "Colonel Faridi",
    "Imran Series": "Ali Imran-M.S.C-D.S.C-(OXEN)-Oxford",
    "Parmod Series": "Major Parmood",
    "Peer_e_Kamil": "Salaar Sikander & Imama Hashim"
}

# Writers Dictionary
novels_writers = {
    "Jasosi Dunya & Faridi Series": ["Sir.Ibne-Safi", "&", "Second Writer Sir.Mazhar-Kaleem-M.A"],
    "Imran Series": ["Sir.Ibne-Safi", "&", "Second Writer Sir.Mazhar-Kaleem-M.A"],
    "Parmod Series": ["Sir.Mazhar-Kaleem-M.A"],
    "Peer_e_Kamil": ["Umera Ahmed"],
}

# Functions to fetch the data
def get_writer(novel_key):
    # This function returns the writers of the novel by the key
    return novels_writers.get(novel_key, ["Unknown Writer"])

def get_novel(novel_key):
    # This function returns the name of the novel
    return novels.get(novel_key, "Unknown Novel")

def get_iq_level(character):
    # This function returns the IQ level for the character
    return iq_level.get(character, "N/A")

# Main Code to Display Information
characters = {
    "Colonel Faridi": "Jasosi Dunya & Faridi Series",
    "Ali Imran": "Imran Series",
    "Major Parmood": "Parmod Series",
    "Salaar Sikander": "Peer_e_Kamil"
}

# Loop to display all characters with their information
for character, novel_key in characters.items():
    print(f"\nCharacter: {character}")
    print(f"Writer(s): {', '.join(get_writer(novel_key))}")  # get writers of the novel
    print(f"Novel: {get_novel(novel_key)}")  # get novel name
    print(f"IQ Level: {get_iq_level(character)}")  # get IQ level of the character