class Calculator:


    def addition(self, n1, n2):
        result = n1 + n2
        return result


    def subtraction(self, n1, n2):
        result = n1 - n2
        return result


    def divide(self, n1, n2):
        result = n1/n2
        return result


    def multiply(self, n1, n2):
        result = n1 * n2
        return result


    def squareroot(self, n1):
        result = n1 ** (1/2)
        return result

    def calculate(self, n1, n2, operation):
        if operation == "**":
            answer = self.squareroot(n1)
            return answer
        elif operation == "-":
            answer = self.subtraction(n1,n2)
            return answer
        elif operation == "+":
            answer = self.addition(n1, n2)
            return answer
        elif operation == "/":
            answer = self.divide(n1, n2)
            return answer
        elif operation == "*":
            answer = self.multiply(n1, n2)
            return answer

    OPERATIONS = {"+": addition,
                  "-": subtraction,
                  "/": divide,
                  "*": multiply,
                  "**": squareroot
                  }

