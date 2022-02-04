"""
State.py - Define state object and methods

Author: Andrews Peter
Version: 1/30/22
Email: n01364109@unf.edu
"""
class State:
    """
    Defines state object, provides
    methods to get, set, and compare
    states
    """
    def __init__(self,state,capitol,region,UHS,population,covidCases,covidDeaths,FVR,MHI,VCR):
        """
        Initialize State object with these parameters
        :param state - name of state
        :param capitol - capital of given state
        :param region - region of US where state is
        :param UHS - US House Seats of given state
        :param population - population of state
        :param covidCases - number of covid cases in state
        :param covidDeaths - number of covid deaths in state
        :param FVR - Full Vaccination Rates
        :param MHI - Median Household Income
        :param VCR - Violent Crime Rates
        """
        self.state = state
        self.capitol = capitol
        self.region = region
        self.UHS = UHS
        self.population = population
        self.covidCases = covidCases
        self.covidDeaths = covidDeaths
        self.FVR = float(FVR)
        self.MHI = int(MHI)
        self.VCR = float(VCR)
        self.caseRate = (int(covidCases)/int(population))*100000
        self.deathRate = (int(covidDeaths)/int(population))*100000
        self.CFR = int(self.getCovidDeaths())/int(self.getCovidCases())

    def getState(self):
        """
        :return name of state
        """
        return self.state

    def setState(self, state):
        """
        set name of state
        :param state - name of state
        """
        self.state = state

    def getCapitol(self):
        """
        Get name of capital of state
        """
        return self.capitol

    def setCapitol(self, capitol):
        """
        Set name of capitol of state
        :param capitol - name of capitol
        """
        self.capitol = capitol

    def getRegion(self):
        """
        :return name of region of state
        """
        return self.region

    def setRegion(self, region):
        """
        :param region - region of state
        """
        self.region = region

    def getUHS(self):
        """
        :return int US House Seats of state
        """
        return self.UHS

    def setUHS(self, UHS):
        """
        :param UHS - US House Seats
        """
        self.UHS = UHS

    def getPopulation(self):
        """
        :return int population
        """
        return self.population

    def setPopulation(self, population):
        """
        :param population - population of each state
        self.population = population
        """
        self.population = population

    def getCovidCases(self):
        """
        :return int number of covid cases in state
        """
        return self.covidCases

    def setCovidCases(self, covidCases):
        """
        :param - int number of covidCases
        """
        self.covidCases = covidCases

    def getCovidDeaths(self):
        """
        :return int of covid deaths in state
        """
        return self.covidDeaths

    def setCovidDeaths(self, covidDeaths):
        """
        :param covidDeaths in each state
        """
        self.covidDeaths = covidDeaths

    def getFVR(self):
        """
        :return Full Vaccination Rates
        """
        return "{:.3f}".format(float(self.FVR)/100)

    def setFVR(self, FVR):
        """
        :param FVR - full vaccination rates
        """
        self.FVR = FVR

    def getMHI(self):
        """
        :return Median Household Income int
        """
        return str(self.MHI)

    def setMHI(self, MHI):
        """
        :param MHI - median household income
        """
        self.MHI = MHI

    def getVCR(self):
        """
        :return violent crime rates
        """
        return str(self.VCR)

    def setVCR(self, VCR):
        """
        :param VCR - violent crime rates of this state
        """
        self.VCR = VCR

    def getCaseRate(self):
        """
        :return (#covid cases/state population)*100000
        """
        return "{:.2f}".format(self.caseRate)

    def getDeathRate(self):
        """
        :return (#covid deaths/state population)*100000
        """
        return "{:.2f}".format(self.deathRate)

    def getCFR(self):
        """
        :return covid fatality rate
        """
        return "{:.6f}".format(self.CFR)

    def __gt__(s1, s2):
        """
        :return - boolean if s1.getState is greater
        lexigographically than s2.getState:
            return True else: return False
        """
        if s1.getState() > s2.getState():
            return True
        else:
            return False

    def __str__(self):
        """
        :return string of state object
        """
        new_line = '\n'
        string = f"{'Name:':15s}{self.getState()}{new_line}{'MHI:':15s}{self.getMHI()}{new_line}{'VCR:':15s}{self.getVCR()}{new_line}{'CFR:':15s}{self.getCFR()}{new_line}{'Case Rate:':15s}{self.getCaseRate()}{new_line}{'Death Rate:':15s}{self.getDeathRate()}{new_line}{'FV Rate:':15s}{self.getFVR()}{new_line}"
        return string







