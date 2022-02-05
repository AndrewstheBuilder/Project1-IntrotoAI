import State
import copy
import csv
from operator import attrgetter
"""
Project1.py - main method reads
in state information from csv and
sets list of state objects

Author: Andrews Peter
Version: 1/30/22
Email: n01364109@unf.edu
"""


def printStatesReport(statesList):
    """
    :param statesList - list of state objects
    print states in statesList
    """
    print(f"{'Name':15s}{'MHI':15s}{'VCR':15s}{'CFR':15s}{'Case Rate':15s}{'Death Rate':15s}{'FVR':15s}")
    print('-------------------------------------------------------------------------------------------------')
    for state in statesList:
        print(f"{state.getState():15s}{state.getMHI():15s}{state.getVCR():15s}{state.getCFR():15s}{state.getCaseRate():15s}{state.getDeathRate():15s}{state.getFVR():15s}")


def sortByStateName(statesList, start, end):
    """
    :param statesList - list of state objects, start - start of array.
    :param end - initialized in the beginning to len(statesList)-1.
    sort list of state objects by state name
    implemented using quick sort
    """
    if start < end:
        pivotValue = statesList[end]
        pivotIndex = start
        for i in range(start, end+1):
            if statesList[i].getState() <= pivotValue.getState():
                temp = statesList[i]
                statesList[i] = statesList[pivotIndex]
                statesList[pivotIndex] = temp
                pivotIndex += 1
        pivotIndex -= 1
        sortByStateName(statesList, start, pivotIndex-1)
        sortByStateName(statesList, pivotIndex+1, end)


def sortByCFR(statesList):
    """
    sort list of state objects by Covid Fataility Rate
    implemented using Merge Sort
    :param statesList - list of state objects
    """
    if len(statesList) > 1:
        mid = len(statesList)//2
        leftList = statesList[:mid]
        rightList = statesList[mid:]
        sortByCFR(leftList)
        sortByCFR(rightList)
        x = y = z = 0

        while x < len(leftList) and y < len(rightList):
            if leftList[x].getCFR() < rightList[y].getCFR():
                statesList[z] = leftList[x]
                x += 1
            else:
                statesList[z] = rightList[y]
                y += 1
            z += 1

        while x < len(leftList):
            statesList[z] = leftList[x]
            x += 1
            z += 1

        while y < len(rightList):
            statesList[z] = rightList[y]
            y += 1
            z += 1


def mergeSort(sList, sortBy):
    """
    sort by different attributes like CFR, VCR, stateName, etc
    """
    if len(sList) > 1:
        mid = len(sList)//2
        leftList = sList[:mid]
        rightList = sList[mid:]
        mergeSort(leftList, sortBy)
        mergeSort(rightList, sortBy)
        x = y = z = 0

        while x < len(leftList) and y < len(rightList):

            # if values are equal change conditonal to compare by state name
            leftVar = getattr(leftList[x], sortBy)
            rightVar = getattr(rightList[y], sortBy)
            conditional = False

            if(leftVar == rightVar):
                leftState = getattr(leftList[x], 'state')
                rightState = getattr(rightList[y], 'state')
                conditional =  (leftState < rightState)
            else:
                conditional = (leftVar < rightVar)
            if conditional:
                sList[z] = leftList[x]
                x += 1
            else:
                sList[z] = rightList[y]
                y += 1
            z += 1

        while x < len(leftList):
            sList[z] = leftList[x]
            x += 1
            z += 1

        while y < len(rightList):
            sList[z] = rightList[y]
            y += 1
            z += 1


def binarySearch(statesList, start, end, state):
    """
    find state name in list by
    binary search and print state
    """
    if end >= start:
        mid = int((start+end)/2)
        if statesList[mid].getState().lower() == state.lower():
            print(statesList[mid])
            return
        elif statesList[mid].getState() > state:
            return binarySearch(statesList, start, mid-1, state)
        else:
            return binarySearch(statesList, mid+1, end, state)
    else:
        print(state + ' not found')
        return


def sequentialSearch(statesList, state):
    """
    sequential search for state in statesList
    :return position of state if found
    """
    for i in range(0, len(statesList)):
        if statesList[i].getState().lower() == state.lower():
            return i
    return -1


