import pandas as pd
import numpy as np

df = pd.DataFrame([
    {'Name': 'JS', 'Item': 'macbook pro', 'Cost': 2000000},
    {'Name': 'DS', 'Item': 'good bag', 'Cost': 1000000},
    {'Name': 'YT', 'Item': 'car', 'Cost': 300000000}],
    index=['Syn1', 'Syn1', 'Syn2'])
print df

df['Date'] = ['December 26', 'January 4', 'June 15']
print df

df['Delivered'] = False
print df

df['Instagram'] = ['Positive', None, 'Negative']
print df

df2 = df.reset_index()
df2['Date'] = pd.Series({0: 'Dec 5', 2: 'April 23'})
print df2

#Join
staff = pd.DataFrame([{'Name': 'Keny', 'Role': 'Director of HR'},
                         {'Name': 'Sully', 'Role': 'Course liasion'},
                         {'Name': 'Jams', 'Role': 'Grader'}])
staff = staff.set_index('Name')
student = pd.DataFrame([{'Name': 'Jams', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sully', 'School': 'Engineering'}])
student = student.set_index('Name')
print(staff.head())
print("---------------------------------------")
print(student.head())

print pd.merge(staff, student, how='outer', left_index=True, right_index=True)
print pd.merge(staff, student, how='inner', left_index=True, right_index=True)
print pd.merge(staff, student, how='left', left_index=True, right_index=True)
print pd.merge(staff, student, how='right', left_index=True, right_index=True)

staff = staff.reset_index()
student = student.reset_index()
staff['Location'] = ['seoul', 'goyang', 'gangwon']
student['Location'] = ['gangnam', 'hongdei', 'soju']
print pd.merge(staff, student, how='left', left_on='Name', right_on='Name')
staff['Initial'] = ['kim', 'suk', 'js']
student['Initial'] = ['jj', 'sy', 'ku']
print staff
print student
print pd.merge(staff, student, how='inner', left_on=['Name', 'Initial'], right_on=['Name', 'Initial'])
print pd.merge(staff, student, how='outer', left_on=['Name', 'Initial'], right_on=['Name', 'Initial'])
print pd.merge(staff, student, how='left', left_on=['Name', 'Initial'], right_on=['Name', 'Initial'])