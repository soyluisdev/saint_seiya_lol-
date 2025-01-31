# Saint Seiya Zodiac Compatibility Matrix

![Project image](/project.png)

A very basic compatibility matrix for the Saint Seiya Zodiac Signs (Some people might say they are just zodiac signs... LOL 😂)

## Requirements

- numpy
- seaborn
- matplotlib

If you want to save the work, you can only copy the image or download it from the repository.

## Usage

```python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

signos = [
    "Aries", "Tauro", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

elementos = {
    "Aries": "Fire", "Leo": "Fire", "Sagittarius": "Fire",
    "Tauro": "Earth", "Virgo": "Earth", "Capricorn": "Earth",
    "Gemini": "Wind", "Libra": "Wind", "Aquarius": "Wind",
    "Cancer": "Water", "Scorpio": "Water", "Pisces": "Water"
}

def calcular_compatibilidad(signo1, signo2):
    elem1, elem2 = elementos[signo1], elementos[signo2]

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

compatibilidad = np.array([[calcular_compatibilidad(s1, s2) for s2 in signos] for s1 in signos])

plt.figure(figsize=(7, 7))
sns.heatmap(compatibilidad, annot=True, cmap="Purples", xticklabels=signos, yticklabels=signos)

plt.title("Saint Seiya Zodiac Compatibility")
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)

plt.show()