from typing import Union

my_list: list[Union[int, str]] = [1,2,"小米","小琪"]

def func(data: Union[int, str]) -> Union[int, str]:
    pass

func()