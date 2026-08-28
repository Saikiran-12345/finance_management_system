# Advanced Tax Calculation Engine
# Contains specific brackets and rules for US States

from decimal import Decimal

class FederalTaxCalculator:
    def __init__(self, year=2024):
        self.year = year
        self.brackets = [
            (Decimal('0'), Decimal('11600'), Decimal('0.10')),
            (Decimal('11600'), Decimal('47150'), Decimal('0.12')),
            (Decimal('47150'), Decimal('100525'), Decimal('0.22')),
            (Decimal('100525'), Decimal('191950'), Decimal('0.24')),
            (Decimal('191950'), Decimal('243725'), Decimal('0.32')),
            (Decimal('243725'), Decimal('609350'), Decimal('0.35')),
            (Decimal('609350'), Decimal('Infinity'), Decimal('0.37'))
        ]
        
    def calculate(self, income):
        tax = Decimal('0')
        remaining = Decimal(str(income))
        
        for i, (lower, upper, rate) in enumerate(self.brackets):
            if remaining <= 0:
                break
            
            if upper == Decimal('Infinity'):
                taxable_in_bracket = remaining
            else:
                taxable_in_bracket = min(remaining, upper - lower)
                
            tax += taxable_in_bracket * rate
            remaining -= taxable_in_bracket
            
        return tax


