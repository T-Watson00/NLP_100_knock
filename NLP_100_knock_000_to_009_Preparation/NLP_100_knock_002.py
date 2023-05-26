from sys import stdin as std

def main() :
    Input :list[str] =  list(map(str,std.readline().strip()))
    Input_string_list = operater(string_list=Input)


class operater :
    def __init__(self,string_list:list[str]) -> None :
        self.string_list :list[str]= string_list
        self.list_length :int = len(string_list)

    def str_to_deque_in_list(self) :
        for letters in self.string_list :
            


    def mixing_eachother(self) :
        while self