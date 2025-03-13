import novels_writers
import novels
import iq_level

# Define Functions for each task

def get_writer(novel_key):
    novels_writers = {
        "Jasosi Dunya & Faridi Series": ["Sir.Ibne-Safi", "&", "Second Writer Sir.Mazhar-Kaleem-M.A"],
        "Imran Series": ["Sir.Ibne-Safi", "&", "Second Writer Sir.Mazhar-Kaleem-M.A"],
        "Parmod Series": ["Sir.Mazhar-Kaleem-M.A", "H.Iqbal"],
        "Aabe Hayat": ["Umera Ahmed"],
        "Peer_e_Kamil": ["Umera Ahmed"]
    }
    return novels_writers.get(novel_key, ["Writer not found"])

def get_novel(novel_key):
    novels = {
        "Jasosi Dunya & Faridi Series": "Colonel Faridi",
        "Imran Series": "Ali Imran-M.S.C-D.S.C-(OXEN)-Oxford",
        "Parmod Series": "Major Parmood",
        "Peer_e_Kamil": "Salaar Sikander & Imama Hashim",
        "Aabe Hayat": "Salaar Sikander & Imama Hashim"
    }
    return novels.get(novel_key, "Novel not found")

def get_iq_level(character):
    iq_level = {
        "Salaar Sikander & Imama Hashim": "150+",
        "Major Parmood": "150+",
        "Colonel Faridi": "160+",
        "Ali Imran-M.S.C-D.S.C-(OXEN)-Oxford": "170+",
    }
    return iq_level.get(character, "N/A")

# Main Code to Display Information

characters = {
    "Colonel Faridi": "Jasosi Dunya & Faridi Series",
    "Ali Imran": "Imran Series",
    "Major Parmood": "Parmod Series",
    "Salaar Sikander": "Peer_e_Kamil"
}

for character, novel_key in characters.items():
    print(f"\nCharacter: {character}")
    print(f"Writer(s): {', '.join(get_writer(novel_key))}")
    print(f"Novel: {get_novel(novel_key)}")
    print(f"IQ Level: {get_iq_level(character)}")