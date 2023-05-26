def main() :
    Input :str = str(input())
    Input_string = operater(string=Input)
    operated_string = Input_string.extract_and_connect_odd_index_letter()
    print(operated_string)





class operater :

    def __init__(self,string:str) -> None :
        self.string = string

    def extract_and_connect_odd_index_letter(self) :
        self.length_of_string = len(self.string)
        connected_string = ""
        for i in range(0,self.length_of_string,2) :
            connected_string += self.string[i]
        return connected_string



if __name__ == "__main__" :
    main()