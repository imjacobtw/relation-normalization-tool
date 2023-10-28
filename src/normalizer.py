def Normalize(relation, normalForm):
    normalizedRelations = []

    match normalForm:
        case "1NF":
            normalizedRelations.append(relation)
    
    return normalizedRelations
    
