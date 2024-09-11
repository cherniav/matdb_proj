# WCMC Materials Tool

## Overview
<p>The goal of this tool is to provide a modular and easy-to-use tool to browse and compare materials. 

Materials selection and mechanical optimization is already hard enough. Tools should make it easier, not more annoying.
</p>

## Units
<p>Units will be stored EXCLUSIVELY in base and derived SI units. Mixing units and recording values with prefixes needlessly invites silly error nonsense. Therefore, any case which requires unit prefixes (For example, kPa instead of Pa) will be a conversion rather than a direct display of the stored value (Pa in this example).
</p>

## The Database
<p>
To store data, I implemented an SQLite 3 database locally for simplicity and speed of implementation. For the future, the idea is to eventually have a centralized database for many users to be able to collaborate and contribute to it.

To communicate between the app and the database to retrieve values, to futureproof, I built an API that can be swapped later on. (NOT IMPLEMENTED YET)
</p>

#### Data Format
<p>The point of the database is to store material data in an obvious and retrievable format. The format looks like this:
</p>

**Properties**
- Elastic Modulus E (Pa)
- Yield Strength (Pa, Tensile)
- Ultimate Strength (Pa, Tensile)
- Compressive Strength (Pa)
- Hardness (Rockwell)
- Material Toughness (J/m<sup>3</sup>) (area under stress-strain curve)
- Fatigue (Cycles to failure)
- Density (g/m<sup>3</sup>)
- Glass Transition Temp (C)
- Melting Temp (C)
- Thermal Conductivity (Wm<sup>-1</sup>K<sup>-1</sup>)
- Thermal Expansion Coefficient ( (m/m)/ <sup>o</sup>C )
- Electrical Conductivity (Siemens / Meter)
- Raw Material Cost (USD/m^3) [not implemented yet] (NEED TO THINK ABOUT THIS A BIT BECAUSE ITS HARD TO QUANTIFY WITHOUT MFG CONSIDERATIONS) (this will need to be updated frequently)