def calculateRho(r1, r2, orderedStateNames):
    """
    :return rho value between two rankings
    :param r1 - first ranking ordered by caseRate or deathRate
    :param r2 - second ranking ordered by MHI, VCR, or FVR
    :param orderedStateNames - reference list for ordering of state name
    """
    dSum = 0
    for name in orderedStateNames:
        d1 = sequentialSearch(r1, name)
        d2 = sequentialSearch(r2, name)
        dSum += pow((d1-d2), 2)
    denominator = 50*(pow(50, 2)-1)
    rho = 1-((6*dSum)/denominator)
    return rho


def calculateSpearmanRhoMatrix(statesList):
    """
    :return string of spearmanrho matrix after its calculated
    """

    # Initialize lists for calculating rho
    sortedStateNameList = []
    sortedCaseRateList = []
    sortedDeathRateList = []
    sortedMHIList = []
    sortedVCRList = []
    sortedFVRList = []

    for state in statesList:
        sortedStateNameList.append(State.State(state.getState(), state.getCapitol(), state.getRegion(), state.getUHS(),
                                               state.getPopulation(), state.getCovidCases(), state.getCovidDeaths(), state.getFVR(), state.getMHI(), state.getVCR()))
        sortedCaseRateList.append(State.State(state.getState(), state.getCapitol(), state.getRegion(), state.getUHS(),
                                               state.getPopulation(), state.getCovidCases(), state.getCovidDeaths(), state.getFVR(), state.getMHI(), state.getVCR()))
        sortedDeathRateList.append(State.State(state.getState(), state.getCapitol(), state.getRegion(), state.getUHS(),
                                               state.getPopulation(), state.getCovidCases(), state.getCovidDeaths(), state.getFVR(), state.getMHI(), state.getVCR()))
        sortedMHIList.append(State.State(state.getState(), state.getCapitol(), state.getRegion(), state.getUHS(),
                                               state.getPopulation(), state.getCovidCases(), state.getCovidDeaths(), state.getFVR(), state.getMHI(), state.getVCR()))
        sortedVCRList.append(State.State(state.getState(), state.getCapitol(), state.getRegion(), state.getUHS(),
                                               state.getPopulation(), state.getCovidCases(), state.getCovidDeaths(), state.getFVR(), state.getMHI(), state.getVCR()))
        sortedFVRList.append(State.State(state.getState(), state.getCapitol(), state.getRegion(), state.getUHS(),
                                               state.getPopulation(), state.getCovidCases(), state.getCovidDeaths(), state.getFVR(), state.getMHI(), state.getVCR()))

    sortByStateName(sortedStateNameList, 0, (len(statesList)-1))
    seqStateNames = []
    for stateObj in sortedStateNameList:
        seqStateNames.append(stateObj.getState())
    mergeSort(sortedCaseRateList, 'caseRate')
    mergeSort(sortedDeathRateList, 'deathRate')
    mergeSort(sortedMHIList, 'MHI')
    mergeSort(sortedVCRList, 'VCR')
    mergeSort(sortedFVRList, 'FVR')

    x1 = "{:.3f}".format(calculateRho(
        sortedCaseRateList, sortedMHIList, seqStateNames))
    x2 = "{:.3f}".format(calculateRho(
        sortedCaseRateList, sortedVCRList, seqStateNames))
    x3 = "{:.3f}".format(calculateRho(
        sortedCaseRateList, sortedFVRList, seqStateNames))
    x4 = "{:.3f}".format(calculateRho(
        sortedDeathRateList, sortedMHIList, seqStateNames))
    x5 = "{:.3f}".format(calculateRho(
        sortedDeathRateList, sortedVCRList, seqStateNames))
    x6 = "{:.3f}".format(calculateRho(
        sortedDeathRateList, sortedFVRList, seqStateNames))
    new_line = '\n'
    separator = '-------------------------------------------------------------------------------------------------'
    matrix = f"{new_line}{separator}\
{new_line}{'|':15s}{'|':7s}{'MHI':7s}{'|':7s}{'VCR':7s}{'|':7s}{'FVR':7s}{'|'}{new_line}\
{separator}{new_line}\
{'|':3s}{'Case Rate':12s}{'|':7s}{x1:7s}{'|':7s}{x2:7s}{'|':7s}{x3:7s}{'|'}{new_line}\
{separator}{new_line}\
{'|':3s}{'Death Rate':12s}{'|':7s}{x4:7s}{'|':7s}{x5:7s}{'|':7s}{x6:7s}{'|'}{new_line}\
{separator}{new_line}"

    return matrix


