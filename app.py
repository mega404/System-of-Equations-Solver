from flask import Flask, request, render_template
import re
import time
from numpy.core.fromnumeric import var

from Code import GaussElimination, GauessJordan, LUDolittle
from court_LU import Court_decompostion
from jacobi import jac
from seidel import Seidel
from Newton import Newton
#
from bracketing import Bracketing
from secant_fixedPoint import SecantMethod, fixed_point
import numpy as np
import os

app = Flask(__name__)
equ_arr = []
var_names = []
ans_dic = {}

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

for file in (os.listdir("/home/gad/Desktop")) :
    if file.endswith('.png') or file.endswith('.jpg') :
        os.remove(os.path.join("/home/gad/Desktop", file))


@app.route("/")
def home() :
    return render_template("home.html")

#===========================================================

@app.route("/Gauss" , methods = ['POST', 'GET'])
def gauss() :
    equ2d, rows, precession  =  create_matrix_input()
    if equ2d == "error" :
        return render_template("error_handle.html", text = "Number of variables must be equal to the number of equations")
    start = time.time()
    gauss = GaussElimination(equ2d[:,:rows] , equ2d[:,rows], precession)
    ans_arr = gauss.backSubstitution()
    end = time.time()
    if ans_arr != "error" :
        ans_dic = conver_from_arr_to_dic(ans_arr)
    else :
        ans_dic = "error"
    print("run gauss")
    return render_template("result.html", text = ans_dic, method = "Gauss Elimination Method", time = end-start)

#=============================================================

@app.route("/GaussJordan", methods = ['POST', 'GET'])
def gaussJordan() :
    equ2d, rows, precession  =  create_matrix_input()
    if equ2d == "error" :
        return render_template("error_handle.html", text = "Number of variables must be equal to the number of equations")
    start = time.time()
    gauss_Jordan = GauessJordan(equ2d[:,:rows] , equ2d[:,rows], precession)
    ans_arr = gauss_Jordan.getOutput()
    end = time.time()
    if ans_arr != "error" :
        ans_dic = conver_from_arr_to_dic(ans_arr)
    else :
        ans_dic = "error"
    print("run gauss jordan")
    return render_template("result.html", text = ans_dic, method = "Gauss Jordan Method", time = end-start)

#==============================================================

@app.route("/Doolittle", methods = ['POST', 'GET'])
def doolittle() :
    equ2d, rows, precession  =  create_matrix_input()
    if equ2d == "error" :
        return render_template("error_handle.html", text = "Number of variables must be equal to the number of equations")
    start = time.time()
    Doolittle = LUDolittle(equ2d[:,:rows] , equ2d[:,rows], precession)
    ans_arr = Doolittle.backSubstitution()
    end = time.time()
    if ans_arr != "error" :
        ans_dic = conver_from_arr_to_dic(ans_arr)
    else :
        ans_dic = "error"
    print("run doolittle")
    return render_template("result.html", text = ans_dic, method = "Doolittle Method", time = end-start)

#=============================================================== 

@app.route("/Crout", methods = ['POST', 'GET'])
def crout() :
    equ2d, rows, precession =  create_matrix_input()
    if equ2d == "error" :
        return render_template("error_handle.html", text = "Number of variables must be equal to the number of equations")
    start = time.time()
    Crout = Court_decompostion(np.array(equ2d[:,:rows],float) , np.array(equ2d[:,rows],float).reshape(rows,1), precession)
    l, u = Crout.turn_to_LU()
    y     = Crout.find_y(l)
    ans_arr = Crout.find_x(u,y)
    end = time.time()
    if ans_arr != "error" :
        ans_dic = conver_from_arr_to_dic(ans_arr)
    else :
        ans_dic = "error"
    print("run crout")
    return render_template("result.html", text = ans_dic, method = "Crout Method", time = end-start)

#=======================================================================

