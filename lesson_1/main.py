
line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days"
replacement = "Eyjafjallajokull"
marker='EY'
marker_end=len(marker)
start=line.find(marker)
part_a=line[:start]
part_b=line[start+marker_end:]
replaced=part_a+replacement+part_b
print replaced