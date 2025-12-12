try:
    result = 1/0
except TypeError as error:
    print(error)
except ZeroDivisionError:
    print("batatinhas")
finally:
    print("concluimos o código")