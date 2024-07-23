#Area of Circle = PI*Raduis*radius

def Area(Radius,PI=3.14):
    print('Radius ',Radius)
    print('PI value ',PI)
    Result = PI*Radius*Radius
    return Result

def main():
    #Positional argument and default
    Output_1 = Area(10)
    print(Output_1)
    #keyword argument
    Output_2 = Area(PI=20,Radius=3)
    print(Output_2)
    #keyword argument and second is ddefault
    Output_3=Area(Radius=9)
    print(Output_3)

if __name__ == "__main__":
    main()

