# This file implements all of the database-related stuff

# Imports and stuff
import sqlite3

# Set up database
dbConn = sqlite3.connect("materialDatabase.db")
cursor = dbConn.cursor()
#cursor.execute("CREATE TABLE material (name TEXT, elastic_mod FLOAT, yield_str FLOAT, ult_str FLOAT, comp_str FLOAT, hardness FLOAT, mat_toughness FLOAT, fatigue_cycles INTEGER, density FLOAT, glass_trans_temp FLOAT, melting_temp FLOAT, therm_cond FLOAT, therm_exp_coeff FLOAT, elec_cond FLOAT, mat_cost_beta FLOAT)")


# Functions to add:

# Add to database

def dbAdd(name, elastic_mod, yield_str, ult_str, comp_str, hardness, mat_toughness, fatigue_cycles, density, glass_trans_temp, melting_temp, therm_cond, therm_exp_coeff, elec_cond, mat_cost_beta):
    # Note: mat_cond_beta is a beta value, handling still undecided
    cursor.execute("INSERT INTO material VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, elastic_mod, yield_str, ult_str, comp_str, hardness, mat_toughness, fatigue_cycles, density, glass_trans_temp, melting_temp, therm_cond, therm_exp_coeff, elec_cond, mat_cost_beta))
    dbConn.commit()

# Remove from database

# Read specific material value
def dbReadSingle(property, material):
    readSinglData = cursor.execute("SELECT (?) FROM (?)", (property), (material)).fetchall()
    return readSinglData

# Read all data for a material
def dbReadData(material):
    readMatData = cursor.execute("SELECT (?)", (material))
    
# Search database based on certain criteria
#  # For each data column, I will allow a search for equal to, greater than, less than, and equal to within a certain amount
#  # In the case of name, I will allow misspellings and general name searches