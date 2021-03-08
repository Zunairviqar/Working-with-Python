class BitList:
    def __init__(self, InputBits):
        if InputBits[:2] != '0b':
            raise ValueError('Did not start with 0b')
        # print(InputBits[2:])
        self.neededbits = InputBits[2:]
        for i in range(len(self.neededbits)):
            if self.neededbits[i] != '0' and self.neededbits[i] != '1':
                raise ValueError('Does not consist only of 1s and 0s')

    @staticmethod
    def from_ints(*args):
        print(args)
        for i in range(len(args)):
            if args[i] != 0 and args[i] != 1:
                raise ValueError('Does not consist only of 1s and 0s')
        s = '0b' + ''.join([str(a) for a in args])
        return BitList(s)

    def __str__(self):
        return str(self.neededbits)

    def __eq__(self, other):
        return self.neededbits == other.neededbits

    def arithmetic_shift_left(self):
        print(self.neededbits)
        tmp = self.neededbits[1:]
        tmp = tmp + '0'
        self.neededbits = tmp

    def arithmetic_shift_right(self):
        print(self.neededbits)
        tmp = self.neededbits[:-1]
        tmp = tmp[0] + tmp
        self.neededbits = tmp

    def bitwise_and(self, otherBitList):
        if len(self.neededbits) == len(otherBitList.neededbits):
            FirstList = list(int(a) for a in self.neededbits)
            SecondList = list(int(a) for a in otherBitList.neededbits)
            ThirdList = []
            for i in range(len(FirstList)):
                ThirdList.append(FirstList[i]*SecondList[i])
            NewBitList = ''.join(str(a) for a in ThirdList)
            NewBitList = '0b'+ NewBitList
            return BitList(NewBitList)
        else:
            print("Lenghts of Both BitLists need to be equal")

    def decode(self, encoding = 'us-ascii'):
        if encoding == 'us-ascii':
            CodePoints = []
            while self.neededbits:
                CodePoints.append(self.neededbits[-7:])
                self.neededbits = self.neededbits[:-7]
            CodePoints.reverse()
            CodePoints[0] = CodePoints[0].zfill(7)
            CodePointsDecimal = []
            CodePointsDecimalValue = []
            CodePointsString = []
            for i in range(len(CodePoints)):
                CodePointsDecimal.append(str(int(CodePoints[i], 2)))
                CodePointsDecimalValue.append(int(CodePoints[i], 2))
                CodePointsString.append(chr(CodePointsDecimalValue[i]))
            DecodedString = ''
            DecodedString = DecodedString.join(CodePointsString)
            return DecodedString
        f = 0
        List = []
        counters = []
        if encoding == 'utf-8':
            CodePoints = []
            while f < len(self.neededbits):
                counter = 1
                count = 0
                if self.neededbits[f + 1] == '1':
                    for i in range(5):
                        if self.neededbits[f + i] == '1':
                            count = count + 1
                            counter = counter + 1
                        else:
                            break
                NewByteString = self.neededbits[f:f + 8 * count]
                f = f + 8 * count
                List.append(NewByteString)
            x = []
            for i in range(len(List)):
                x = breakutf(List[i])
            CodePoints = x
            CodePointsDecimal = []
            CodePointsDecimalValue = []
            CodePointsString = []
            for i in range(len(CodePoints)):
                CodePointsDecimal.append(str(int(CodePoints[i], 2)))
                CodePointsDecimalValue.append(int(CodePoints[i], 2))
                CodePointsString.append(chr(CodePointsDecimalValue[i]))
            DecodedString = ''
            DecodedString = DecodedString.join(CodePointsString)
            return DecodedString

# I tried some implementation of utf-8. Since it is optional, I tried to complete it but it doesnt work to its full functionality.

UtfBinary = []
def breakutf(OriginalByte):
    count = 1
    if OriginalByte[0] == '1':
        for i in range(5):
            if OriginalByte[i] == '1':
                count = count + 1
                ByteToUse = OriginalByte[count:]
            else:
                break
        x = 8 - count
        NewByteString = ByteToUse[:x]
        ByteToUse = ByteToUse[x:]
        for i in range(count - 2):
            NewByteString = NewByteString + ByteToUse[2:8]
            ByteToUse = ByteToUse[8:]
        UtfBinary.append(NewByteString)
        return UtfBinary

