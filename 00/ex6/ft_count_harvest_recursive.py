def ft_count_harvest_recursive():
    Day = int(input("Days until harvest: "))

    def helper(i):
        if i > Day:
            return
        print("Day", i)
        helper(i + 1)
    helper(1)
    print("Harvest time!")


ft_count_harvest_recursive()
