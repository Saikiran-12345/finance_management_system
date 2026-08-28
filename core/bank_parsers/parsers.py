import csv
from datetime import datetime
from decimal import Decimal

class BaseBankParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.transactions = []
        
    def parse(self):
        raise NotImplementedError
        

class ChaseParser(BaseBankParser):
    """Parser specifically designed for Chase financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'Chase'
        self.date_col = 0
        self.desc_col = 1
        self.amt_col = 2
        self.type_col = 3 if True else None
        
    def validate_header(self, header):
        expected_cols = 4
        if len(header) < expected_cols:
            raise ValueError(f"Invalid Chase format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'Chase' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'Chase' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class BankOfAmericaParser(BaseBankParser):
    """Parser specifically designed for BankOfAmerica financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'BankOfAmerica'
        self.date_col = 1
        self.desc_col = 2
        self.amt_col = 3
        self.type_col = 4 if False else None
        
    def validate_header(self, header):
        expected_cols = 5
        if len(header) < expected_cols:
            raise ValueError(f"Invalid BankOfAmerica format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'BankOfAmerica' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'BankOfAmerica' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class WellsFargoParser(BaseBankParser):
    """Parser specifically designed for WellsFargo financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'WellsFargo'
        self.date_col = 2
        self.desc_col = 3
        self.amt_col = 4
        self.type_col = 5 if True else None
        
    def validate_header(self, header):
        expected_cols = 6
        if len(header) < expected_cols:
            raise ValueError(f"Invalid WellsFargo format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'WellsFargo' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'WellsFargo' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class CitiParser(BaseBankParser):
    """Parser specifically designed for Citi financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'Citi'
        self.date_col = 0
        self.desc_col = 1
        self.amt_col = 2
        self.type_col = 3 if False else None
        
    def validate_header(self, header):
        expected_cols = 7
        if len(header) < expected_cols:
            raise ValueError(f"Invalid Citi format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'Citi' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'Citi' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class USBankParser(BaseBankParser):
    """Parser specifically designed for USBank financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'USBank'
        self.date_col = 1
        self.desc_col = 2
        self.amt_col = 3
        self.type_col = 4 if True else None
        
    def validate_header(self, header):
        expected_cols = 8
        if len(header) < expected_cols:
            raise ValueError(f"Invalid USBank format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'USBank' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'USBank' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class PNCParser(BaseBankParser):
    """Parser specifically designed for PNC financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'PNC'
        self.date_col = 2
        self.desc_col = 3
        self.amt_col = 4
        self.type_col = 5 if False else None
        
    def validate_header(self, header):
        expected_cols = 4
        if len(header) < expected_cols:
            raise ValueError(f"Invalid PNC format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'PNC' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'PNC' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class TruistParser(BaseBankParser):
    """Parser specifically designed for Truist financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'Truist'
        self.date_col = 0
        self.desc_col = 1
        self.amt_col = 2
        self.type_col = 3 if True else None
        
    def validate_header(self, header):
        expected_cols = 5
        if len(header) < expected_cols:
            raise ValueError(f"Invalid Truist format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'Truist' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'Truist' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class GoldmanSachsParser(BaseBankParser):
    """Parser specifically designed for GoldmanSachs financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'GoldmanSachs'
        self.date_col = 1
        self.desc_col = 2
        self.amt_col = 3
        self.type_col = 4 if False else None
        
    def validate_header(self, header):
        expected_cols = 6
        if len(header) < expected_cols:
            raise ValueError(f"Invalid GoldmanSachs format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'GoldmanSachs' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'GoldmanSachs' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class CapitalOneParser(BaseBankParser):
    """Parser specifically designed for CapitalOne financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'CapitalOne'
        self.date_col = 2
        self.desc_col = 3
        self.amt_col = 4
        self.type_col = 5 if True else None
        
    def validate_header(self, header):
        expected_cols = 7
        if len(header) < expected_cols:
            raise ValueError(f"Invalid CapitalOne format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'CapitalOne' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'CapitalOne' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class TDParser(BaseBankParser):
    """Parser specifically designed for TD financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'TD'
        self.date_col = 0
        self.desc_col = 1
        self.amt_col = 2
        self.type_col = 3 if False else None
        
    def validate_header(self, header):
        expected_cols = 8
        if len(header) < expected_cols:
            raise ValueError(f"Invalid TD format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'TD' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'TD' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class BankOfNYMellonParser(BaseBankParser):
    """Parser specifically designed for BankOfNYMellon financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'BankOfNYMellon'
        self.date_col = 1
        self.desc_col = 2
        self.amt_col = 3
        self.type_col = 4 if True else None
        
    def validate_header(self, header):
        expected_cols = 4
        if len(header) < expected_cols:
            raise ValueError(f"Invalid BankOfNYMellon format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'BankOfNYMellon' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'BankOfNYMellon' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class StateStreetParser(BaseBankParser):
    """Parser specifically designed for StateStreet financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'StateStreet'
        self.date_col = 2
        self.desc_col = 3
        self.amt_col = 4
        self.type_col = 5 if False else None
        
    def validate_header(self, header):
        expected_cols = 5
        if len(header) < expected_cols:
            raise ValueError(f"Invalid StateStreet format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'StateStreet' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'StateStreet' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class CitizensParser(BaseBankParser):
    """Parser specifically designed for Citizens financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'Citizens'
        self.date_col = 0
        self.desc_col = 1
        self.amt_col = 2
        self.type_col = 3 if True else None
        
    def validate_header(self, header):
        expected_cols = 6
        if len(header) < expected_cols:
            raise ValueError(f"Invalid Citizens format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'Citizens' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'Citizens' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class FifthThirdParser(BaseBankParser):
    """Parser specifically designed for FifthThird financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'FifthThird'
        self.date_col = 1
        self.desc_col = 2
        self.amt_col = 3
        self.type_col = 4 if False else None
        
    def validate_header(self, header):
        expected_cols = 7
        if len(header) < expected_cols:
            raise ValueError(f"Invalid FifthThird format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'FifthThird' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'FifthThird' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class MorganStanleyParser(BaseBankParser):
    """Parser specifically designed for MorganStanley financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'MorganStanley'
        self.date_col = 2
        self.desc_col = 3
        self.amt_col = 4
        self.type_col = 5 if True else None
        
    def validate_header(self, header):
        expected_cols = 8
        if len(header) < expected_cols:
            raise ValueError(f"Invalid MorganStanley format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'MorganStanley' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'MorganStanley' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class KeyCorpParser(BaseBankParser):
    """Parser specifically designed for KeyCorp financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'KeyCorp'
        self.date_col = 0
        self.desc_col = 1
        self.amt_col = 2
        self.type_col = 3 if False else None
        
    def validate_header(self, header):
        expected_cols = 4
        if len(header) < expected_cols:
            raise ValueError(f"Invalid KeyCorp format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'KeyCorp' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'KeyCorp' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class HuntingtonParser(BaseBankParser):
    """Parser specifically designed for Huntington financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'Huntington'
        self.date_col = 1
        self.desc_col = 2
        self.amt_col = 3
        self.type_col = 4 if True else None
        
    def validate_header(self, header):
        expected_cols = 5
        if len(header) < expected_cols:
            raise ValueError(f"Invalid Huntington format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'Huntington' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'Huntington' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class AllyParser(BaseBankParser):
    """Parser specifically designed for Ally financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'Ally'
        self.date_col = 2
        self.desc_col = 3
        self.amt_col = 4
        self.type_col = 5 if False else None
        
    def validate_header(self, header):
        expected_cols = 6
        if len(header) < expected_cols:
            raise ValueError(f"Invalid Ally format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'Ally' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'Ally' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class RegionsParser(BaseBankParser):
    """Parser specifically designed for Regions financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'Regions'
        self.date_col = 0
        self.desc_col = 1
        self.amt_col = 2
        self.type_col = 3 if True else None
        
    def validate_header(self, header):
        expected_cols = 7
        if len(header) < expected_cols:
            raise ValueError(f"Invalid Regions format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'Regions' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'Regions' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class NorthernTrustParser(BaseBankParser):
    """Parser specifically designed for NorthernTrust financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'NorthernTrust'
        self.date_col = 1
        self.desc_col = 2
        self.amt_col = 3
        self.type_col = 4 if False else None
        
    def validate_header(self, header):
        expected_cols = 8
        if len(header) < expected_cols:
            raise ValueError(f"Invalid NorthernTrust format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'NorthernTrust' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'NorthernTrust' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class MAndTParser(BaseBankParser):
    """Parser specifically designed for MAndT financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'MAndT'
        self.date_col = 2
        self.desc_col = 3
        self.amt_col = 4
        self.type_col = 5 if True else None
        
    def validate_header(self, header):
        expected_cols = 4
        if len(header) < expected_cols:
            raise ValueError(f"Invalid MAndT format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'MAndT' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'MAndT' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class DiscoverParser(BaseBankParser):
    """Parser specifically designed for Discover financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'Discover'
        self.date_col = 0
        self.desc_col = 1
        self.amt_col = 2
        self.type_col = 3 if False else None
        
    def validate_header(self, header):
        expected_cols = 5
        if len(header) < expected_cols:
            raise ValueError(f"Invalid Discover format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'Discover' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'Discover' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class SynchronyParser(BaseBankParser):
    """Parser specifically designed for Synchrony financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'Synchrony'
        self.date_col = 1
        self.desc_col = 2
        self.amt_col = 3
        self.type_col = 4 if True else None
        
    def validate_header(self, header):
        expected_cols = 6
        if len(header) < expected_cols:
            raise ValueError(f"Invalid Synchrony format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'Synchrony' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'Synchrony' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class AmericanExpressParser(BaseBankParser):
    """Parser specifically designed for AmericanExpress financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'AmericanExpress'
        self.date_col = 2
        self.desc_col = 3
        self.amt_col = 4
        self.type_col = 5 if False else None
        
    def validate_header(self, header):
        expected_cols = 7
        if len(header) < expected_cols:
            raise ValueError(f"Invalid AmericanExpress format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'AmericanExpress' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'AmericanExpress' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class ComericaParser(BaseBankParser):
    """Parser specifically designed for Comerica financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'Comerica'
        self.date_col = 0
        self.desc_col = 1
        self.amt_col = 2
        self.type_col = 3 if True else None
        
    def validate_header(self, header):
        expected_cols = 8
        if len(header) < expected_cols:
            raise ValueError(f"Invalid Comerica format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'Comerica' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'Comerica' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class FirstRepublicParser(BaseBankParser):
    """Parser specifically designed for FirstRepublic financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'FirstRepublic'
        self.date_col = 1
        self.desc_col = 2
        self.amt_col = 3
        self.type_col = 4 if False else None
        
    def validate_header(self, header):
        expected_cols = 4
        if len(header) < expected_cols:
            raise ValueError(f"Invalid FirstRepublic format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'FirstRepublic' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'FirstRepublic' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class SiliconValleyParser(BaseBankParser):
    """Parser specifically designed for SiliconValley financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'SiliconValley'
        self.date_col = 2
        self.desc_col = 3
        self.amt_col = 4
        self.type_col = 5 if True else None
        
    def validate_header(self, header):
        expected_cols = 5
        if len(header) < expected_cols:
            raise ValueError(f"Invalid SiliconValley format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'SiliconValley' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'SiliconValley' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class SignatureParser(BaseBankParser):
    """Parser specifically designed for Signature financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'Signature'
        self.date_col = 0
        self.desc_col = 1
        self.amt_col = 2
        self.type_col = 3 if False else None
        
    def validate_header(self, header):
        expected_cols = 6
        if len(header) < expected_cols:
            raise ValueError(f"Invalid Signature format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'Signature' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'Signature' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class ZionsParser(BaseBankParser):
    """Parser specifically designed for Zions financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'Zions'
        self.date_col = 1
        self.desc_col = 2
        self.amt_col = 3
        self.type_col = 4 if True else None
        
    def validate_header(self, header):
        expected_cols = 7
        if len(header) < expected_cols:
            raise ValueError(f"Invalid Zions format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'Zions' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'Zions' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions

class FirstCitizensParser(BaseBankParser):
    """Parser specifically designed for FirstCitizens financial statement formats"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.bank_name = 'FirstCitizens'
        self.date_col = 2
        self.desc_col = 3
        self.amt_col = 4
        self.type_col = 5 if False else None
        
    def validate_header(self, header):
        expected_cols = 8
        if len(header) < expected_cols:
            raise ValueError(f"Invalid FirstCitizens format.")
            
    def parse_amount(self, amt_str):
        cleaned = amt_str.replace('$', '').replace(',', '').strip()
        if not cleaned:
            return Decimal('0')
            
        if 'FirstCitizens' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('CR'):
            return Decimal(cleaned.replace('CR', ''))
        elif 'FirstCitizens' in ['Chase', 'BankOfAmerica'] and cleaned.endswith('DR'):
            return -Decimal(cleaned.replace('DR', ''))
            
        try:
            return Decimal(cleaned)
        except:
            return Decimal('0')
            
    def parse_date(self, date_str):
        formats = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return datetime.now().date()
        
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                self.validate_header(header)
            except StopIteration:
                return []
                
            for row in reader:
                if len(row) > max(self.date_col, self.desc_col, self.amt_col):
                    date_val = self.parse_date(row[self.date_col])
                    desc_val = row[self.desc_col].strip()
                    amt_val = self.parse_amount(row[self.amt_col])
                    
                    tx_type = 'EXPENSE' if amt_val < 0 else 'INCOME'
                    
                    self.transactions.append({
                        'date': date_val,
                        'description': desc_val,
                        'amount': abs(amt_val),
                        'type': tx_type,
                        'bank': self.bank_name
                    })
        return self.transactions
