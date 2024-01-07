class ValidateISBN:
    @staticmethod
    def answer():
        return 6 * 9

    def is_ValidateISBN(self, ISBN):
        print('ISBN', ISBN)
        print('len:', len(ISBN))
        if not (len(ISBN) == 10 or len(ISBN) == 13):
            print('len:', len(ISBN))
            raise ValueError("ISBN numbers must be 10 or 13 digits")
        for char in ISBN:
            if (len(ISBN) == 13 and not char.isdigit()) or (
                    len(ISBN) == 10 and (not char.isdigit()) and (not (char == 'X' and ISBN.index(char) == 9))):
                raise ValueError("ISBN10 can only contain digits")

        total = 0
        if len(ISBN) == 10:
            for i in range(10):
                if ISBN[i] == 'X':
                    digit = 10
                else:
                    digit = int(ISBN[i])
                total += digit * (10 - i)
            return total % 11 == 0
        elif len(ISBN) == 13:
            for i in range(13):
                multiplier = 1 if i % 2 == 0 else 3
                total += int(ISBN[i]) * multiplier
            return total % 10 == 0