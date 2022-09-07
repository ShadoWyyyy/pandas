import numpy as np
import pandas as pd

            
s = pd.Series([1, 3, 5, np.nan, 6, 8])

dates = pd.date_range("20130101", periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3]*4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo"
    }
)

# Check data type
print(df2.dtypes)
# View df
print(df.head(5))
print(df.tail(3))
print(df.index)
print(df.columns)
# Statistical summary
print(df.describe())
# Transpose
print(df.T)
# Arrange by column value
print(df.sort_values(by="B"))

# information about employees
id_number = ['128', '478', '257', '299', '175', '328', '099', '457', '144', '222']
name = ['Patrick', 'Amanda', 'Antonella', 'Eduard', 'John', 'Alejandra', 'Layton', 'Melanie', 'David', 'Lewis']
surname = ['Miller', 'Torres', 'Brown', 'Iglesias', 'Wright', 'Campos', 'Platt', 'Cavill', 'Lange', 'Bellow']
division = ['Sales', 'IT', 'IT', 'Sales', 'Marketing', 'Engineering', 'Engineering', 'Sales', 'Engineering', 'Sales']
salary = [30000, 54000, 80000, 79000, 15000, 18000, 30000, 35000, 45000, 30500]
telephone = ['7366578', '7366444', '7366120', '7366574', '7366113', '7366117', '7366777', '7366579', '7366441', '7366440']
type_contract = ['permanent', 'temporary', 'temporary', 'permanent', 'internship', 'internship', 'permanent', 'temporary', 'permanent', 'permanent']

# data frame containing information about employees
df_employees = pd.DataFrame({'name': name, 'surname': surname, 'division': division,
                             'salary': salary, 'telephone': telephone, 'type_contract': type_contract}, index=id_number)

print(df_employees)

# Access by columns
print(df_employees.salary)
type(df_employees['salary'])
type(df_employees[['salary']])

print(df_employees[['division', 'salary']])
df_employees.select_dtypes(include=np.number)
df_employees.info()
print(df_employees.dtypes)

# Access by rows
type(df_employees.loc['478'])
type(df_employees.iloc[[1]])
type(df_employees.iloc[0:5])

# Access by coordinates
print(df_employees.iat[1, 3])
print(df_employees.at['478', 'salary'])

# filter and select
print(df_employees[df_employees['salary'] > 45000])
print(df_employees[(df_employees['salary'] > 45000) & (df_employees['type_contract'] == 'permanent')])

print(df_employees[df_employees['type_contract'].isin(['temporary', 'permanent'])])
print(df_employees[df_employees['salary'].between(30000, 80000)])
print(df_employees[df_employees['telephone'].str.contains('57')])
print(df_employees[df_employees['name'].str.startswith('A')])

