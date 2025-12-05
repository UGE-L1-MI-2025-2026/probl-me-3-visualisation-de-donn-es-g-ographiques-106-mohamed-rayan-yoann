
"""for i in range(len(sf.records())):
    record = sf.record(i)
    code_dept = record[0]

    if code_dept not in codes_outre_mer:
        print(code_dept)
        dept = sf.shape(i)
        liste = dept.points #La liste des points du contour du departement en cours
        liste_mercator = list(map(wgs_mercator, (point for point in liste)))
        x = [point[0] for point in liste_mercator]
        y = [point[1] for point in liste_mercator]

        min_x , max_x = min(x), max(x)
        min_y, min_x = min(y), max(y)"""