# Created by: Zack Isingoma
# Created on: 28th Jan 2022.
# merges user inputs

def joined(list_a, list_b):
    joined_list = []
    for i in range(len(list_a)):
        joined_list.append(list_a[i])
        joined_list.append(list_b[i])
    return joined(list_a, list_b)


def main():
    first_list = input("Enter the elements you want in the list: ")
    second_list = input("Enter the elements of the second list: ")
    print("List a is:", first_list)
    print("List b is:", second_list)
    merged_list = (first_list, second_list)
    final_list = ",".join(merged_list)
    print(final_list)


if __name__ == "__main__":
    main()