def main():
    """
    main function to read in csv and create
    state objects and provide menu of 6 options
    to manipulate state object data
    :raise IOError - cannot open csv files
    """

    """
    Test getters and setters
    s1 = State.State('FL','Tally','South',100,1000,5000,3005,5.55,500,2.5151)
    print('State before:'+s1.getState())
    s1.setState('Mass')
    print('State after:'+s1.getState())

    print('Capitol before:'+s1.getCapitol())
    s1.setCapitol('New Hamp')
    print('Capitol after:'+s1.getCapitol())

    print('Region before:'+s1.getRegion())
    s1.setRegion('North')
    print('Region after:'+s1.getRegion())

    print('UHS before:',s1.getUHS())
    s1.setUHS(1)
    print('UHS after:',s1.getUHS())

    print('Population before:',s1.getPopulation())
    s1.setPopulation(2)
    print('Population after:',s1.getPopulation())

    print('Covid cases before:',s1.getCovidCases())
    s1.setCovidCases(3)
    print('Covid cases after:',s1.getCovidCases())

    print('Covid deaths before:',s1.getCovidDeaths())
    s1.setCovidDeaths(4)
    print('Covid deaths after:',s1.getCovidDeaths())

    print('Full Vaccination Rates before:',s1.getFVR())
    s1.setFVR(5.0)
    print('FVR after:',s1.getFVR())

    print('MHI before:',s1.getMHI())
    s1.setMHI(6)
    print('MHI after:',s1.getMHI())

    print('VCR before:',s1.getVCR())
    s1.setVCR(7)
    print('VCR after:',s1.getVCR())

    ***Test magic methods***

    s1 = State.State('FL','Tally','South',100,1000,5000,3005,5.55,500,2.5151)
    s2 = State.State('AL','Tally','South',100,1000,5000,3005,5.55,500,2.5151)
    if(s1>s2):
        print('s1 is greater than s2')
    else:
        print('s1 is less than s2 or equal to s2')
    print('s2 object printed',s2)
    """
    statesList = []
    try:
        file = open('States.csv', 'r')
        lines = csv.reader(file)
        for line in lines:
            if(line[0] != 'State'):
                state, capitol, region, UHS, population, covidCases, covidDeaths, FVR, MHI, VCR = [
                    line[x] for x in range(0, len(line))]
                statesList.append(State.State(
                    state, capitol, region, UHS, population, covidCases, covidDeaths, FVR, MHI, VCR))
        print('\nThere were '+str(len(statesList)) +
              ' states read from the csv.\n')
        choice = -1
        sorted = False
        while choice != '6':
            print('1. Print a state report\n2. Sort by state name\n3. Sort by case fatality rate\n4. Find and print a State for a given name\n5. Print Spearman\'s rho matrix\n6. Quit')
            choice = input('Enter a choice:')
            if(choice.isdigit() == False or int(choice) < 1 or int(choice) > 6):
                print('Invalid choice:', choice)
                print()
            else:
                if(choice == '1'):
                    printStatesReport(statesList)
                elif(choice == '2'):
                    """statesList ="""
                    sortByStateName(statesList, 0, len(statesList)-1)
                    print('States sorted by Name.\n')
                    sorted = True
                elif(choice == '3'):
                    sortByCFR(statesList)
                    print('States sorted by Case Fatality Rate\n')
                    sorted = False
                elif(choice == '4'):
                    stateToSearch = input('Enter State name:')
                    if(sorted):
                        print('Binary Search\n')
                        binarySearch(statesList, 0, len(
                            statesList)-1, stateToSearch)
                    else:
                        print('Sequential Search\n')
                        pos = sequentialSearch(statesList, stateToSearch)
                        if(pos != -1):
                            print(statesList[pos])
                        else:
                            print(stateToSearch + ' not found')
                elif(choice == '5'):
                    print(calculateSpearmanRhoMatrix(statesList))

        file.close()
    except IOError:
        print("Cannot open States.csv")


if __name__ == "__main__":
    main()