if __name__ == '__main__':
    data = []
    Continue = True
    while Continue == True:
        OriginalByte = input("Enter your binary sequence: ")
        ByteCorrect = False
        while ByteCorrect == False:
            ByteCorrect = True
            for i in range(len(OriginalByte)):
                if OriginalByte[i] != '0' and OriginalByte[i] != '1' and OriginalByte[i] != '/' and OriginalByte[i] != ' ':
                    OriginalByte = input("Re-Enter your binary sequence: ")
                    ByteCorrect = False
                    break
        OriginalByte = OriginalByte.replace(" ", "")
        Encoding = input("Enter your preferred encoding: ")
        EncodingEntered = False
        while EncodingEntered == False:
            EncodingEntered = True
            if Encoding != 'us-ascii' and Encoding != 'utf-8':
                Encoding = input(
                    "Sorry, we do not support the encoding you entered. Please choose either 'us-ascii' or 'utf-8': ")
                EncodingEntered = False

        NotinData = False

        for i in range(len(data)):
            if OriginalByte == data[i][0] and Encoding == data[i][1]:
                NotinData = True
                print('you already entered those bits and encoding:', data[i][2])
                break

        if NotinData == False:
            print('Input: ', OriginalByte)
            CopyOriginalByte = OriginalByte

            if Encoding == 'us-ascii':
                CodePoints = []
                while OriginalByte:
                    CodePoints.append(OriginalByte[-7:])
                    OriginalByte = OriginalByte[:-7]
                CodePoints.reverse()
                CodePoints[0] = CodePoints[0].zfill(7)
                CodePointsBinary = ' '
                CodePointsBinary = CodePointsBinary.join(CodePoints)

                print('Code Points Binary: ', CodePointsBinary)

                CodePointsDecimal = []
                CodePointsDecimalValue = []
                CodePointsString = []

                for i in range(len(CodePoints)):
                    CodePointsDecimal.append(str(int(CodePoints[i], 2)))
                    CodePointsDecimalValue.append(int(CodePoints[i], 2))
                    CodePointsString.append(chr(CodePointsDecimalValue[i]))

                CodePointsDecimalString = ' '
                CodePointsDecimalString = CodePointsDecimalString.join(CodePointsDecimal)
                print('Code Points Decimal:', CodePointsDecimalString)

                DecodedString = ''
                DecodedString = DecodedString.join(CodePointsString)
                print('Decoded String:', DecodedString)

            f = 0
            List = []
            counters = []
            if Encoding == 'utf-8':
                CodePoints = []
                while f < len(OriginalByte):
                    counter = 1
                    count = 0
                    if OriginalByte[f + 1] == '1':
                        for i in range(5):
                            if OriginalByte[f + i] == '1':
                                count = count + 1
                                counter = counter + 1
                            else:
                                break
                    NewByteString = OriginalByte[f:f + 8 * count]
                    f = f + 8 * count
                    List.append(NewByteString)
                x = []
                for i in range(len(List)):
                    x = breakutf(List[i])
                CodePoints = x
                CodePointsBinary = ' '
                CodePointsBinary = CodePointsBinary.join(CodePoints)
                print('Code Points Binary: ', CodePointsBinary)

                CodePointsDecimal = []
                CodePointsDecimalValue = []
                CodePointsString = []

                for i in range(len(CodePoints)):
                    CodePointsDecimal.append(str(int(CodePoints[i], 2)))
                    CodePointsDecimalValue.append(int(CodePoints[i], 2))
                    CodePointsString.append(chr(CodePointsDecimalValue[i]))

                CodePointsDecimalString = ' '
                CodePointsDecimalString = CodePointsDecimalString.join(CodePointsDecimal)
                print('Code Points Decimal:', CodePointsDecimalString)

                DecodedString = ''
                DecodedString = DecodedString.join(CodePointsString)
                print('Decoded String:', DecodedString)

            data.append((CopyOriginalByte, Encoding, DecodedString))

        ContinueString = input('Type Y to enter more bits?')
        if ContinueString != 'Y':
            Continue = False
        else:
            Continue = True

    print('\n')
    print('Thanks, these were all the bits you entered!')
    for i in range(len(data)):
        print(data[i][1] + '-' + data[i][0] + ' >>> ' + data[i][2])