# доработка мб смена дб
COMPONENT_DATA = {
    "cpu": ["Intel Core i5-12600K", "AMD Ryzen 5 5600X", "Intel Core i7-13700K"],
    "motherboard": ["ASUS ROG Strix Z790-A", "MSI MAG B650 Tomahawk", "Gigabyte B760 AORUS ELITE AX"],
    "ram": ["Corsair Vengeance DDR5 32GB", "Kingston Fury DDR4 16GB", "G.Skill Trident Z5 32GB"],
    "gpu": ["NVIDIA GeForce RTX 4070", "AMD Radeon RX 6800 XT", "NVIDIA GeForce RTX 3060"],
    "storage": ["Samsung 980 Pro 1TB", "Seagate Barracuda 2TB", "Western Digital Black SN850X 1TB"],
    "power": ["Corsair RM850x", "Seasonic Focus GX-750", "EVGA SuperNOVA 850 GT"],
    "case": ["NZXT H510 Flow", "Fractal Design Meshify 2", "Lian Li O11 Dynamic"],
    "cooler": ["Noctua NH-D15", "Corsair iCUE H150i Elite", "Cooler Master Hyper 212"]
}

CONFIGURATIONS = {}

COMPATIBILITY_RULES = {
    "cpu": {
        "Intel Core i5-12600K": ["ASUS ROG Strix Z790-A", "Gigabyte B760 AORUS ELITE AX"],
        "AMD Ryzen 5 5600X": ["MSI MAG B650 Tomahawk"],
        "Intel Core i7-13700K": ["ASUS ROG Strix Z790-A","Gigabyte B760 AORUS ELITE AX"]
    },
    "ram":{
        "Corsair Vengeance DDR5 32GB": ["ASUS ROG Strix Z790-A", "Gigabyte B760 AORUS ELITE AX"],
        "Kingston Fury DDR4 16GB": ["MSI MAG B650 Tomahawk"],
        "G.Skill Trident Z5 32GB": ["ASUS ROG Strix Z790-A","Gigabyte B760 AORUS ELITE AX"]
    }
}