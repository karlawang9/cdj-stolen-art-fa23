candles = ["Candlesticks", "Candle Snuffers", "candlestickcandleholder", "Candlesticks and Holders", "Incense Burndeers"]
collectibles = ["Coins and Paper Money", "Stamps", "Other - Collectibles", "sports,collectibles", "other,collectibles", "Sports Collectibles"]
containers=["Boxes", "Cigarette Case", "Vase", "Ornamental Ceramic Wares", "Holloware", "metal,flatware", "Metal Flatware", "Flatware", "Ceramic Tea and Coffee Wares", "Bowls", "Napkin Ring"]
religion=["Cross", "Monstrance", "Altar", "Shrine", "Ethnographic Works of Art", "Crucifix", "Pedestals", "Triptych/Diptych/Icon","icon,triptych,diptych"]
accessories=["mask", "Brooches and Pins", "other,jewelry", "Other - Jewelry", "Jewelry - Pendants", "Jewelry - Rings", "Jewelry - Earrings", "Bracelets", "Necklaces", "pocketwatch", "Timepieces - Pocket Watch"]
instruments=["Instruments - String", "Instruments - Guitars", "Other - Musical Instruments", "Instruments - Wind", "stringinstruments", "Bell"]
furniture=["firefurniture", "Furniture - Table", "Cabinets","winecooler", "Wine Cooler", "lamp","clock,timepiece","Timepieces - Clock","Timepieces - Sundial","Doors","Mirror"]
warRelics=["Cannon","Guns and Firearms - Rifle","Guns and Firearms","Blades"]
fabrics=["Sampler","Tapestry","Carpet","other,textiles","Other - Textiles","Clothing and Costumes"]
figures=["figurineMaker","Figurine","Netsuke","Dolls and Figurines","dollsandfigurines","Sculpture","016144","Boats"]
observationalTools=["Navigational Instruments","Binoculars and Telescopes"]
physicalArt=["Paintings","Posters","Photographs","Jardiniere","drawing,watercolour","Watercolour Drawings","Books","Print"]
flatSurfaces=["Mosaic","Stained Glass","Screen"]
miscellaneous=["boardgames","Board Games","other,assorted","Other - Arts and Antiques","Other - Assorted","None","Condiments","nan"]

import pandas as pd
data = pd.read_csv("../data/nsaf_data.csv")

small_categories=data["Category"]

large_categories=[candles, collectibles, containers, religion, accessories,
      instruments, furniture, warRelics,
      fabrics, figures,observationalTools,
      physicalArt, flatSurfaces, miscellaneous]

names=["Candles", "Collectibles", "Containers", "Relgion", "Accessories", "Instruments", "Furniture", "War Relics",
      "Fabrics", "Figures","Observational Tools", "Physical Art", "Flat Surfaces", "Miscellaneous"]

Category=[]

for element in small_categories: 
    seen=False
    for i in range(len(large_categories)):
        if element in large_categories[i]:
            Category.append(names[i])
            seen=True
            break
    if seen==False:
        Category.append("")
    

data.insert(2, column="New Category", value=Category)
data.to_csv("../data/nsaf_data_new.csv")

