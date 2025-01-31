''' A very basic compatibility matrix for the Saint Seiya Zodiac Signs (Other people might say they are just zodiac signs LOL)
Requires: numpy, seaborn, matplotlib, but if you want to save the work, you can only copy the image or download it from the repository.
'''

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


signs = [
    "Aries", "Tauro", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]


elements = {
    "Aries": "Fire", "Leo": "Fire", "Sagittarius": "Fire",
    "Tauro": "Earth", "Virgo": "Earth", "Capricorn": "Earth",
    "Gemini": "Wind", "Libra": "Wind", "Aquarius": "Wind",
    "Cancer": "Water", "Scorpio": "Water", "Pisces": "Water"
}


def calculate_compatibility(sign1, sign2):
    elem1, elem2 = elements[sign1], elements[sign2]

    if elem1 == elem2:
        return 10  # !!!!
    elif (elem1 == "Fire" and elem2 == "Wind") or (elem1 == "Wind" and elem2 == "Fire"):
        return 7.5  # Buen 
    elif (elem1 == "Earth" and elem2 == "Water") or (elem1 == "Water" and elem2 == "Earth"):
        return 7.5  # Buen 
    elif (elem1 == "Fire" and elem2 == "Earth") or (elem1 == "Earth" and elem2 == "Fire"):
        return 2.5  # Meh
    elif (elem1 == "Water" and elem2 == "Wind") or (elem1 == "Wind" and elem2 == "Water"):
        return 2.5  # Meh
    elif (elem1 == "Fire" and elem2 == "Water") or (elem1 == "Water" and elem2 == "Fire"):
        return 0.0  # Nope
    elif (elem1 == "Earth" and elem2 == "Wind") or (elem1 == "Wind" and elem2 == "Earth"):
        return 0.0  # Nope
    else:
        return 5  # x


compatibility = np.array([[calculate_compatibility(s1, s2) for s2 in signs] for s1 in signs])


plt.figure(figsize=(7, 7))
sns.heatmap(compatibility, annot=True, cmap="Purples", xticklabels=signs, yticklabels=signs)


plt.title("Saint Seiya Zodiac Compatibility")
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)


plt.show()
