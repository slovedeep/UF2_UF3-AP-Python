import getMenu as gM
import functions as f


def main():
    operation = gM.menu()

    if operation == 1:
        f.get_data()
    elif operation == 2:
        f.show_std()
    else:
        f.analyze_records()






if __name__ == '__main__':
    main()