def main() :
    Input :str = str(input())
    input_string = String_reverse(string=Input)
    operated_string = input_string.roop_reverser()
    print(operated_string)





##main()関数に用いるclass,function
class String_reverse :
    def __init__(self,string:str) -> None:
        self.string = string

    def roop_reverser(self) -> str :
        reversed_string = ""
        for i in range(len(self.string)-1,-1,-1) :          ##stringの後ろから参照できるようにfor文のindexを設定
            reversed_string += self.string[i]
        return reversed_string



if __name__ == "__main__"  :
    main()