from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest
from django.http import HttpResponse
from django.template.loader import get_template
from models import Plant
from optimization import getOptimalSolution
from optimization import getCost
from optimization import getWaterConsumption

import csv
# Create your views here.
import os


def to_float(string):
    if string == '':
        return 1
    if string == '???':
        return 1e9
    string = string.replace(',', '')
    return float(string)

def to_bool(string):
    if 'x' in string:
        return True
    return False

def to_int(string):
    if string == '':
        return 1
    string = string.replace(',', '')
    return int(string)

def update_db():
    with open('/mnt/project/KnapsackSolver/data.txt') as f:
        reader = csv.reader(f)
        for fields in reader:
            if len(fields) == 0:
                continue
            #print(fields[10])
            if(Plant.objects.filter(serial_number = fields[0]).exists()):
                existing_plant = Plant.objects.filter(serial_number = fields[0])
                existing_plant.code = fields[1],
                existing_plant.classification = fields[2],
                existing_plant.plant_type = fields[3],
                existing_plant.genus = fields[4],
                existing_plant.species = fields[5],
                existing_plant.latin_name = fields[6],
                existing_plant.common_name = fields[7],
                existing_plant.min_spread = to_float(fields[10]),
                existing_plant.max_spread = to_float(fields[11]),
                existing_plant.min_height = to_float(fields[12]),
                existing_plant.max_height = to_float(fields[13]),
                existing_plant.min_roots = to_float(fields[14]),
                existing_plant.max_roots = to_float(fields[15]),
                existing_plant.blooms_in_jan = to_bool(fields[16]),
                existing_plant.blooms_in_feb = to_bool(fields[17]),
                existing_plant.blooms_in_mar = to_bool(fields[18]),
                existing_plant.blooms_in_apr = to_bool(fields[19]),
                existing_plant.blooms_in_may = to_bool(fields[20]),
                existing_plant.blooms_in_jun = to_bool(fields[21]),
                existing_plant.blooms_in_jul = to_bool(fields[22]),
                existing_plant.blooms_in_aug = to_bool(fields[23]),
                existing_plant.blooms_in_sep = to_bool(fields[24]),
                existing_plant.blooms_in_oct = to_bool(fields[25]),
                existing_plant.blooms_in_nov = to_bool(fields[26]),
                existing_plant.blooms_in_dec = to_bool(fields[27]),
                existing_plant.min_life_cycle = to_int(fields[28]),
                existing_plant.max_life_cycle = to_int(fields[29]),
                existing_plant.light = fields[30],
                existing_plant.soil_ph = to_float(fields[31]),
                existing_plant.salt_tolerance = fields[32],
                existing_plant.drought_tolerance = fields[33],
                existing_plant.irrigation = fields[34],
                existing_plant.UOM = fields[35],
                existing_plant.material_cost = to_float(fields[36]),
                existing_plant.planting_cost = to_float(fields[37]),
                existing_plant.maintainence_cost_during_execution = to_float(fields[38]),
                existing_plant.maintainence_cost_after_initial_handing_over = to_float(fields[39])
                existing_plant[0].save()
            else:
                new_plant = Plant(serial_number = fields[0],
                              code = fields[1],
                              classification = fields[2],
                              plant_type = fields[3],
                              genus = fields[4],
                              species = fields[5],
                              latin_name = fields[6],
                              common_name = fields[7],
                              min_spread = to_float(fields[10]),
                              max_spread = to_float(fields[11]),
                              min_height = to_float(fields[12]),
                              max_height = to_float(fields[13]),
                              min_roots = to_float(fields[14]),
                              max_roots = to_float(fields[15]),
                              blooms_in_jan = to_bool(fields[16]),
                              blooms_in_feb = to_bool(fields[17]),
                              blooms_in_mar = to_bool(fields[18]),
                              blooms_in_apr = to_bool(fields[19]),
                              blooms_in_may = to_bool(fields[20]),
                              blooms_in_jun = to_bool(fields[21]),
                              blooms_in_jul = to_bool(fields[22]),
                              blooms_in_aug = to_bool(fields[23]),
                              blooms_in_sep = to_bool(fields[24]),
                              blooms_in_oct = to_bool(fields[25]),
                              blooms_in_nov = to_bool(fields[26]),
                              blooms_in_dec = to_bool(fields[27]),
                              min_life_cycle = to_int(fields[28]),
                              max_life_cycle = to_int(fields[29]),
                              light = fields[30],
                              soil_ph = to_float(fields[31]),
                              salt_tolerance = fields[32],
                              drought_tolerance = fields[33],
                              irrigation = fields[34],
                              UOM = fields[35],
                              material_cost = to_float(fields[36]),
                              planting_cost = to_float(fields[37]),
                              maintainence_cost_during_execution = to_float(fields[38]),
                              maintainence_cost_after_initial_handing_over = to_float(fields[39])
                             )
                new_plant.save()



def homepage(request):
    if request.method == 'POST':
        update_db()
    return render(request, 'Homepage.html',
                  {
                      'passed_string' : 'YOLO',
                   'plant_types' : ['Aquatic Plants', 'Climbers', 'Ground Cover', 'Ornamental Grass',
                                   'Palm-like', 'Palms', 'Shrubs', 'Succulent', 'Trees']
                  }
                 )

def getDataFromPOST(POST):
    maxWaterConsumption = int(POST["max-water-consumption"])
    numFields = int(POST["num-rows"])
    typesRequired = {}
    for i in range(1, numFields + 1):
        numRequired = int(POST["number-input-" + str(i)])
        typeRequired = POST["type-input-" + str(i)]
        if not typeRequired in typesRequired:
            typesRequired[typeRequired] = numRequired
        else:
            typesRequired[typeRequired] += numRequired
    return (maxWaterConsumption, typesRequired)

def solve(request):
    if not 'number-input-1' in request.POST:
        return redirect("/")
    maxWaterConsumption, typesRequired = getDataFromPOST(request.POST)
    (sol, plantList) = getOptimalSolution(maxWaterConsumption, typesRequired)
    plantInfo = []
    sumOfCosts, totalWC = 0, 0
    for plant in plantList:
        plantInfo.append({
            'serialNumber' : plant.serial_number,
            'classification' : plant.classification,
            'numRequested' : typesRequired[plant.classification],
            'waterConsumption' : typesRequired[plant.classification] * getWaterConsumption(plant),
            'totalCost' : typesRequired[plant.classification] * getCost(plant),
            'commonName' : plant.common_name,
            'latinName' : plant.latin_name
        })
        sumOfCosts += typesRequired[plant.classification] * getCost(plant)
        totalWC += typesRequired[plant.classification] * getWaterConsumption(plant)

    return render(request, 'DisplaySolution.html', {
        'solution_plants' : plantInfo,
        'solutionExists' : len(plantInfo) != 0,
        'sumOfCosts' : sumOfCosts,
        'totalWaterConsumption' : totalWC,
    });
