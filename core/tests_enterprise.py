import unittest
from core.tax_engine.calculators import *
from core.bank_parsers.parsers import *
from core.quant.indicators import TechnicalIndicators
import pandas as pd

class TestEnterpriseFeatures(unittest.TestCase):

    def test_alabama_tax_calculator(self):
        calc = AlabamaTaxCalculator()
        res = calc.calculate(100000)
        self.assertTrue(res >= 0)
        report = calc.get_full_report(50000)
        self.assertEqual(report['state'], 'Alabama')
        self.assertTrue(report['effective_rate'] >= 0)

    def test_alaska_tax_calculator(self):
        calc = AlaskaTaxCalculator()
        res = calc.calculate(100000)
        self.assertTrue(res >= 0)
        report = calc.get_full_report(50000)
        self.assertEqual(report['state'], 'Alaska')
        self.assertTrue(report['effective_rate'] >= 0)

    def test_arizona_tax_calculator(self):
        calc = ArizonaTaxCalculator()
        res = calc.calculate(100000)
        self.assertTrue(res >= 0)
        report = calc.get_full_report(50000)
        self.assertEqual(report['state'], 'Arizona')
        self.assertTrue(report['effective_rate'] >= 0)

    def test_arkansas_tax_calculator(self):
        calc = ArkansasTaxCalculator()
        res = calc.calculate(100000)
        self.assertTrue(res >= 0)
        report = calc.get_full_report(50000)
        self.assertEqual(report['state'], 'Arkansas')
        self.assertTrue(report['effective_rate'] >= 0)

    def test_california_tax_calculator(self):
        calc = CaliforniaTaxCalculator()
        res = calc.calculate(100000)
        self.assertTrue(res >= 0)
        report = calc.get_full_report(50000)
        self.assertEqual(report['state'], 'California')
        self.assertTrue(report['effective_rate'] >= 0)

    def test_colorado_tax_calculator(self):
        calc = ColoradoTaxCalculator()
        res = calc.calculate(100000)
        self.assertTrue(res >= 0)
        report = calc.get_full_report(50000)
        self.assertEqual(report['state'], 'Colorado')
        self.assertTrue(report['effective_rate'] >= 0)

    def test_connecticut_tax_calculator(self):
        calc = ConnecticutTaxCalculator()
        res = calc.calculate(100000)
        self.assertTrue(res >= 0)
        report = calc.get_full_report(50000)
        self.assertEqual(report['state'], 'Connecticut')
        self.assertTrue(report['effective_rate'] >= 0)

    def test_delaware_tax_calculator(self):
        calc = DelawareTaxCalculator()
        res = calc.calculate(100000)
        self.assertTrue(res >= 0)
        report = calc.get_full_report(50000)
        self.assertEqual(report['state'], 'Delaware')
        self.assertTrue(report['effective_rate'] >= 0)

    def test_florida_tax_calculator(self):
        calc = FloridaTaxCalculator()
        res = calc.calculate(100000)
        self.assertTrue(res >= 0)
        report = calc.get_full_report(50000)
        self.assertEqual(report['state'], 'Florida')
        self.assertTrue(report['effective_rate'] >= 0)

    def test_georgia_tax_calculator(self):
        calc = GeorgiaTaxCalculator()
        res = calc.calculate(100000)
        self.assertTrue(res >= 0)
        report = calc.get_full_report(50000)
        self.assertEqual(report['state'], 'Georgia')
        self.assertTrue(report['effective_rate'] >= 0)

    def test_quant_indicator_1(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_1(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_2(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_2(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_3(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_3(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_4(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_4(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_5(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_5(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_6(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_6(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_7(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_7(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_8(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_8(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_9(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_9(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_10(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_10(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_11(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_11(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_12(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_12(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_13(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_13(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_14(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_14(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_15(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_15(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_16(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_16(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_17(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_17(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_18(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_18(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_19(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_19(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_20(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_20(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_21(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_21(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_22(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_22(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_23(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_23(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_24(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_24(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_25(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_25(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_26(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_26(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_27(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_27(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_28(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_28(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_29(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_29(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_30(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_30(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_31(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_31(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_32(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_32(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_33(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_33(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_34(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_34(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_35(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_35(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_36(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_36(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_37(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_37(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_38(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_38(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_39(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_39(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_40(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_40(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_41(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_41(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_42(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_42(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_43(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_43(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_44(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_44(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_45(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_45(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_46(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_46(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_47(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_47(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_48(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_48(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_49(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_49(data)
        self.assertEqual(len(res), len(data))

    def test_quant_indicator_50(self):
        data = [10, 12, 15, 14, 16, 18, 20, 19, 22, 25, 24, 26, 28, 30] * 5
        res = TechnicalIndicators.custom_indicator_50(data)
        self.assertEqual(len(res), len(data))
