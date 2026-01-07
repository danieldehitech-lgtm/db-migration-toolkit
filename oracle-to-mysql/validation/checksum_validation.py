import hashlib

def checksum(values):
    return hashlib.md5("".join(values).encode()).hexdigest()

oracle_sample = ["1Ali", "2Sara"]
mysql_sample  = ["1Ali", "2Sara"]

assert checksum(oracle_sample) == checksum(mysql_sample)
print("Data validation passed")