class AlabamaTaxCalculator:
    """Advanced State Tax Calculator for Alabama"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('2000')
        self.personal_exemption = Decimal('1000')
        
        self.brackets = [
            (Decimal('0'), Decimal('5000'), Decimal('0.01')),
            (Decimal('5000'), Decimal('20000'), Decimal('0.02')),
            (Decimal('20000'), Decimal('50000'), Decimal('0.03')),
            (Decimal('50000'), Decimal('Infinity'), Decimal('0.04'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('0')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Alabama',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class AlaskaTaxCalculator:
    """Advanced State Tax Calculator for Alaska"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('2150')
        self.personal_exemption = Decimal('1050')
        
        self.brackets = [
            (Decimal('0'), Decimal('5100'), Decimal('0.02')),
            (Decimal('5100'), Decimal('20500'), Decimal('0.03')),
            (Decimal('20500'), Decimal('51000'), Decimal('0.04')),
            (Decimal('51000'), Decimal('Infinity'), Decimal('0.05'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('25')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Alaska',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class ArizonaTaxCalculator:
    """Advanced State Tax Calculator for Arizona"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('2300')
        self.personal_exemption = Decimal('1100')
        
        self.brackets = [
            (Decimal('0'), Decimal('5200'), Decimal('0.03')),
            (Decimal('5200'), Decimal('21000'), Decimal('0.04')),
            (Decimal('21000'), Decimal('52000'), Decimal('0.05')),
            (Decimal('52000'), Decimal('Infinity'), Decimal('0.06'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('50')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Arizona',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class ArkansasTaxCalculator:
    """Advanced State Tax Calculator for Arkansas"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('2450')
        self.personal_exemption = Decimal('1150')
        
        self.brackets = [
            (Decimal('0'), Decimal('5300'), Decimal('0.04')),
            (Decimal('5300'), Decimal('21500'), Decimal('0.05')),
            (Decimal('21500'), Decimal('53000'), Decimal('0.06')),
            (Decimal('53000'), Decimal('Infinity'), Decimal('0.07'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('75')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Arkansas',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class CaliforniaTaxCalculator:
    """Advanced State Tax Calculator for California"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('2600')
        self.personal_exemption = Decimal('1200')
        
        self.brackets = [
            (Decimal('0'), Decimal('5400'), Decimal('0.05')),
            (Decimal('5400'), Decimal('22000'), Decimal('0.06')),
            (Decimal('22000'), Decimal('54000'), Decimal('0.07')),
            (Decimal('54000'), Decimal('Infinity'), Decimal('0.08'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('100')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'California',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class ColoradoTaxCalculator:
    """Advanced State Tax Calculator for Colorado"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('2750')
        self.personal_exemption = Decimal('1250')
        
        self.brackets = [
            (Decimal('0'), Decimal('5500'), Decimal('0.01')),
            (Decimal('5500'), Decimal('22500'), Decimal('0.07')),
            (Decimal('22500'), Decimal('55000'), Decimal('0.08')),
            (Decimal('55000'), Decimal('Infinity'), Decimal('0.09'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('125')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Colorado',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class ConnecticutTaxCalculator:
    """Advanced State Tax Calculator for Connecticut"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('2900')
        self.personal_exemption = Decimal('1300')
        
        self.brackets = [
            (Decimal('0'), Decimal('5600'), Decimal('0.02')),
            (Decimal('5600'), Decimal('23000'), Decimal('0.02')),
            (Decimal('23000'), Decimal('56000'), Decimal('0.09')),
            (Decimal('56000'), Decimal('Infinity'), Decimal('0.010'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('150')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Connecticut',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class DelawareTaxCalculator:
    """Advanced State Tax Calculator for Delaware"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('3050')
        self.personal_exemption = Decimal('1350')
        
        self.brackets = [
            (Decimal('0'), Decimal('5700'), Decimal('0.03')),
            (Decimal('5700'), Decimal('23500'), Decimal('0.03')),
            (Decimal('23500'), Decimal('57000'), Decimal('0.03')),
            (Decimal('57000'), Decimal('Infinity'), Decimal('0.011'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('175')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Delaware',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class FloridaTaxCalculator:
    """Advanced State Tax Calculator for Florida"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('3200')
        self.personal_exemption = Decimal('1400')
        
        self.brackets = [
            (Decimal('0'), Decimal('5800'), Decimal('0.04')),
            (Decimal('5800'), Decimal('24000'), Decimal('0.04')),
            (Decimal('24000'), Decimal('58000'), Decimal('0.04')),
            (Decimal('58000'), Decimal('Infinity'), Decimal('0.04'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('200')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Florida',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class GeorgiaTaxCalculator:
    """Advanced State Tax Calculator for Georgia"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('3350')
        self.personal_exemption = Decimal('1450')
        
        self.brackets = [
            (Decimal('0'), Decimal('5900'), Decimal('0.05')),
            (Decimal('5900'), Decimal('24500'), Decimal('0.05')),
            (Decimal('24500'), Decimal('59000'), Decimal('0.05')),
            (Decimal('59000'), Decimal('Infinity'), Decimal('0.05'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('225')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Georgia',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class HawaiiTaxCalculator:
    """Advanced State Tax Calculator for Hawaii"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('3500')
        self.personal_exemption = Decimal('1500')
        
        self.brackets = [
            (Decimal('0'), Decimal('6000'), Decimal('0.01')),
            (Decimal('6000'), Decimal('25000'), Decimal('0.06')),
            (Decimal('25000'), Decimal('60000'), Decimal('0.06')),
            (Decimal('60000'), Decimal('Infinity'), Decimal('0.06'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('250')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Hawaii',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class IdahoTaxCalculator:
    """Advanced State Tax Calculator for Idaho"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('3650')
        self.personal_exemption = Decimal('1550')
        
        self.brackets = [
            (Decimal('0'), Decimal('6100'), Decimal('0.02')),
            (Decimal('6100'), Decimal('25500'), Decimal('0.07')),
            (Decimal('25500'), Decimal('61000'), Decimal('0.07')),
            (Decimal('61000'), Decimal('Infinity'), Decimal('0.07'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('275')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Idaho',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class IllinoisTaxCalculator:
    """Advanced State Tax Calculator for Illinois"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('3800')
        self.personal_exemption = Decimal('1600')
        
        self.brackets = [
            (Decimal('0'), Decimal('6200'), Decimal('0.03')),
            (Decimal('6200'), Decimal('26000'), Decimal('0.02')),
            (Decimal('26000'), Decimal('62000'), Decimal('0.08')),
            (Decimal('62000'), Decimal('Infinity'), Decimal('0.08'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('300')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Illinois',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class IndianaTaxCalculator:
    """Advanced State Tax Calculator for Indiana"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('3950')
        self.personal_exemption = Decimal('1650')
        
        self.brackets = [
            (Decimal('0'), Decimal('6300'), Decimal('0.04')),
            (Decimal('6300'), Decimal('26500'), Decimal('0.03')),
            (Decimal('26500'), Decimal('63000'), Decimal('0.09')),
            (Decimal('63000'), Decimal('Infinity'), Decimal('0.09'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('325')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Indiana',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class IowaTaxCalculator:
    """Advanced State Tax Calculator for Iowa"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('4100')
        self.personal_exemption = Decimal('1700')
        
        self.brackets = [
            (Decimal('0'), Decimal('6400'), Decimal('0.05')),
            (Decimal('6400'), Decimal('27000'), Decimal('0.04')),
            (Decimal('27000'), Decimal('64000'), Decimal('0.03')),
            (Decimal('64000'), Decimal('Infinity'), Decimal('0.010'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('350')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Iowa',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class KansasTaxCalculator:
    """Advanced State Tax Calculator for Kansas"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('4250')
        self.personal_exemption = Decimal('1750')
        
        self.brackets = [
            (Decimal('0'), Decimal('6500'), Decimal('0.01')),
            (Decimal('6500'), Decimal('27500'), Decimal('0.05')),
            (Decimal('27500'), Decimal('65000'), Decimal('0.04')),
            (Decimal('65000'), Decimal('Infinity'), Decimal('0.011'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('375')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Kansas',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class KentuckyTaxCalculator:
    """Advanced State Tax Calculator for Kentucky"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('4400')
        self.personal_exemption = Decimal('1800')
        
        self.brackets = [
            (Decimal('0'), Decimal('6600'), Decimal('0.02')),
            (Decimal('6600'), Decimal('28000'), Decimal('0.06')),
            (Decimal('28000'), Decimal('66000'), Decimal('0.05')),
            (Decimal('66000'), Decimal('Infinity'), Decimal('0.04'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('400')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Kentucky',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class LouisianaTaxCalculator:
    """Advanced State Tax Calculator for Louisiana"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('4550')
        self.personal_exemption = Decimal('1850')
        
        self.brackets = [
            (Decimal('0'), Decimal('6700'), Decimal('0.03')),
            (Decimal('6700'), Decimal('28500'), Decimal('0.07')),
            (Decimal('28500'), Decimal('67000'), Decimal('0.06')),
            (Decimal('67000'), Decimal('Infinity'), Decimal('0.05'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('425')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Louisiana',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class MaineTaxCalculator:
    """Advanced State Tax Calculator for Maine"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('4700')
        self.personal_exemption = Decimal('1900')
        
        self.brackets = [
            (Decimal('0'), Decimal('6800'), Decimal('0.04')),
            (Decimal('6800'), Decimal('29000'), Decimal('0.02')),
            (Decimal('29000'), Decimal('68000'), Decimal('0.07')),
            (Decimal('68000'), Decimal('Infinity'), Decimal('0.06'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('450')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Maine',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class MarylandTaxCalculator:
    """Advanced State Tax Calculator for Maryland"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('4850')
        self.personal_exemption = Decimal('1950')
        
        self.brackets = [
            (Decimal('0'), Decimal('6900'), Decimal('0.05')),
            (Decimal('6900'), Decimal('29500'), Decimal('0.03')),
            (Decimal('29500'), Decimal('69000'), Decimal('0.08')),
            (Decimal('69000'), Decimal('Infinity'), Decimal('0.07'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('475')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Maryland',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class MassachusettsTaxCalculator:
    """Advanced State Tax Calculator for Massachusetts"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('5000')
        self.personal_exemption = Decimal('2000')
        
        self.brackets = [
            (Decimal('0'), Decimal('7000'), Decimal('0.01')),
            (Decimal('7000'), Decimal('30000'), Decimal('0.04')),
            (Decimal('30000'), Decimal('70000'), Decimal('0.09')),
            (Decimal('70000'), Decimal('Infinity'), Decimal('0.08'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('500')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Massachusetts',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class MichiganTaxCalculator:
    """Advanced State Tax Calculator for Michigan"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('5150')
        self.personal_exemption = Decimal('2050')
        
        self.brackets = [
            (Decimal('0'), Decimal('7100'), Decimal('0.02')),
            (Decimal('7100'), Decimal('30500'), Decimal('0.05')),
            (Decimal('30500'), Decimal('71000'), Decimal('0.03')),
            (Decimal('71000'), Decimal('Infinity'), Decimal('0.09'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('525')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Michigan',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class MinnesotaTaxCalculator:
    """Advanced State Tax Calculator for Minnesota"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('5300')
        self.personal_exemption = Decimal('2100')
        
        self.brackets = [
            (Decimal('0'), Decimal('7200'), Decimal('0.03')),
            (Decimal('7200'), Decimal('31000'), Decimal('0.06')),
            (Decimal('31000'), Decimal('72000'), Decimal('0.04')),
            (Decimal('72000'), Decimal('Infinity'), Decimal('0.010'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('550')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Minnesota',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class MississippiTaxCalculator:
    """Advanced State Tax Calculator for Mississippi"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('5450')
        self.personal_exemption = Decimal('2150')
        
        self.brackets = [
            (Decimal('0'), Decimal('7300'), Decimal('0.04')),
            (Decimal('7300'), Decimal('31500'), Decimal('0.07')),
            (Decimal('31500'), Decimal('73000'), Decimal('0.05')),
            (Decimal('73000'), Decimal('Infinity'), Decimal('0.011'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('575')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Mississippi',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class MissouriTaxCalculator:
    """Advanced State Tax Calculator for Missouri"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('5600')
        self.personal_exemption = Decimal('2200')
        
        self.brackets = [
            (Decimal('0'), Decimal('7400'), Decimal('0.05')),
            (Decimal('7400'), Decimal('32000'), Decimal('0.02')),
            (Decimal('32000'), Decimal('74000'), Decimal('0.06')),
            (Decimal('74000'), Decimal('Infinity'), Decimal('0.04'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('600')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Missouri',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class MontanaTaxCalculator:
    """Advanced State Tax Calculator for Montana"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('5750')
        self.personal_exemption = Decimal('2250')
        
        self.brackets = [
            (Decimal('0'), Decimal('7500'), Decimal('0.01')),
            (Decimal('7500'), Decimal('32500'), Decimal('0.03')),
            (Decimal('32500'), Decimal('75000'), Decimal('0.07')),
            (Decimal('75000'), Decimal('Infinity'), Decimal('0.05'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('625')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Montana',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class NebraskaTaxCalculator:
    """Advanced State Tax Calculator for Nebraska"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('5900')
        self.personal_exemption = Decimal('2300')
        
        self.brackets = [
            (Decimal('0'), Decimal('7600'), Decimal('0.02')),
            (Decimal('7600'), Decimal('33000'), Decimal('0.04')),
            (Decimal('33000'), Decimal('76000'), Decimal('0.08')),
            (Decimal('76000'), Decimal('Infinity'), Decimal('0.06'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('650')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Nebraska',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class NevadaTaxCalculator:
    """Advanced State Tax Calculator for Nevada"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('6050')
        self.personal_exemption = Decimal('2350')
        
        self.brackets = [
            (Decimal('0'), Decimal('7700'), Decimal('0.03')),
            (Decimal('7700'), Decimal('33500'), Decimal('0.05')),
            (Decimal('33500'), Decimal('77000'), Decimal('0.09')),
            (Decimal('77000'), Decimal('Infinity'), Decimal('0.07'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('675')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Nevada',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class NewHampshireTaxCalculator:
    """Advanced State Tax Calculator for NewHampshire"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('6200')
        self.personal_exemption = Decimal('2400')
        
        self.brackets = [
            (Decimal('0'), Decimal('7800'), Decimal('0.04')),
            (Decimal('7800'), Decimal('34000'), Decimal('0.06')),
            (Decimal('34000'), Decimal('78000'), Decimal('0.03')),
            (Decimal('78000'), Decimal('Infinity'), Decimal('0.08'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('700')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'NewHampshire',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class NewJerseyTaxCalculator:
    """Advanced State Tax Calculator for NewJersey"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('6350')
        self.personal_exemption = Decimal('2450')
        
        self.brackets = [
            (Decimal('0'), Decimal('7900'), Decimal('0.05')),
            (Decimal('7900'), Decimal('34500'), Decimal('0.07')),
            (Decimal('34500'), Decimal('79000'), Decimal('0.04')),
            (Decimal('79000'), Decimal('Infinity'), Decimal('0.09'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('725')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'NewJersey',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class NewMexicoTaxCalculator:
    """Advanced State Tax Calculator for NewMexico"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('6500')
        self.personal_exemption = Decimal('2500')
        
        self.brackets = [
            (Decimal('0'), Decimal('8000'), Decimal('0.01')),
            (Decimal('8000'), Decimal('35000'), Decimal('0.02')),
            (Decimal('35000'), Decimal('80000'), Decimal('0.05')),
            (Decimal('80000'), Decimal('Infinity'), Decimal('0.010'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('750')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'NewMexico',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class NewYorkTaxCalculator:
    """Advanced State Tax Calculator for NewYork"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('6650')
        self.personal_exemption = Decimal('2550')
        
        self.brackets = [
            (Decimal('0'), Decimal('8100'), Decimal('0.02')),
            (Decimal('8100'), Decimal('35500'), Decimal('0.03')),
            (Decimal('35500'), Decimal('81000'), Decimal('0.06')),
            (Decimal('81000'), Decimal('Infinity'), Decimal('0.011'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('775')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'NewYork',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class NorthCarolinaTaxCalculator:
    """Advanced State Tax Calculator for NorthCarolina"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('6800')
        self.personal_exemption = Decimal('2600')
        
        self.brackets = [
            (Decimal('0'), Decimal('8200'), Decimal('0.03')),
            (Decimal('8200'), Decimal('36000'), Decimal('0.04')),
            (Decimal('36000'), Decimal('82000'), Decimal('0.07')),
            (Decimal('82000'), Decimal('Infinity'), Decimal('0.04'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('800')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'NorthCarolina',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class NorthDakotaTaxCalculator:
    """Advanced State Tax Calculator for NorthDakota"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('6950')
        self.personal_exemption = Decimal('2650')
        
        self.brackets = [
            (Decimal('0'), Decimal('8300'), Decimal('0.04')),
            (Decimal('8300'), Decimal('36500'), Decimal('0.05')),
            (Decimal('36500'), Decimal('83000'), Decimal('0.08')),
            (Decimal('83000'), Decimal('Infinity'), Decimal('0.05'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('825')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'NorthDakota',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class OhioTaxCalculator:
    """Advanced State Tax Calculator for Ohio"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('7100')
        self.personal_exemption = Decimal('2700')
        
        self.brackets = [
            (Decimal('0'), Decimal('8400'), Decimal('0.05')),
            (Decimal('8400'), Decimal('37000'), Decimal('0.06')),
            (Decimal('37000'), Decimal('84000'), Decimal('0.09')),
            (Decimal('84000'), Decimal('Infinity'), Decimal('0.06'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('850')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Ohio',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class OklahomaTaxCalculator:
    """Advanced State Tax Calculator for Oklahoma"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('7250')
        self.personal_exemption = Decimal('2750')
        
        self.brackets = [
            (Decimal('0'), Decimal('8500'), Decimal('0.01')),
            (Decimal('8500'), Decimal('37500'), Decimal('0.07')),
            (Decimal('37500'), Decimal('85000'), Decimal('0.03')),
            (Decimal('85000'), Decimal('Infinity'), Decimal('0.07'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('875')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Oklahoma',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class OregonTaxCalculator:
    """Advanced State Tax Calculator for Oregon"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('7400')
        self.personal_exemption = Decimal('2800')
        
        self.brackets = [
            (Decimal('0'), Decimal('8600'), Decimal('0.02')),
            (Decimal('8600'), Decimal('38000'), Decimal('0.02')),
            (Decimal('38000'), Decimal('86000'), Decimal('0.04')),
            (Decimal('86000'), Decimal('Infinity'), Decimal('0.08'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('900')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Oregon',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class PennsylvaniaTaxCalculator:
    """Advanced State Tax Calculator for Pennsylvania"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('7550')
        self.personal_exemption = Decimal('2850')
        
        self.brackets = [
            (Decimal('0'), Decimal('8700'), Decimal('0.03')),
            (Decimal('8700'), Decimal('38500'), Decimal('0.03')),
            (Decimal('38500'), Decimal('87000'), Decimal('0.05')),
            (Decimal('87000'), Decimal('Infinity'), Decimal('0.09'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('925')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Pennsylvania',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class RhodeIslandTaxCalculator:
    """Advanced State Tax Calculator for RhodeIsland"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('7700')
        self.personal_exemption = Decimal('2900')
        
        self.brackets = [
            (Decimal('0'), Decimal('8800'), Decimal('0.04')),
            (Decimal('8800'), Decimal('39000'), Decimal('0.04')),
            (Decimal('39000'), Decimal('88000'), Decimal('0.06')),
            (Decimal('88000'), Decimal('Infinity'), Decimal('0.010'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('950')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'RhodeIsland',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class SouthCarolinaTaxCalculator:
    """Advanced State Tax Calculator for SouthCarolina"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('7850')
        self.personal_exemption = Decimal('2950')
        
        self.brackets = [
            (Decimal('0'), Decimal('8900'), Decimal('0.05')),
            (Decimal('8900'), Decimal('39500'), Decimal('0.05')),
            (Decimal('39500'), Decimal('89000'), Decimal('0.07')),
            (Decimal('89000'), Decimal('Infinity'), Decimal('0.011'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('975')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'SouthCarolina',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class SouthDakotaTaxCalculator:
    """Advanced State Tax Calculator for SouthDakota"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('8000')
        self.personal_exemption = Decimal('3000')
        
        self.brackets = [
            (Decimal('0'), Decimal('9000'), Decimal('0.01')),
            (Decimal('9000'), Decimal('40000'), Decimal('0.06')),
            (Decimal('40000'), Decimal('90000'), Decimal('0.08')),
            (Decimal('90000'), Decimal('Infinity'), Decimal('0.04'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('1000')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'SouthDakota',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class TennesseeTaxCalculator:
    """Advanced State Tax Calculator for Tennessee"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('8150')
        self.personal_exemption = Decimal('3050')
        
        self.brackets = [
            (Decimal('0'), Decimal('9100'), Decimal('0.02')),
            (Decimal('9100'), Decimal('40500'), Decimal('0.07')),
            (Decimal('40500'), Decimal('91000'), Decimal('0.09')),
            (Decimal('91000'), Decimal('Infinity'), Decimal('0.05'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('1025')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Tennessee',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class TexasTaxCalculator:
    """Advanced State Tax Calculator for Texas"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('8300')
        self.personal_exemption = Decimal('3100')
        
        self.brackets = [
            (Decimal('0'), Decimal('9200'), Decimal('0.03')),
            (Decimal('9200'), Decimal('41000'), Decimal('0.02')),
            (Decimal('41000'), Decimal('92000'), Decimal('0.03')),
            (Decimal('92000'), Decimal('Infinity'), Decimal('0.06'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('1050')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Texas',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class UtahTaxCalculator:
    """Advanced State Tax Calculator for Utah"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('8450')
        self.personal_exemption = Decimal('3150')
        
        self.brackets = [
            (Decimal('0'), Decimal('9300'), Decimal('0.04')),
            (Decimal('9300'), Decimal('41500'), Decimal('0.03')),
            (Decimal('41500'), Decimal('93000'), Decimal('0.04')),
            (Decimal('93000'), Decimal('Infinity'), Decimal('0.07'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('1075')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Utah',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class VermontTaxCalculator:
    """Advanced State Tax Calculator for Vermont"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('8600')
        self.personal_exemption = Decimal('3200')
        
        self.brackets = [
            (Decimal('0'), Decimal('9400'), Decimal('0.05')),
            (Decimal('9400'), Decimal('42000'), Decimal('0.04')),
            (Decimal('42000'), Decimal('94000'), Decimal('0.05')),
            (Decimal('94000'), Decimal('Infinity'), Decimal('0.08'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('1100')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Vermont',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class VirginiaTaxCalculator:
    """Advanced State Tax Calculator for Virginia"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('8750')
        self.personal_exemption = Decimal('3250')
        
        self.brackets = [
            (Decimal('0'), Decimal('9500'), Decimal('0.01')),
            (Decimal('9500'), Decimal('42500'), Decimal('0.05')),
            (Decimal('42500'), Decimal('95000'), Decimal('0.06')),
            (Decimal('95000'), Decimal('Infinity'), Decimal('0.09'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('1125')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Virginia',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class WashingtonTaxCalculator:
    """Advanced State Tax Calculator for Washington"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('8900')
        self.personal_exemption = Decimal('3300')
        
        self.brackets = [
            (Decimal('0'), Decimal('9600'), Decimal('0.02')),
            (Decimal('9600'), Decimal('43000'), Decimal('0.06')),
            (Decimal('43000'), Decimal('96000'), Decimal('0.07')),
            (Decimal('96000'), Decimal('Infinity'), Decimal('0.010'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('1150')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Washington',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class WestVirginiaTaxCalculator:
    """Advanced State Tax Calculator for WestVirginia"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('9050')
        self.personal_exemption = Decimal('3350')
        
        self.brackets = [
            (Decimal('0'), Decimal('9700'), Decimal('0.03')),
            (Decimal('9700'), Decimal('43500'), Decimal('0.07')),
            (Decimal('43500'), Decimal('97000'), Decimal('0.08')),
            (Decimal('97000'), Decimal('Infinity'), Decimal('0.011'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('1175')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'WestVirginia',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class WisconsinTaxCalculator:
    """Advanced State Tax Calculator for Wisconsin"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('9200')
        self.personal_exemption = Decimal('3400')
        
        self.brackets = [
            (Decimal('0'), Decimal('9800'), Decimal('0.04')),
            (Decimal('9800'), Decimal('44000'), Decimal('0.02')),
            (Decimal('44000'), Decimal('98000'), Decimal('0.09')),
            (Decimal('98000'), Decimal('Infinity'), Decimal('0.04'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('1200')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Wisconsin',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }

class WyomingTaxCalculator:
    """Advanced State Tax Calculator for Wyoming"""
    def __init__(self, filing_status='single'):
        self.filing_status = filing_status
        self.standard_deduction = Decimal('9350')
        self.personal_exemption = Decimal('3450')
        
        self.brackets = [
            (Decimal('0'), Decimal('9900'), Decimal('0.05')),
            (Decimal('9900'), Decimal('44500'), Decimal('0.03')),
            (Decimal('44500'), Decimal('99000'), Decimal('0.03')),
            (Decimal('99000'), Decimal('Infinity'), Decimal('0.05'))
        ]
        
    def get_effective_rate(self, income):
        tax = self.calculate(income)
        if income > 0:
            return tax / Decimal(str(income))
        return Decimal('0')
        
    def calculate(self, gross_income):
        gross = Decimal(str(gross_income))
        adjusted_gross = gross - self.standard_deduction - self.personal_exemption
        if adjusted_gross <= 0:
            return Decimal('0')
            
        tax = Decimal('0')
        remaining = adjusted_gross
        
        for lower, upper, rate in self.brackets:
            if remaining <= 0:
                break
                
            if upper == Decimal('Infinity'):
                taxable = remaining
            else:
                taxable = min(remaining, upper - lower)
                
            tax += taxable * rate
            remaining -= taxable
            
        state_credit = Decimal('1225')
        return max(Decimal('0'), tax - state_credit)
        
    def get_full_report(self, gross_income):
        return {
            'state': 'Wyoming',
            'gross_income': gross_income,
            'tax_liability': self.calculate(gross_income),
            'effective_rate': self.get_effective_rate(gross_income),
            'standard_deduction': self.standard_deduction,
            'personal_exemption': self.personal_exemption
        }
