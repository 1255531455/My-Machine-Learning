# Python Script
# In order to apply the Singular Value Decomposition algorithm, we employed the Numpy open-source Python library.1
from sklearn import linear_model

U, S, VT = np.linalg.svd(M) #execute SVD
# To calculate the predicted energy barrier matrix
#Read U,S,VT .csv files
U = np.array(pd.read_csv(U.csv, sep=',', header=None))
S = np.array(pd.read_csv(S.csv, sep=',', header=None))
VT = np.array(pd.read_csv(VT.csv, sep=',', header=None))
#Transpose the U matrix, select the number of hds to predict the energy barrier
U_t = np.transpose(U)
M_intermediate = list()
number_hd = 26
#Compute the predicted energy barrier matrix (predictedenergy_matrix_26)
for n in range(number_hd):
M_intermediate.append(U_t[n]*S[n])
np_M_intermediate = np.array(M_intermediate)
M_intermediate_26_26 = np.transpose(np_M_intermediate)
VT_reshaped = VT[:26].reshape((number_hd,26))
predictedenergy_matrix_26 =
np.matmul(M_intermediate_26_26,VT_reshaped)
# To perform linear regression in a loop.
#Read U, S,VT, conv_descrip .csv files
U = np.array(pd.read_csv(U.csv, sep=',', header=None))
S = np.array(pd.read_csv(S.csv, sep=',', header=None))
VT = np.array(pd.read_csv(VT.csv, sep=',', header=None))
Conv_descrip = np.transpose(np.array(pd.read_csv('conv_descrip.csv',
sep=',',header=None, error_bad_lines=False)))
r_value_list = list()
U_data = U_gibbs_react[:26,0] #select the HD number of EG
3
VT_data = V_gibbs_react[0,:26] #select the HD number of LG
column = [j for j in range(2,193,1)] #select the columns of the
conventional descriptors to correlate with the HDs
#Linear regression between one HD vector and the conventional
descriptors
for i in column:
descrip_set = conv_descrip[i, 1:27]
l_descrip = list(descrip_set)
l_x = [float(obj) for obj in l_descrip]
l_y = list(U_datat)
slope, intercept, r_value, p_value, std_err =
stats.linregress(l_y, l_x) #perform the linear regression
print('y = ' + str(round(slope,3)) + 'x' + ' + ' + str(round(intercept,3)) , " R²:", str(round(r_value**2,3)), ' ', 'Descriptor number:',i-1)
r_value_list.append(round(r_value**2,3))
# To perform multilinear regression in a loop:
#Read U, S,VT, conv_descrip .csv files
conv_descrip = np.transpose(np.array(pd.read_csv(path1,
sep=',',header=None, error_bad_lines=False)))
descriptors = conv_descrip[2:147,1:27]
descriptors2 = [[float(o2) for o2 in o] for o in descriptors]
hiddendescriptors = np.transpose(np.array(pd.read_csv(path2, sep=',',header=None))).astype(np.float)
hd1 = hiddendescriptors[:1, :26]
descriptors2_matrix = np.array(descriptors2)
Total_Variables = [i for i in range(len(descriptors2))]
#Calculation of how many combinations are
comb = list(combinations(Total_Variables, 2))
#Save the descriptors of each of the combination
first_tuple_elements = []
second_tuple_elements = []
for i in comb:
 first_tuple_elements.append(i[0])
 second_tuple_elements.append(i[1])
4
#Save the descriptors of each of the combination
descriptors3 = []
for i in first_tuple_elements:
 descriptors3.append(descriptors2_matrix[i, :])
descriptors4 = []
for j in second_tuple_elements:
 descriptors4.append(descriptors2_matrix[j, :])
#Generation of the tensor with all the matrix of descriptors
matrix_test = np.zeros((2,26,len(comb)))
for z in range(len(comb)):
 matrix_test[:,:,z] = np.array([descriptors3[z], descriptors4[z]])
#Solution of the system of linear equations
len_comb = [i for i in range(len(comb))]
indices = zip(first_tuple_elements, second_tuple_elements, len_comb)
r_value_list = list()
elements_list = list()
elements_sorted = list()
for i in range(len(comb)):
 regr = linear_model.LinearRegression()
 regr.fit(matrix_test[:,:,i].T , hd1.T)
 coef = regr.coef_
 r_value = regr.score(matrix_test[:,:,i].T, hd1.T)
 intercept_value = regr.intercept_
 r_value_list.append(round(r_value**2,3))
 elements = zip(r_value_list, first_tuple_elements,
second_tuple_elements, len_comb)
 elements_list = list(elements)
 print(len(elements_list))
 elements_list.sort(reverse=True, key=lambda i:i[0])
We also calculated the maximum and minimum error applying Numpy Library.
Mean_value = i.mean(i)
Max_value = np.max(i)
5
We applied Scikit-learn Library to compute MAE and MSE.2
MAE = metrics.mean_absolute_error(exact_energy, predicted_energy)
MSE = metrics. mean_squared_error (exact_energy, predicted_energy)