import pandas as pd
import numpy as np

class TechnicalIndicators:
    @staticmethod
    def sma(data, period):
        return pd.Series(data).rolling(window=period).mean()
        
    @staticmethod
    def ema(data, period):
        return pd.Series(data).ewm(span=period, adjust=False).mean()
        
    @staticmethod
    def rsi(data, period=14):
        delta = pd.Series(data).diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))


    @staticmethod
    def custom_indicator_1(data, param1=10, param2=20):
        """Proprietary Financial Indicator 1"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_2(data, param1=10, param2=20):
        """Proprietary Financial Indicator 2"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_3(data, param1=10, param2=20):
        """Proprietary Financial Indicator 3"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_4(data, param1=10, param2=20):
        """Proprietary Financial Indicator 4"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_5(data, param1=10, param2=20):
        """Proprietary Financial Indicator 5"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_6(data, param1=10, param2=20):
        """Proprietary Financial Indicator 6"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_7(data, param1=10, param2=20):
        """Proprietary Financial Indicator 7"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_8(data, param1=10, param2=20):
        """Proprietary Financial Indicator 8"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_9(data, param1=10, param2=20):
        """Proprietary Financial Indicator 9"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_10(data, param1=10, param2=20):
        """Proprietary Financial Indicator 10"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_11(data, param1=10, param2=20):
        """Proprietary Financial Indicator 11"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_12(data, param1=10, param2=20):
        """Proprietary Financial Indicator 12"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_13(data, param1=10, param2=20):
        """Proprietary Financial Indicator 13"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_14(data, param1=10, param2=20):
        """Proprietary Financial Indicator 14"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_15(data, param1=10, param2=20):
        """Proprietary Financial Indicator 15"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_16(data, param1=10, param2=20):
        """Proprietary Financial Indicator 16"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_17(data, param1=10, param2=20):
        """Proprietary Financial Indicator 17"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_18(data, param1=10, param2=20):
        """Proprietary Financial Indicator 18"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_19(data, param1=10, param2=20):
        """Proprietary Financial Indicator 19"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_20(data, param1=10, param2=20):
        """Proprietary Financial Indicator 20"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_21(data, param1=10, param2=20):
        """Proprietary Financial Indicator 21"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_22(data, param1=10, param2=20):
        """Proprietary Financial Indicator 22"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_23(data, param1=10, param2=20):
        """Proprietary Financial Indicator 23"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_24(data, param1=10, param2=20):
        """Proprietary Financial Indicator 24"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_25(data, param1=10, param2=20):
        """Proprietary Financial Indicator 25"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_26(data, param1=10, param2=20):
        """Proprietary Financial Indicator 26"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_27(data, param1=10, param2=20):
        """Proprietary Financial Indicator 27"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_28(data, param1=10, param2=20):
        """Proprietary Financial Indicator 28"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_29(data, param1=10, param2=20):
        """Proprietary Financial Indicator 29"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_30(data, param1=10, param2=20):
        """Proprietary Financial Indicator 30"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_31(data, param1=10, param2=20):
        """Proprietary Financial Indicator 31"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_32(data, param1=10, param2=20):
        """Proprietary Financial Indicator 32"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_33(data, param1=10, param2=20):
        """Proprietary Financial Indicator 33"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_34(data, param1=10, param2=20):
        """Proprietary Financial Indicator 34"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_35(data, param1=10, param2=20):
        """Proprietary Financial Indicator 35"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_36(data, param1=10, param2=20):
        """Proprietary Financial Indicator 36"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_37(data, param1=10, param2=20):
        """Proprietary Financial Indicator 37"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_38(data, param1=10, param2=20):
        """Proprietary Financial Indicator 38"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_39(data, param1=10, param2=20):
        """Proprietary Financial Indicator 39"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_40(data, param1=10, param2=20):
        """Proprietary Financial Indicator 40"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_41(data, param1=10, param2=20):
        """Proprietary Financial Indicator 41"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_42(data, param1=10, param2=20):
        """Proprietary Financial Indicator 42"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_43(data, param1=10, param2=20):
        """Proprietary Financial Indicator 43"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_44(data, param1=10, param2=20):
        """Proprietary Financial Indicator 44"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_45(data, param1=10, param2=20):
        """Proprietary Financial Indicator 45"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_46(data, param1=10, param2=20):
        """Proprietary Financial Indicator 46"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_47(data, param1=10, param2=20):
        """Proprietary Financial Indicator 47"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_48(data, param1=10, param2=20):
        """Proprietary Financial Indicator 48"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_49(data, param1=10, param2=20):
        """Proprietary Financial Indicator 49"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_50(data, param1=10, param2=20):
        """Proprietary Financial Indicator 50"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_51(data, param1=10, param2=20):
        """Proprietary Financial Indicator 51"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_52(data, param1=10, param2=20):
        """Proprietary Financial Indicator 52"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_53(data, param1=10, param2=20):
        """Proprietary Financial Indicator 53"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_54(data, param1=10, param2=20):
        """Proprietary Financial Indicator 54"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_55(data, param1=10, param2=20):
        """Proprietary Financial Indicator 55"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_56(data, param1=10, param2=20):
        """Proprietary Financial Indicator 56"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_57(data, param1=10, param2=20):
        """Proprietary Financial Indicator 57"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_58(data, param1=10, param2=20):
        """Proprietary Financial Indicator 58"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_59(data, param1=10, param2=20):
        """Proprietary Financial Indicator 59"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_60(data, param1=10, param2=20):
        """Proprietary Financial Indicator 60"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_61(data, param1=10, param2=20):
        """Proprietary Financial Indicator 61"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_62(data, param1=10, param2=20):
        """Proprietary Financial Indicator 62"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_63(data, param1=10, param2=20):
        """Proprietary Financial Indicator 63"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_64(data, param1=10, param2=20):
        """Proprietary Financial Indicator 64"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_65(data, param1=10, param2=20):
        """Proprietary Financial Indicator 65"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_66(data, param1=10, param2=20):
        """Proprietary Financial Indicator 66"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_67(data, param1=10, param2=20):
        """Proprietary Financial Indicator 67"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_68(data, param1=10, param2=20):
        """Proprietary Financial Indicator 68"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_69(data, param1=10, param2=20):
        """Proprietary Financial Indicator 69"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_70(data, param1=10, param2=20):
        """Proprietary Financial Indicator 70"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_71(data, param1=10, param2=20):
        """Proprietary Financial Indicator 71"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_72(data, param1=10, param2=20):
        """Proprietary Financial Indicator 72"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_73(data, param1=10, param2=20):
        """Proprietary Financial Indicator 73"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_74(data, param1=10, param2=20):
        """Proprietary Financial Indicator 74"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_75(data, param1=10, param2=20):
        """Proprietary Financial Indicator 75"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_76(data, param1=10, param2=20):
        """Proprietary Financial Indicator 76"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_77(data, param1=10, param2=20):
        """Proprietary Financial Indicator 77"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_78(data, param1=10, param2=20):
        """Proprietary Financial Indicator 78"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_79(data, param1=10, param2=20):
        """Proprietary Financial Indicator 79"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_80(data, param1=10, param2=20):
        """Proprietary Financial Indicator 80"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_81(data, param1=10, param2=20):
        """Proprietary Financial Indicator 81"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_82(data, param1=10, param2=20):
        """Proprietary Financial Indicator 82"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_83(data, param1=10, param2=20):
        """Proprietary Financial Indicator 83"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_84(data, param1=10, param2=20):
        """Proprietary Financial Indicator 84"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_85(data, param1=10, param2=20):
        """Proprietary Financial Indicator 85"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_86(data, param1=10, param2=20):
        """Proprietary Financial Indicator 86"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_87(data, param1=10, param2=20):
        """Proprietary Financial Indicator 87"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_88(data, param1=10, param2=20):
        """Proprietary Financial Indicator 88"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_89(data, param1=10, param2=20):
        """Proprietary Financial Indicator 89"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_90(data, param1=10, param2=20):
        """Proprietary Financial Indicator 90"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_91(data, param1=10, param2=20):
        """Proprietary Financial Indicator 91"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_92(data, param1=10, param2=20):
        """Proprietary Financial Indicator 92"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_93(data, param1=10, param2=20):
        """Proprietary Financial Indicator 93"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_94(data, param1=10, param2=20):
        """Proprietary Financial Indicator 94"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_95(data, param1=10, param2=20):
        """Proprietary Financial Indicator 95"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_96(data, param1=10, param2=20):
        """Proprietary Financial Indicator 96"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_97(data, param1=10, param2=20):
        """Proprietary Financial Indicator 97"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_98(data, param1=10, param2=20):
        """Proprietary Financial Indicator 98"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_99(data, param1=10, param2=20):
        """Proprietary Financial Indicator 99"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_100(data, param1=10, param2=20):
        """Proprietary Financial Indicator 100"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_101(data, param1=10, param2=20):
        """Proprietary Financial Indicator 101"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_102(data, param1=10, param2=20):
        """Proprietary Financial Indicator 102"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_103(data, param1=10, param2=20):
        """Proprietary Financial Indicator 103"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_104(data, param1=10, param2=20):
        """Proprietary Financial Indicator 104"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_105(data, param1=10, param2=20):
        """Proprietary Financial Indicator 105"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_106(data, param1=10, param2=20):
        """Proprietary Financial Indicator 106"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_107(data, param1=10, param2=20):
        """Proprietary Financial Indicator 107"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_108(data, param1=10, param2=20):
        """Proprietary Financial Indicator 108"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_109(data, param1=10, param2=20):
        """Proprietary Financial Indicator 109"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_110(data, param1=10, param2=20):
        """Proprietary Financial Indicator 110"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_111(data, param1=10, param2=20):
        """Proprietary Financial Indicator 111"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_112(data, param1=10, param2=20):
        """Proprietary Financial Indicator 112"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_113(data, param1=10, param2=20):
        """Proprietary Financial Indicator 113"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_114(data, param1=10, param2=20):
        """Proprietary Financial Indicator 114"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_115(data, param1=10, param2=20):
        """Proprietary Financial Indicator 115"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_116(data, param1=10, param2=20):
        """Proprietary Financial Indicator 116"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_117(data, param1=10, param2=20):
        """Proprietary Financial Indicator 117"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_118(data, param1=10, param2=20):
        """Proprietary Financial Indicator 118"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_119(data, param1=10, param2=20):
        """Proprietary Financial Indicator 119"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_120(data, param1=10, param2=20):
        """Proprietary Financial Indicator 120"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_121(data, param1=10, param2=20):
        """Proprietary Financial Indicator 121"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_122(data, param1=10, param2=20):
        """Proprietary Financial Indicator 122"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_123(data, param1=10, param2=20):
        """Proprietary Financial Indicator 123"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_124(data, param1=10, param2=20):
        """Proprietary Financial Indicator 124"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_125(data, param1=10, param2=20):
        """Proprietary Financial Indicator 125"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_126(data, param1=10, param2=20):
        """Proprietary Financial Indicator 126"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_127(data, param1=10, param2=20):
        """Proprietary Financial Indicator 127"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_128(data, param1=10, param2=20):
        """Proprietary Financial Indicator 128"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_129(data, param1=10, param2=20):
        """Proprietary Financial Indicator 129"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_130(data, param1=10, param2=20):
        """Proprietary Financial Indicator 130"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_131(data, param1=10, param2=20):
        """Proprietary Financial Indicator 131"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_132(data, param1=10, param2=20):
        """Proprietary Financial Indicator 132"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_133(data, param1=10, param2=20):
        """Proprietary Financial Indicator 133"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_134(data, param1=10, param2=20):
        """Proprietary Financial Indicator 134"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_135(data, param1=10, param2=20):
        """Proprietary Financial Indicator 135"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_136(data, param1=10, param2=20):
        """Proprietary Financial Indicator 136"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_137(data, param1=10, param2=20):
        """Proprietary Financial Indicator 137"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_138(data, param1=10, param2=20):
        """Proprietary Financial Indicator 138"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_139(data, param1=10, param2=20):
        """Proprietary Financial Indicator 139"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_140(data, param1=10, param2=20):
        """Proprietary Financial Indicator 140"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_141(data, param1=10, param2=20):
        """Proprietary Financial Indicator 141"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_142(data, param1=10, param2=20):
        """Proprietary Financial Indicator 142"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_143(data, param1=10, param2=20):
        """Proprietary Financial Indicator 143"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_144(data, param1=10, param2=20):
        """Proprietary Financial Indicator 144"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_145(data, param1=10, param2=20):
        """Proprietary Financial Indicator 145"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_146(data, param1=10, param2=20):
        """Proprietary Financial Indicator 146"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_147(data, param1=10, param2=20):
        """Proprietary Financial Indicator 147"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_148(data, param1=10, param2=20):
        """Proprietary Financial Indicator 148"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_149(data, param1=10, param2=20):
        """Proprietary Financial Indicator 149"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_150(data, param1=10, param2=20):
        """Proprietary Financial Indicator 150"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_151(data, param1=10, param2=20):
        """Proprietary Financial Indicator 151"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_152(data, param1=10, param2=20):
        """Proprietary Financial Indicator 152"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_153(data, param1=10, param2=20):
        """Proprietary Financial Indicator 153"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_154(data, param1=10, param2=20):
        """Proprietary Financial Indicator 154"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_155(data, param1=10, param2=20):
        """Proprietary Financial Indicator 155"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_156(data, param1=10, param2=20):
        """Proprietary Financial Indicator 156"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_157(data, param1=10, param2=20):
        """Proprietary Financial Indicator 157"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_158(data, param1=10, param2=20):
        """Proprietary Financial Indicator 158"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_159(data, param1=10, param2=20):
        """Proprietary Financial Indicator 159"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_160(data, param1=10, param2=20):
        """Proprietary Financial Indicator 160"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_161(data, param1=10, param2=20):
        """Proprietary Financial Indicator 161"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_162(data, param1=10, param2=20):
        """Proprietary Financial Indicator 162"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_163(data, param1=10, param2=20):
        """Proprietary Financial Indicator 163"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_164(data, param1=10, param2=20):
        """Proprietary Financial Indicator 164"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_165(data, param1=10, param2=20):
        """Proprietary Financial Indicator 165"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_166(data, param1=10, param2=20):
        """Proprietary Financial Indicator 166"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_167(data, param1=10, param2=20):
        """Proprietary Financial Indicator 167"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_168(data, param1=10, param2=20):
        """Proprietary Financial Indicator 168"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_169(data, param1=10, param2=20):
        """Proprietary Financial Indicator 169"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_170(data, param1=10, param2=20):
        """Proprietary Financial Indicator 170"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_171(data, param1=10, param2=20):
        """Proprietary Financial Indicator 171"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_172(data, param1=10, param2=20):
        """Proprietary Financial Indicator 172"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_173(data, param1=10, param2=20):
        """Proprietary Financial Indicator 173"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_174(data, param1=10, param2=20):
        """Proprietary Financial Indicator 174"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_175(data, param1=10, param2=20):
        """Proprietary Financial Indicator 175"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_176(data, param1=10, param2=20):
        """Proprietary Financial Indicator 176"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_177(data, param1=10, param2=20):
        """Proprietary Financial Indicator 177"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_178(data, param1=10, param2=20):
        """Proprietary Financial Indicator 178"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_179(data, param1=10, param2=20):
        """Proprietary Financial Indicator 179"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_180(data, param1=10, param2=20):
        """Proprietary Financial Indicator 180"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_181(data, param1=10, param2=20):
        """Proprietary Financial Indicator 181"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_182(data, param1=10, param2=20):
        """Proprietary Financial Indicator 182"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_183(data, param1=10, param2=20):
        """Proprietary Financial Indicator 183"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_184(data, param1=10, param2=20):
        """Proprietary Financial Indicator 184"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_185(data, param1=10, param2=20):
        """Proprietary Financial Indicator 185"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_186(data, param1=10, param2=20):
        """Proprietary Financial Indicator 186"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_187(data, param1=10, param2=20):
        """Proprietary Financial Indicator 187"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_188(data, param1=10, param2=20):
        """Proprietary Financial Indicator 188"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_189(data, param1=10, param2=20):
        """Proprietary Financial Indicator 189"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_190(data, param1=10, param2=20):
        """Proprietary Financial Indicator 190"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_191(data, param1=10, param2=20):
        """Proprietary Financial Indicator 191"""
        series = pd.Series(data)
        factor = 2
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_192(data, param1=10, param2=20):
        """Proprietary Financial Indicator 192"""
        series = pd.Series(data)
        factor = 3
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_193(data, param1=10, param2=20):
        """Proprietary Financial Indicator 193"""
        series = pd.Series(data)
        factor = 4
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_194(data, param1=10, param2=20):
        """Proprietary Financial Indicator 194"""
        series = pd.Series(data)
        factor = 5
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_195(data, param1=10, param2=20):
        """Proprietary Financial Indicator 195"""
        series = pd.Series(data)
        factor = 6
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_196(data, param1=10, param2=20):
        """Proprietary Financial Indicator 196"""
        series = pd.Series(data)
        factor = 7
        shift = 1
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_197(data, param1=10, param2=20):
        """Proprietary Financial Indicator 197"""
        series = pd.Series(data)
        factor = 8
        shift = 2
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_198(data, param1=10, param2=20):
        """Proprietary Financial Indicator 198"""
        series = pd.Series(data)
        factor = 9
        shift = 3
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_199(data, param1=10, param2=20):
        """Proprietary Financial Indicator 199"""
        series = pd.Series(data)
        factor = 10
        shift = 4
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()

    @staticmethod
    def custom_indicator_200(data, param1=10, param2=20):
        """Proprietary Financial Indicator 200"""
        series = pd.Series(data)
        factor = 1
        shift = 0
        
        step1 = series.shift(shift) * factor
        step2 = step1.rolling(window=param1).mean()
        step3 = step2.rolling(window=param2).std()
        
        result = (step1 + step2) / (step3 + 0.0001)
        return result.fillna(0).tolist()
