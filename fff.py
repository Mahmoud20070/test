import pandas as pd

tkt = r'//mypath//mypath//test.test'
sch = r'//mypath//mypath//DB//roster-Jan-24.linux'

columns_head = ['Date Of Case', 'ACD_1', 'New_shift1', 'ACD_2', 'New_shift2', 'Resolution', 'Category']
ids_to_check = [52300]
date_to_check = ['25-Jan']

dftkt = pd.read_csv(tkt, usecols=columns_head).iloc[::-1]

filtered_df = dftkt[(dftkt['Resolution'] == 'Done') & 
                    (dftkt['Category'] == 'Eschedule') | (dftkt['Category'] == 'Request')]  
                    #& (dftkt['ACD_1'].isin(ids_to_check) | dftkt['ACD_2'].isin(ids_to_check))
                    #& (dftkt['Date Of Case'].isin(date_to_check))



removeduplicate1 = filtered_df.drop_duplicates(subset=['Date Of Case', 'ACD_1', 'ACD_2'])
removeduplicate2 = filtered_df.drop_duplicates(subset=['Date Of Case', 'ACD_1'])
removeduplicate3 = filtered_df.drop_duplicates(subset=['Date Of Case', 'ACD_2'])

date_acd_shift_dict = {}
for index, row in removeduplicate3.iterrows():
    date_acd_concat = row['Date Of Case'] + '_' + str(row['ACD_1'])
    date_acd_concat2 = row['Date Of Case'] + '_' + str(row['ACD_2'])

    if date_acd_concat not in date_acd_shift_dict and str(row['ACD_1']) != "-":
        shift_value1 = row['New_shift1']  # Assuming you want to use 'New_shift1'
        date_acd_shift_dict[date_acd_concat] = shift_value1

    if date_acd_concat2 not in date_acd_shift_dict and str(row['ACD_2']) != "-":
        shift_value2 = row['New_shift2']  # Assuming you want to use 'New_shift1'
        date_acd_shift_dict[date_acd_concat2] = shift_value2    
    
d  = pd.DataFrame.from_dict(date_acd_shift_dict,orient='index', columns=['Shift Value'])

d.to_excel('/home/ml/Desktop/withindex.xlsx')
d.reset_index().to_excel('/home/ml/Desktop/withoutindex.xlsx')