@app.route("/Jacobii", methods = ['POST', 'GET'])
def jacobii() :
    initial_guess   = request.form['initial_guess']
    no_of_iteration = request.form['no_of_iteration']
    abs_rel_error   = request.form['abs_rel_error']
    if initial_guess == "" :
        jacobi = jac( rowsj, equ2dj[:,:rowsj] , np.array(equ2dj[:,rowsj],float), precessionj, abs_rel_error , no_of_iteration, initial_guess)
    else :
        jacobi = jac( rowsj, equ2dj[:,:rowsj] , np.array(equ2dj[:,rowsj],float), precessionj, abs_rel_error , no_of_iteration, np.array(float(initial_guess)))
    start = time.time() 
    ans_arr = jacobi.Eval()
    end = time.time()
    ans_dic = conver_from_arr_to_dic(ans_arr)
    print("run jacobii")
    return render_template("result.html", method = "Jacobii Method", text = ans_dic, time = end-start)

#==================================================================

@app.route("/GaussSeidal", methods = ['POST', 'GET'])
def gaussSeidal() :
    initial_guess   = request.form['initial_guess']
    no_of_iteration = request.form['no_of_iteration']
    abs_rel_error   = request.form['abs_rel_error']
    if initial_guess == "" :
        seidel = Seidel( rowsg, equ2dg[:,:rowsg] , np.array(equ2dg[:,rowsg],float), precessiong, abs_rel_error , no_of_iteration, initial_guess)
    else :
        seidel = Seidel( rowsg, equ2dg[:,:rowsg] , np.array(equ2dg[:,rowsg],float), precessiong, abs_rel_error , no_of_iteration, np.array(float(initial_guess)))
    start = time.time()
    ans_arr = seidel.Eval()
    end = time.time()
    ans_dic = conver_from_arr_to_dic(ans_arr)
    print("run gaussSeidal")
    return render_template("result.html", text = ans_dic, method = "Gauss Seidal Method", time = end-start)

#===================================================================

@app.route("/jacobi_mat", methods = ['POST', 'GET'])
def jacobi_mat():
    global equ2dj  
    global rowsj 
    global precessionj
    equ2dj, rowsj, precessionj =  create_matrix_input()
    if equ2dj == "error" :
        return render_template("error_handle.html", text = "Number of variables must be equal to the number of equations")
    return render_template("Jacoobi.html")

#===================================================================

@app.route("/seidal_mat", methods = ['POST', 'GET'])
def seidal_mat():
    global equ2dg 
    global rowsg 
    global precessiong
    equ2dg, rowsg, precessiong =  create_matrix_input()
    if equ2dg == "error" :
        return render_template("error_handle.html", text = "Number of variables must be equal to the number of equations")
    return render_template("GaussSeidal.html")


#equ_arr = ["x+y-z=1", "x+y=2", "x+z=4"]
#print(equ_arr[-1])

#@app.route("/matrix_dim", methods = ['POST', 'GET'])
#================================================================================================


@app.route("/Bisection_before", methods = ['POST', 'GET'])
def Bisection_before():
    global precessionB
    global equ_arrB
    rows = request.form['rows']
    precessionB = request.form['precission']
    equ_arrB = request.form['equ_no1']
    #plt.savefig('C:/Users/es-abdoahmed022/gui_for_signs/static/confusion_matrix.png', facecolor = "green")
    return render_template("bisection.html")

@app.route("/Bisection", methods = ['POST', 'GET'])
def Bisection():
    xl = request.form['x_Lower']
    xu = request.form['x_Upper']
    abs = request.form['abs_rel_error']
    global startB
    global endB
    global condB
    startB = time.time()
    root = Bracketing(equ_arrB, 'bisection', (xl), (xu), (precessionB), (abs))
    condB = root.find_root()
    endB = time.time()
    #plt.savefig('C:/Users/es-abdoahmed022/gui_for_signs/static/confusion_matrix.png', facecolor = "green")
    return render_template("bi_image.html")

@app.route("/Bisection_answer", methods = ['POST', 'GET'])
def Bisection_answer():
    return render_template("result.html", text =  condB, method = "Bisection Method", time = endB-startB)

#===================================================================


@app.route("/Regula_falsii_before", methods = ['POST', 'GET'])
def Regula_falsii_before():
    global precessionR
    global equ_arrR
    rows = request.form['rows']
    precessionR = request.form['precission']
    equ_arrR = request.form['equ_no1']
    #plt.savefig('C:/Users/es-abdoahmed022/gui_for_signs/static/confusion_matrix.png', facecolor = "green")
    return render_template("regula_falsii.html")

