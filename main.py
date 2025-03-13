import novels_writers
import novels
import iq_level

# List of characters
characters = {
    "Colonel Faridi": "Jasosi Dunya & Faridi Series",
    "Ali Imran": "Imran Series",
    "Major Parmood": "Parmood Series",
    "Salaar Sikander": "Peer_e_Kamil"
}

# Loop through characters and display information
for character, novel_key in characters.items():
    print(f"\nCharacter: {character}")
    print(f"Writer(s): {', '.join(novels_writers.novels_writers[novel_key])}")
    print(f"Novel: {novels.novels[novel_key]}")
    print(f"IQ Level: {iq_level.iq_level.get(character, 'N/A')[0]}")