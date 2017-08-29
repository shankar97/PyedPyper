"""
Definition of models.
"""

from django.db import models

# Create your models here.


class ElementarySchool(models.Model):
    # choice limits?
    name = models.CharField(max_length=25)
    community = models.CharField(max_length=25)
    zipCode = models.IntegerField()
    adequateProgress = models.NullBooleanField(blank=True, null=True, default=None)
    standardTrack = models.NullBooleanField(blank=True, null=True, default=None) # if true, standard, if false, track E
    performanceProbation = models.NullBooleanField(blank=True, null=True, default=None)
    performanceLevel = models.IntegerField(default=-1) # level -1 is NDA
    healthySchool = models.NullBooleanField(blank=True, null=True, default=None)
    safetyScore = models.IntegerField(default=-1) # change strength into number rankings
    familyInvolvementScore = models.IntegerField(default=-1)
    environmentScore = models.IntegerField(default=-1)
    instructionScore = models.IntegerField(default=-1)
    leadersScore = models.IntegerField(default=-1)
    teachersScore = models.IntegerField(default=-1)
    parentEngagementScore = models.IntegerField(default=-1)
    parentEnvironmentScore = models.IntegerField(default=-1)
    studentAttendance = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    misconductRate = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5) # per 100
    teacherAttendance = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    individualizedEducation = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    pk2Lit = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    pk2Math = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    gr3to5Math = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    gr3to5Reading = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    gr3to5MathPace = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    gr3to5ReadingPace = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    gr6to8Math = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    gr6to8Reading = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    gr6to8MathPace = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    gr6to8ReadingPace = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    gr8MathExplore = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    gr8ReadingExplore = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    isatMathExceed = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    isatReadingExceed = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    isatMathAdd = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    isatReadingAdd = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    algebraPercentTake = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    algebraPercentPass = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    collegeEnroll = models.IntegerField(default=-1)
    generalServices = models.IntegerField(default=-1)
    studentTotal = models.IntegerField(default=-1)
    studentLowIncome = models.IntegerField(default=-1)
    studentSpecialEd = models.IntegerField(default=-1)
    studentEnglishLearners = models.IntegerField(default=-1)
    studentBlack = models.IntegerField(default=-1)
    studentHispanic = models.IntegerField(default=-1)
    studentWhite = models.IntegerField(default=-1)
    studentAsian = models.IntegerField(default=-1)
    studentNativeAmerican = models.IntegerField(default=-1)
    studentOther = models.IntegerField(default=-1)
    studentAsianPacificIslander = models.IntegerField(default=-1)
    studentMulti = models.IntegerField(default=-1)
    studentHawaiian = models.IntegerField(default=-1)
    studentNDA = models.IntegerField(default=-1)


class HighSchool(models.Model):
    # choice limits?
    name = models.CharField(max_length=25)
    community = models.CharField(max_length=25)
    zipCode = models.IntegerField()
    adequateProgress = models.NullBooleanField(blank=True, null=True, default=None)
    standardTrack = models.NullBooleanField(blank=True, null=True, default=None) # if true, standard, if false, track E
    performanceProbation = models.NullBooleanField(blank=True, null=True, default=None)
    performanceLevel = models.IntegerField(default=-1) # level -1 is NDA
    healthySchool = models.NullBooleanField(blank=True, null=True, default=None)
    safetyScore = models.IntegerField(default=-1) # change strength into number rankings
    familyInvolvementScore = models.IntegerField(default=-1)
    environmentScore = models.IntegerField(default=-1)
    instructionScore = models.IntegerField(default=-1)
    leadersScore = models.IntegerField(default=-1)
    teachersScore = models.IntegerField(default=-1)
    parentEngagementScore = models.IntegerField(default=-1)
    parentEnvironmentScore = models.IntegerField(default=-1)
    studentAttendance = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    misconductRate = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5) # per 100
    teacherAttendance = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    individualizedEducation = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    isatMathExceed = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    isatReadingExceed = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    isatMathAdd = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    isatReadingAdd = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    algebraPercentTake = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    algebraPercentPass = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    collegeEnroll = models.IntegerField(default=-1)
    generalServices = models.IntegerField(default=-1)
    explore2009 = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    explore2010 = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    plan2009 = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    plan2010 = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    netExplorePlan = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    act2011 = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    netPlanAct = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    collegeEligibility = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    gradRate = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    collegeEnrollRate = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    freshmanTrack = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    studentTotal = models.IntegerField(default=-1)
    studentLowIncome = models.IntegerField(default=-1)
    studentSpecialEd = models.IntegerField(default=-1)
    studentEnglishLearners = models.IntegerField(default=-1)
    studentBlack = models.IntegerField(default=-1)
    studentHispanic = models.IntegerField(default=-1)
    studentWhite = models.IntegerField(default=-1)
    studentAsian = models.IntegerField(default=-1)
    studentNativeAmerican = models.IntegerField(default=-1)
    studentOther = models.IntegerField(default=-1)
    studentAsianPacificIslander = models.IntegerField(default=-1)
    studentMulti = models.IntegerField(default=-1)
    studentHawaiian = models.IntegerField(default=-1)
    studentNDA = models.IntegerField(default=-1)


class Community(models.Model):
    name = models.CharField(max_length=25)
    percentHousingCrowded = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    percentHouseholdPoverty = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    percentAge16Unemployed = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    percentAge25NoDiploma = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    percentUnder18Over64 = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    perCapitaIncome = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    hardshipIndex = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    lifeExpectancy1990 = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    lifeLower1990 = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    lifeUpper1990 = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    lifeExpectancy2000 = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    lifeLower2000 = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    lifeUpper2000 = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    lifeExpectancy2010 = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    lifeLower2010 = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)
    lifeUpper2010 = models.DecimalField(default=-1, decimal_places = 4, max_digits = 5)

    # there doesn't need to be a ward number since that's just the ID.