@app.route("/Regula_falsii", methods = ['POST', 'GET'])
def Regula_falsii():
    xl = request.form['x_Lower']
    xu = request.form['x_Upper']
    abs = request.form['abs_rel_error']
    global startR
    global endR
    global condR
    startR = time.time()
    root = Bracketing(equ_arrR, 'Regula-Falsi', xl, xu, precessionR, abs)
    condR = root.find_root()
    endR = time.time()
    #plt.savefig('C:/Users/es-abdoahmed022/gui_for_signs/static/confusion_matrix.png', facecolor = "green")
    return render_template("ri_image.html")


@app.route("/Regula_falsii_answer", methods = ['POST', 'GET'])
def Regula_falsii_answer():
    return render_template("result.html", text = condR, method = "Regula_falsii Method", time = endR-startR)


#===================================================================

@app.route("/Fixed_point_before", methods = ['POST', 'GET'])
def Fixed_point_before():
    global rowsF
    global precessionF
    global equ_arrF
    rowsF = request.form['rows']
    precessionF = request.form['precission']
    equ_arrF = request.form['equ_no1']
    return render_template("fixed.html", method = "Fixed_point Method")

@app.route("/Fixed_point", methods = ['POST', 'GET'])
def Fixed_point():
    Xi = request.form['Xi']
    no_of_iteration = request.form['no_of_iteration']
    abs_rel_error   = request.form['abs_rel_error']
    global startf
    global endf
    global resf
    startf = time.time()
    fx = fixed_point(equ_arrF, int(Xi), (abs_rel_error), (precessionF))
    resf = fx.computeFixedPoint()
    endf = time.time()
    return render_template("f_image.html")

@app.route("/Fixed_answer", methods = ['POST', 'GET'])
def Fixed_answer():
    return render_template("result.html", text = resf, method = "Secant Method", time = endf-startf)  

#===================================================================
@app.route("/Newton_before", methods = ['POST', 'GET'])
def Newton_before():
    global rowsN 
    global precessionN
    global equ_arrN
    rowsN = request.form['rows']
    precessionN = request.form['precission']
    equ_arrN = request.form['equ_no1']
    return render_template("newton.html", method = "Newton Raphason Method") 


@app.route("/Newton_Raphason", methods = ['POST', 'GET'])
def Newton_Raphason():
    global initial_guessN   
    global no_of_iterationN 
    global abs_rel_errorN 
    initial_guessN   = request.form['initial_guess']
    no_of_iterationN = request.form['no_of_iteration']
    abs_rel_errorN   = request.form['abs_rel_error']
    return render_template("image.html")

@app.route("/Newton_answer", methods = ['POST', 'GET'])
def Newton_answer():
    global rowsN 
    global precessionN
    global equ_arrN
    start = time.time()
    newton = Newton(equ_arrN, (initial_guessN), (precessionN), (no_of_iterationN), (abs_rel_errorN))
    ans = newton.algorithm()
    end = time.time()
    return render_template("result.html", text = ans, method = "Newton Raphason Method", time = end-start)

#===================================================================

@app.route("/Secant_before", methods = ['POST', 'GET'])
def Secant_before():
    global rowsS
    global precessionS
    global equ_arrS
    rowsS = request.form['rows']
    precessionS = request.form['precission']
    equ_arrS = request.form['equ_no1']
    return render_template("secant.html", method = "Secant Method")


@app.route("/Secant", methods = ['POST', 'GET'])
def Secant():
    Xi_1  = request.form['Xi_1']
    Xi = request.form['Xi']
    no_of_iteration = request.form['no_of_iteration']
    abs_rel_error   = request.form['abs_rel_error']
    global startS
    global endS
    global resS
    startS = time.time()
    sc = SecantMethod(equ_arrS, int(Xi_1), int(Xi), (abs_rel_error), (precessionS))
    resS = sc.secant()
    endS = time.time()
    return render_template("s_image.html")

@app.route("/Secant_answer", methods = ['POST', 'GET'])
def Secant_answer():
    return render_template("result.html", text = resS, method = "Secant Method", time = endS-startS)  
'''
    global Xi 
    global Xi_1
    global no_of_iterationN 
    global abs_rel_errorN 
'''

