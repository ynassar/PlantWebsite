from models import Plant

def getWaterConsumption(plant):
    string = plant.irrigation
    if string == "Low":
        return 50
    elif string == "Moderate":
        return 75
    else:
        return 100

def getCost(plant):
    return plant.material_cost + plant.planting_cost + plant.maintainence_cost_during_execution + plant.maintainence_cost_after_initial_handing_over

toleranceLevels = ['No preference','', 'Intolerant', 'M. Tolerant', 'L. Tolerant', 'Tolerant']
def getRequiredArr(typesRequired):
    requiredArr = []
    for typeRequired in typesRequired:
        saltToleranceIdx = toleranceLevels.index(typesRequired[typeRequired]['minSaltTolerance'])
        droughtToleranceIdx = toleranceLevels.index(typesRequired[typeRequired]['minDroughtTolerance'])
        bloomsIn = typesRequired[typeRequired]['bloomsIn']
        minRoots = typesRequired[typeRequired]['minRoots']
        minSpread = typesRequired[typeRequired]['minSpread']
        minHeight = typesRequired[typeRequired]['minHeight']
        typeArr = Plant.objects.filter(classification=typeRequired)
        for i in range(saltToleranceIdx - 1, 0, -1):
            typeArr = typeArr.exclude(salt_tolerance = toleranceLevels[i])
        for i in range(droughtToleranceIdx - 1,0, -1):
            typeArr = typeArr.exclude(drought_tolerance = toleranceLevels[i])
        if bloomsIn[0]:
            typeArr = typeArr.exclude(blooms_in_jan = False)
        if bloomsIn[1]:
            typeArr = typeArr.exclude(blooms_in_feb = False)
        if bloomsIn[2]:
            typeArr = typeArr.exclude(blooms_in_mar = False)
        if bloomsIn[3]:
            typeArr = typeArr.exclude(blooms_in_apr = False)
        if bloomsIn[4]:
            typeArr = typeArr.exclude(blooms_in_may = False)
        if bloomsIn[5]:
            typeArr = typeArr.exclude(blooms_in_jun = False)
        if bloomsIn[6]:
            typeArr = typeArr.exclude(blooms_in_jul = False)
        if bloomsIn[7]:
            typeArr = typeArr.exclude(blooms_in_aug = False)
        if bloomsIn[8]:
            typeArr = typeArr.exclude(blooms_in_sep = False)
        if bloomsIn[9]:
            typeArr = typeArr.exclude(blooms_in_oct = False)
        if bloomsIn[10]:
            typeArr = typeArr.exclude(blooms_in_nov = False)
        if bloomsIn[11]:
            typeArr = typeArr.exclude(blooms_in_dec = False)
        typeArr = typeArr.exclude(min_spread__lt = 0)
        typeArr = typeArr.exclude(min_roots__lt = 0)
        typeArr = typeArr.exclude(min_height__lt = minHeight)
        requiredArr.append(typeArr)
    return requiredArr


def getOptimalSolutionRec(typesRequired, waterConsumptionLeft, requiredArr, dpArr, i, j):
    if i == len(requiredArr):
        solution = 0
        dpArr[(waterConsumptionLeft, i, j)] = solution
        return 0

    if j == len(requiredArr[i]):
        solution = 0
        dpArr[(waterConsumptionLeft, i, j)] = solution
        return 1e9

    if (waterConsumptionLeft, i, j) in dpArr:
        return dpArr[(waterConsumptionLeft, i, j)]

    numRequired = typesRequired[requiredArr[i][j].classification]['numReq']
    currentItemWaterConsumption = numRequired * getWaterConsumption(requiredArr[i][j])
    currentItemCost = numRequired * getCost(requiredArr[i][j])

    if waterConsumptionLeft >= currentItemWaterConsumption:
        solution = min(currentItemCost +
                 getOptimalSolutionRec(typesRequired, waterConsumptionLeft - currentItemWaterConsumption, requiredArr, dpArr, i + 1, 0),
                  getOptimalSolutionRec(typesRequired, waterConsumptionLeft, requiredArr, dpArr, i, j + 1))
        dpArr[(waterConsumptionLeft,i,j)] = solution
        return solution


    solution = getOptimalSolutionRec(typesRequired, waterConsumptionLeft, requiredArr, dpArr, i, j + 1)
    dpArr[(waterConsumptionLeft,i,j)] = solution
    return solution

def getActualPlantsRec(typesRequired, waterConsumptionLeft, requiredArr, dpArr, i, j, actualPlants):
    if i == len(requiredArr):
        return
    if j == len(requiredArr[i]):
        return

    numRequired = typesRequired[requiredArr[i][j].classification]['numReq']
    currentItemWaterConsumption = numRequired * getWaterConsumption(requiredArr[i][j])
    currentItemCost = numRequired * getCost(requiredArr[i][j])

    if waterConsumptionLeft >= currentItemWaterConsumption:
        if dpArr[(waterConsumptionLeft, i, j)] == currentItemCost + dpArr[(waterConsumptionLeft - currentItemWaterConsumption, i + 1, 0)]:
            actualPlants.append(requiredArr[i][j])
            getActualPlantsRec(typesRequired, waterConsumptionLeft - currentItemWaterConsumption, requiredArr, dpArr, i + 1, 0, actualPlants)
        else:
            getActualPlantsRec(typesRequired, waterConsumptionLeft, requiredArr, dpArr, i, j + 1, actualPlants)
        return

    getActualPlantsRec(typesRequired, waterConsumptionLeft, requiredArr, dpArr, i, j + 1, actualPlants)

def listAllSolutionsRec(solutionsList, i, j, waterConsumptionLeft, cost, maxWaterConsumption, requiredArr, typesRequired):
    if i == len(requiredArr):
        solutionsList.append((maxWaterConsumption - waterConsumptionLeft, cost))
        return
    if j == len(requiredArr[i]):
        return
    numRequired = typesRequired[requiredArr[i][j].classification]['numReq']
    currentItemWaterConsumption = numRequired * getWaterConsumption(requiredArr[i][j])
    currentItemCost = numRequired * getCost(requiredArr[i][j])
    if waterConsumptionLeft >= currentItemWaterConsumption:
        listAllSolutionsRec(solutionsList, i + 1, 0, waterConsumptionLeft - currentItemWaterConsumption, cost + currentItemCost, maxWaterConsumption, requiredArr, typesRequired)
    listAllSolutionsRec(solutionsList, i, j + 1, waterConsumptionLeft, cost, maxWaterConsumption, requiredArr, typesRequired)


def getOptimalSolution(maxWaterConsumption, typesRequired):
    requiredArr = getRequiredArr(typesRequired)
    dpArr = {}
    optimalSolution = getOptimalSolutionRec(typesRequired, maxWaterConsumption, requiredArr, dpArr, 0,0)
    actualPlants = []
    getActualPlantsRec(typesRequired, maxWaterConsumption, requiredArr, dpArr, 0,0, actualPlants)
    solutionsList = []
    listAllSolutionsRec(solutionsList, 0, 0, maxWaterConsumption, 0, maxWaterConsumption, requiredArr, typesRequired)
    return (optimalSolution, actualPlants, solutionsList)
