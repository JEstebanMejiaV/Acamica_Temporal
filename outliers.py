def getBigotes(data, feature):
    '''
    Función que recibe un DataFrame y analiza los valores de los bigotes inferior y superior en el Feature especificado.
    
    Argumentos:
    data = DataFrame
    feature = Feature sobre el cual buscamos los outliers    
    allFeaturesOutput = True devuelve en la salida, todos los features, si es False solo devuelve el especificado.
    
    '''
    quantile1 = data[feature].quantile(0.25)
    quantile3 = data[feature].quantile(0.75)
    
    interCuartil = quantile3 - quantile1
        
    bigoteInferior = (quantile1 - 1.5 * interCuartil)
    bigoteSuperior = (quantile3 + 1.5 * interCuartil)
    
    return bigoteInferior, bigoteSuperior

def getOutliersForFeature(data, feature, order=False, allFeaturesOutput=False):    
    '''
    Función que recibe un DataFrame y devuelve los Outliers que presenta el Feature especificado.
    
    Argumentos:
    data = DataFrame
    feature = Feature sobre el cual buscamos los outliers
    order = True ordena la salida por los valores de los outliers
    allFeaturesOutput = True devuelve en la salida, todos los features, si es False solo devuelve el especificado.
    
    Retorno:
    DataFrame con todos los outliers que tiene el feature.
    '''

    bigoteInferior, bigoteSuperior = getBigotes(data, feature)
    
    indexOutliers = (data[feature] < bigoteInferior) | (data[feature] > bigoteSuperior)
    instancesOutliers = data[indexOutliers]
    
    if (order == True):
        outliersOrder = instancesOutliers.sort_values(feature)
        
        if (allFeaturesOutput == True):
            outliers = outliersOrder
        else:
            outliers = outliersOrder[feature]
    else:
        if (allFeaturesOutput == True):
            outliers = instancesOutliers
        else:
            outliers = instancesOutliers[feature]        
    
    return outliers

def dropOutliersForFeature(data, feature, allFeaturesOutput = False):  
    '''
    Función que recibe un DataFrame, le quita los Outliers que presenta el Feature especificado.
    
    Argumentos:
    data = DataFrame
    feature = Feature sobre el cual buscamos los outliers    
    allFeaturesOutput = True devuelve en la salida, todos los features, si es False solo devuelve el especificado.
    
    Retorno:
    DataFrame sin los outliers que tiene el feature.
    '''
    
    bigoteInferior, bigoteSuperior = getBigotes(data, feature)
    
    indexWithoutOutliers = (data[feature] >= bigoteInferior) & (data[feature] <= bigoteSuperior)
    instancesWithoutOutliers = data[indexWithoutOutliers]
    
    if (allFeaturesOutput == True):
        dataWithoutOutliers = instancesWithoutOutliers
    else:
        dataWithoutOutliers = instancesWithoutOutliers[feature]

    return dataWithoutOutliers
