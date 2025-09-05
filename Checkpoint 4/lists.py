#["Inicio", 2, 5.6, ["end", "post"]]
indepence_stages = ["Inicio", "Organizacion", "Resistencia", "Consumacion"]
print(indepence_stages[0])
print(len(indepence_stages))

#List Methods
#indepence_stages.append("Post Inde") add things to the list
leaders = []
leaders.append("Miguel Hidalgo")
leaders.append("Vicente Guerrero")
#leaders.extend(indepence_stages) //Mix lists together
leaders.insert(1,"Jose Maria Morelos")
#leaders.remove("Vicente Guerrero") //delete first match of specific items
leaders.append("Agustin Iturbide")
#leaders.pop(1) 
#leaders.clear() //remove the list
print(leaders.index("Miguel Hidalgo"))
print(leaders.count("Vicente Guerrero"))
#leaders.sort() //acomodar en order alfabetico
#leaders.reverse() //poner al reves el orden
new_leaders = leaders.copy


print(leaders)
print(new_leaders)