#===================================================================


def create_matrix_input():
    rows = request.form['rows']
    precission = request.form['precission']
    #print(precission)
    for i in range(int(rows)) :
        equ_arr.append(request.form['equ_no' + str(i+1)])

    equs_validity = check_equs_validity(equ_arr, int(rows))
    if (equs_validity == "Number of variables must be equal to the number of equations") :
        return "error", "error", "error"
    return generate_mat(equ_arr, int(rows),  precission)

#=================================================================================================

def generate_mat(equ_arr, rows,  precission) :
    
    '''
    for i in range(rows) :
        equ = re.split('\+|=|-', equ_arr[i])
        print(equ)
        if len(equ) != (rows + 1) :
            continue
        else :
            for i in range(len(equ)-1) :
                for j in range(len(equ[i])) :
                    if equ[i][j].isalpha() :
                        var_names.append(equ[i][j:])
            break
    '''
    for i in (var_names) :
        print(i)

    
    
    list_of_equ_dict = []
    equ_dict = {}
    for i in range(rows) :
        print("yes")
        equ_dict = {}
        for j in range(len(var_names)) :
            if not(var_names[j] in equ_arr[i]) :
                equ_dict[var_names[j]] = 0
            else :
                print("no")
                index = equ_arr[i].index(var_names[j])
                print(index)
                num = ""
                first_entry = True
                while (True) :
                    if ((equ_arr[i][index-1] == "+") and first_entry) or (index == 0 and first_entry) :
                        equ_dict[var_names[j]] = 1
                        break
                    elif (equ_arr[i][index-1] == "-") and first_entry :
                        equ_dict[var_names[j]] = -1
                        break
                    elif ((equ_arr[i][index-1] != ".") and (not(equ_arr[i][index-1].isdigit())) and (equ_arr[i][index-1] != "-")) or (index == 0) :
                        break
                    elif (equ_arr[i][index-1] == "-") :
                        num += equ_arr[i][index-1]
                        break
                    else :
                        num += equ_arr[i][index-1]
                        index -=1
                    first_entry = False
                if not first_entry : equ_dict[var_names[j]] = float(num[::-1])
        list_of_equ_dict.append(equ_dict)

    for i in range(rows) :
        list_of_equ_dict[i]["b" + str(i)] = float(equ_arr[i].split("=")[-1])


    for i in list_of_equ_dict :
        print(i)

    return convert_from_dic_to_2darr(list_of_equ_dict, rows) , rows,  precission

#=================================================================================

def convert_from_dic_to_2darr(arr_dic, rows):
    equ_arr1d = []
    for i in arr_dic:
        for j in i:
            equ_arr1d.append(i[j])

    arr = np.array(equ_arr1d)
    equ_arr2d = arr.reshape(rows, rows+1)

    print(equ_arr2d[:,:rows])


    return equ_arr2d

#==================================================================================

def conver_from_arr_to_dic(arr):
    ans_dic={}
    for i in range(len(arr)) :
        ans_dic[var_names[i]] = arr[i]
    return ans_dic


#====================================================================================

def check_equs_validity(equ_arr, rows) :
    global var_names
    '''
    for i in range(rows) :
        equ = re.split('\+|=|-', equ_arr[i])
        if len(equ) > (rows + 1) :
            return "Number of variables must be equal to the number of equations"
    
    valid_input = False
    for i in range(rows) :
        equ = re.split('\+|=|-', equ_arr[i])
        if len(equ) != (rows + 1) :
            continue
        else :
            valid_input = True
            break
    
    if (valid_input == False) :
        return "Number of variables must be equal to the number of equations"
    '''
    for i in range(rows) :
        equ = re.split('\+|=|-', equ_arr[i])
        for i in range(len(equ)-1) :
            for j in range(len(equ[i])) :
                if equ[i][j].isalpha() :
                    var_names.append(equ[i][j:])

    if len(set(var_names)) > rows :
        return "Number of variables must be equal to the number of equations"
    elif len(set(var_names)) < rows :
        return "Number of variables must be equal to the number of equations"
    else :
        var_names = list(set(var_names))


    return "valid"

#generate_mat(equ_arr ,3)
    

app.run(debug = True)