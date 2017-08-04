"""Docstring."""

import chamber.const as const

def k_l(temp_k):
    """Use temperature in Kelvin to obtain liquid water thermal conductivity [W/mK].

    Description: Given a tempertaure in Kelvin (between 273.15 and 373.15), return the thermal
    conductivity of pure liquid water in [W/m K]

    Positional arguments:
    temp_k -- float or int (between 273.15 and 373.15)
    """
    if temp_k >= 273.15 and temp_k <= 373.15:
        res = 0
        for idx, coeff in enumerate(const.K_L_COEFF):
            res += coeff * temp_k**idx
        return res
    else:
        raise ValueError('Please enter a temperature between 273.15 and 373.15 K.')

def c_l(temp_k):
    """Use temperature in Kelvin to obtain liquid water thermal conductivity [W/mK].

    Description: Given a tempertaure in Kelvin (between 273.15 and 373.15), return the specific
    heat of pure liquid water in [J/kg K]

    Positional arguments:
    temp_k -- float or int (between 273.15 and 373.15)
    """
    if temp_k >= 273.15 and temp_k <= 373.15:
        res = 0
        for idx, coeff in enumerate(const.C_L_COEFF):
            res += coeff * temp_k**idx
        return res
    else:
        raise ValueError('Please enter a temperature between 273.15 and 373.15 K.')

def rho_l(temp_k):
    """Use temperature in Kelvin to obtain liquid water density [kg/m^3].

    Description: Given a tempertaure in Kelvin (between 273.15 and 373.15), return the density
    of pure liquid water in [W/mK]

    Positional arguments:
    temp_k -- float or int (between 273.15 and 373.15)
    """
    if temp_k >= 273.15 and temp_k <= 373.15:
        res = 0
        for idx, coeff in enumerate(const.RHO_L_COEFF):
            res += coeff * temp_k**idx
        return res
    else:
        raise ValueError('Please enter a temperature between 273.15 and 373.15 K.')