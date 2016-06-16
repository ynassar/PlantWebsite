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


def getRequiredArr(typesRequired):
    requiredArr = []
    for typeRequired in typesRequired:
        typeArr = Plant.objects.filter(classification=typeRequired)
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

    numRequired = typesRequired[requiredArr[i][j].classification]
    currentItemWaterConsumption = numRequired * getWaterConsumption(requiredArr[i][j])
    currentItemCost = numRequired * getCost(requiredArr[i][j])

    if waterConsumptionLeft >= getWaterConsumption(requiredArr[i][j]):
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

    numRequired = typesRequired[requiredArr[i][j].classification]
    currentItemWaterConsumption = numRequired * getWaterConsumption(requiredArr[i][j])
    currentItemCost = numRequired * getCost(requiredArr[i][j])

    if waterConsumptionLeft >= getWaterConsumption(requiredArr[i][j]):
        if dpArr[(waterConsumptionLeft, i, j)] == currentItemCost + dpArr[(waterConsumptionLeft - currentItemWaterConsumption, i + 1, 0)]:
            actualPlants.append(requiredArr[i][j])
            getActualPlantsRec(typesRequired, waterConsumptionLeft - currentItemWaterConsumption, requiredArr, dpArr, i + 1, 0, actualPlants)
        else:
            getActualPlantsRec(typesRequired, waterConsumptionLeft, requiredArr, dpArr, i, j + 1, actualPlants)
        return

    getActualPlantsRec(typesRequired, waterConsumptionLeft, requiredArr, dpArr, i, j + 1, actualPlants)


def getOptimalSolution(maxWaterConsumption, typesRequired):
    requiredArr = getRequiredArr(typesRequired)
    dpArr = {}
    optimalSolution = getOptimalSolutionRec(typesRequired, maxWaterConsumption, requiredArr, dpArr, 0,0)
    actualPlants = []
    getActualPlantsRec(typesRequired, maxWaterConsumption, requiredArr, dpArr, 0,0, actualPlants)
    return (optimalSolution, actualPlants)
